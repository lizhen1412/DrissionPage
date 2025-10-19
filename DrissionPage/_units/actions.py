#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Website  : https://DrissionPage.cn
@Copyright: (c) 2020 by g1879, Inc. All Rights Reserved.
"""
from pathlib import Path
from platform import system
from time import sleep, perf_counter

from .._functions.keys import modifierBit, make_input_data, input_text_or_keys, Keys
from .._functions.settings import Settings as _S
from .._functions.web import location_in_viewport


class Actions:
    """
    Actions 类：用于模拟用户的鼠标和键盘操作
    
    该类提供了一系列链式调用的方法，可以模拟真实用户的交互行为，包括：
    - 鼠标移动、点击、拖拽、滚动
    - 键盘按键、输入
    - 文件拖放
    
    所有方法都返回 self，支持链式调用，例如：
    actions.move_to(element).click().type('hello')
    """

    def __init__(self, owner):
        """
        初始化 Actions 对象
        
        Args:
            owner: 拥有此 Actions 对象的页面对象（ChromiumPage 或 ChromiumTab）
        """
        self.owner = owner  # 页面对象的引用
        self._dr = owner.driver  # Chrome DevTools Protocol (CDP) 驱动对象
        self.modifier = 0  # 修饰键状态，使用位掩码表示：Alt=1, Ctrl=2, Meta/Command=4, Shift=8
        self.curr_x = 0  # 当前鼠标在视口中的 x 坐标
        self.curr_y = 0  # 当前鼠标在视口中的 y 坐标
        self._holding = 'left'  # 当前按下的鼠标按键（'left'、'right' 或 'middle'）

    def move_to(self, ele_or_loc, offset_x=None, offset_y=None, duration=.5):
        """
        将鼠标移动到指定元素或坐标位置
        
        该方法会自动处理滚动，确保目标位置在视口内可见。
        如果目标在视口外，会先滚动页面使其可见，然后再移动鼠标。
        
        Args:
            ele_or_loc: 目标元素或坐标
                - ChromiumElement 对象：移动到元素位置
                - 定位符字符串：先查找元素，再移动到元素位置
                - (x, y) 坐标元组/列表：移动到页面坐标（非视口坐标）
            offset_x: x 轴偏移量，默认为 None
                - None 且 offset_y 也为 None：移动到元素中心点
                - 0 或其他数值：在元素左上角基础上偏移
            offset_y: y 轴偏移量，默认为 None
            duration: 移动持续时间（秒），模拟真实鼠标移动速度，默认 0.5 秒
        
        Returns:
            self: 返回自身，支持链式调用
        """
        is_loc = False  # 标记是否为坐标模式
        mid_point = offset_x == offset_y is None  # 判断是否移动到中心点（两个偏移都是None）
        if offset_x is None:
            offset_x = 0
        if offset_y is None:
            offset_y = 0
            
        # 处理不同类型的输入参数
        if isinstance(ele_or_loc, (tuple, list)):
            # 坐标模式：直接使用页面坐标
            is_loc = True
            lx = ele_or_loc[0] + offset_x  # 页面坐标 x
            ly = ele_or_loc[1] + offset_y  # 页面坐标 y
        elif isinstance(ele_or_loc, str) or ele_or_loc._type == 'ChromiumElement':
            # 元素模式：需要获取元素位置
            ele_or_loc = self.owner(ele_or_loc)  # 如果是字符串定位符，先查找元素
            self.owner.scroll.to_see(ele_or_loc)  # 滚动使元素可见
            x, y = ele_or_loc.rect.midpoint if mid_point else ele_or_loc.rect.location
            lx = x + offset_x  # 元素在页面中的 x 坐标
            ly = y + offset_y  # 元素在页面中的 y 坐标
        else:
            raise ValueError(_S._lang.join(_S._lang.INCORRECT_TYPE_, 'ele_or_loc',
                                           ALLOW_TYPE=_S._lang.ELE_LOC_FORMAT, CURR_VAL=ele_or_loc))

        # 如果目标位置不在当前视口内，需要滚动页面
        if not location_in_viewport(self.owner, lx, ly):
            # 计算视口尺寸
            clientWidth = self.owner._run_js('return document.body.clientWidth;')
            clientHeight = self.owner._run_js('return document.body.clientHeight;')
            # 将目标位置滚动到视口中央
            self.owner.scroll.to_location(lx - clientWidth // 2, ly - clientHeight // 2)

        # 计算视口坐标（考虑固定定位等不随滚动条滚动的元素）
        if is_loc:
            # 坐标模式：将页面坐标转换为视口坐标
            cx, cy = location_to_client(self.owner, lx, ly)
        else:
            # 元素模式：直接获取元素在视口中的位置
            x, y = ele_or_loc.rect.viewport_midpoint if mid_point else ele_or_loc.rect.viewport_location
            cx = x + offset_x
            cy = y + offset_y

        # 计算相对当前位置的偏移量
        ox = cx - self.curr_x
        oy = cy - self.curr_y
        # 执行移动操作
        self.move(ox, oy, duration)
        return self

    def move(self, offset_x=0, offset_y=0, duration=.5):
        """
        相对当前位置移动鼠标
        
        该方法通过在起点和终点之间插入多个中间点，模拟真实的鼠标移动轨迹。
        移动速度是恒定的，每个中间点之间间隔约 0.02 秒（50fps）。
        
        Args:
            offset_x: x 轴偏移量（像素），正值向右，负值向左
            offset_y: y 轴偏移量（像素），正值向下，负值向上
            duration: 移动持续时间（秒），默认 0.5 秒
        
        Returns:
            self: 返回自身，支持链式调用
        """
        # 最小持续时间为 0.02 秒（防止移动过快）
        duration = .02 if duration < .02 else duration
        # 计算中间点数量，以 50fps 的速度进行插值
        num = int(duration * 50)

        # 生成从起点到终点的线性插值点列表
        # 使用列表推导式生成 num-1 个中间点
        points = [(self.curr_x + i * (offset_x / num),
                   self.curr_y + i * (offset_y / num)) for i in range(1, num)]
        # 添加终点，确保最终精确到达目标位置
        points.append((self.curr_x + offset_x, self.curr_y + offset_y))

        # 遍历每个点，依次移动鼠标
        for x, y in points:
            t = perf_counter()  # 记录当前时间，用于控制移动速度
            self.curr_x = x
            self.curr_y = y
            # 通过 CDP 协议发送鼠标移动事件
            self._dr.run('Input.dispatchMouseEvent', type='mouseMoved', button=self._holding,
                         x=self.curr_x, y=self.curr_y, modifiers=self.modifier)
            # 计算需要等待的时间，确保每次移动间隔约 0.02 秒
            ss = .02 - perf_counter() + t
            if ss > 0:
                sleep(ss)

        return self

    def click(self, on_ele=None, times=1):
        """
        左键单击（或多次点击）
        
        Args:
            on_ele: 要点击的元素或坐标，None 表示在当前位置点击
            times: 点击次数，用于实现双击、三击等，默认为 1
        
        Returns:
            self: 返回自身，支持链式调用
        """
        self._hold(on_ele, 'left', times).wait(.05)._release('left')
        return self

    def r_click(self, on_ele=None, times=1):
        """
        右键单击（或多次点击）
        
        Args:
            on_ele: 要点击的元素或坐标，None 表示在当前位置点击
            times: 点击次数，默认为 1
        
        Returns:
            self: 返回自身，支持链式调用
        """
        self._hold(on_ele, 'right', times).wait(.05)._release('right')
        return self

    def m_click(self, on_ele=None, times=1):
        """
        中键单击（或多次点击）
        
        Args:
            on_ele: 要点击的元素或坐标，None 表示在当前位置点击
            times: 点击次数，默认为 1
        
        Returns:
            self: 返回自身，支持链式调用
        """
        self._hold(on_ele, 'middle', times).wait(.05)._release('middle')
        return self

    def hold(self, on_ele=None):
        """
        按住鼠标左键
        
        常用于拖拽操作：hold() -> move_to() -> release()
        
        Args:
            on_ele: 要按住的元素或坐标，None 表示在当前位置按住
        
        Returns:
            self: 返回自身，支持链式调用
        """
        self._hold(on_ele, 'left')
        return self

    def release(self, on_ele=None):
        """
        释放鼠标左键
        
        Args:
            on_ele: 释放位置的元素或坐标，None 表示在当前位置释放
        
        Returns:
            self: 返回自身，支持链式调用
        """
        if on_ele:
            self.move_to(on_ele, duration=.2)  # 先移动到目标位置
        self._release('left')
        return self

    def r_hold(self, on_ele=None):
        """
        按住鼠标右键
        
        Args:
            on_ele: 要按住的元素或坐标，None 表示在当前位置按住
        
        Returns:
            self: 返回自身，支持链式调用
        """
        self._hold(on_ele, 'right')
        return self

    def r_release(self, on_ele=None):
        """
        释放鼠标右键
        
        Args:
            on_ele: 释放位置的元素或坐标，None 表示在当前位置释放
        
        Returns:
            self: 返回自身，支持链式调用
        """
        if on_ele:
            self.move_to(on_ele, duration=.2)  # 先移动到目标位置
        self._release('right')
        return self

    def m_hold(self, on_ele=None):
        """
        按住鼠标中键
        
        Args:
            on_ele: 要按住的元素或坐标，None 表示在当前位置按住
        
        Returns:
            self: 返回自身，支持链式调用
        """
        self._hold(on_ele, 'middle')
        return self

    def m_release(self, on_ele=None):
        """
        释放鼠标中键
        
        Args:
            on_ele: 释放位置的元素或坐标，None 表示在当前位置释放
        
        Returns:
            self: 返回自身，支持链式调用
        """
        if on_ele:
            self.move_to(on_ele, duration=.2)  # 先移动到目标位置
        self._release('middle')
        return self

    def _hold(self, on_ele=None, button='left', count=1):
        """
        内部方法：按下鼠标按键
        
        Args:
            on_ele: 要按住的元素或坐标，None 表示在当前位置按住
            button: 按键类型，'left'、'right' 或 'middle'
            count: 点击次数，用于实现双击、三击等
        
        Returns:
            self: 返回自身，支持链式调用
        """
        if on_ele:
            self.move_to(on_ele, duration=.2)  # 先移动到目标位置
        # 通过 CDP 协议发送鼠标按下事件
        self._dr.run('Input.dispatchMouseEvent', type='mousePressed', button=button, clickCount=count,
                     x=self.curr_x, y=self.curr_y, modifiers=self.modifier)
        self._holding = button  # 记录当前按住的按键
        return self

    def _release(self, button):
        """
        内部方法：释放鼠标按键
        
        Args:
            button: 按键类型，'left'、'right' 或 'middle'
        
        Returns:
            self: 返回自身，支持链式调用
        """
        # 通过 CDP 协议发送鼠标释放事件
        self._dr.run('Input.dispatchMouseEvent', type='mouseReleased', button=button, clickCount=1,
                     x=self.curr_x, y=self.curr_y, modifiers=self.modifier)
        self._holding = 'left'  # 重置为默认状态
        return self

    def scroll(self, delta_y=0, delta_x=0, on_ele=None):
        """
        在当前位置或指定元素上执行滚轮操作
        
        Args:
            delta_y: 垂直滚动量，正值向下滚动，负值向上滚动
            delta_x: 水平滚动量，正值向右滚动，负值向左滚动
            on_ele: 要滚动的元素或坐标，None 表示在当前位置滚动
        
        Returns:
            self: 返回自身，支持链式调用
        """
        if on_ele:
            self.move_to(on_ele, duration=.2)  # 先移动到目标位置
        # 通过 CDP 协议发送滚轮事件
        self._dr.run('Input.dispatchMouseEvent', type='mouseWheel', x=self.curr_x, y=self.curr_y,
                     deltaX=delta_x, deltaY=delta_y, modifiers=self.modifier)
        return self

    def up(self, pixel):
        """
        向上移动鼠标
        
        Args:
            pixel: 移动的像素数
        
        Returns:
            self: 返回自身，支持链式调用
        """
        return self.move(0, -pixel)

    def down(self, pixel):
        """
        向下移动鼠标
        
        Args:
            pixel: 移动的像素数
        
        Returns:
            self: 返回自身，支持链式调用
        """
        return self.move(0, pixel)

    def left(self, pixel):
        """
        向左移动鼠标
        
        Args:
            pixel: 移动的像素数
        
        Returns:
            self: 返回自身，支持链式调用
        """
        return self.move(-pixel, 0)

    def right(self, pixel):
        """
        向右移动鼠标
        
        Args:
            pixel: 移动的像素数
        
        Returns:
            self: 返回自身，支持链式调用
        """
        return self.move(pixel, 0)

    def key_down(self, key):
        """
        按下键盘按键（不释放）
        
        该方法用于模拟按住某个键，常用于组合键操作。
        例如：key_down('ctrl').key_down('c').key_up('c').key_up('ctrl')
        
        Args:
            key: 按键名称，可以是：
                - Keys 类中的常量名（如 'ENTER'、'TAB'）
                - 字符（如 'a'、'1'）
                - 修饰键（ALT、CTRL、META/COMMAND、SHIFT）
        
        Returns:
            self: 返回自身，支持链式调用
        
        Note:
            修饰键（Alt、Ctrl、Command、Shift）会被记录到 modifier 状态中，
            影响后续的鼠标和键盘事件。
        """
        # 尝试从 Keys 类获取按键常量，如果不存在则使用原值
        key = getattr(Keys, key.upper(), key)
        # 检查是否为修饰键：Alt(\ue00a)、Ctrl(\ue009)、Meta/Command(\ue03d)、Shift(\ue008)
        if key in ('\ue009', '\ue008', '\ue00a', '\ue03d'):
            # 发送修饰键的实际按键事件
            # 注意：修饰键本身不带 modifier，所以使用 modifier=0
            data = make_input_data(0, key, False)
            if data:
                # 修饰键使用 rawKeyDown 类型
                data['type'] = 'rawKeyDown'
                self.owner._run_cdp('Input.dispatchKeyEvent', **data)
            
            # 使用位或运算添加修饰键标记
            self.modifier |= modifierBit.get(key, 0)
            return self

        # 生成键盘事件数据（keyDown 事件）
        data = make_input_data(self.modifier, key, False)
        if not data:
            raise ValueError(_S._lang.join(_S._lang.NO_SUCH_KEY_, key))
        # 通过 CDP 协议发送键盘按下事件
        self.owner._run_cdp('Input.dispatchKeyEvent', **data)
        return self

    def key_up(self, key):
        """
        释放键盘按键
        
        该方法用于释放之前按下的按键。
        
        Args:
            key: 按键名称，可以是：
                - Keys 类中的常量名（如 'ENTER'、'TAB'）
                - 字符（如 'a'、'1'）
                - 修饰键（ALT、CTRL、META/COMMAND、SHIFT）
        
        Returns:
            self: 返回自身，支持链式调用
        
        Note:
            修饰键（Alt、Ctrl、Command、Shift）释放时会从 modifier 状态中移除。
        """
        # 尝试从 Keys 类获取按键常量，如果不存在则使用原值
        key = getattr(Keys, key.upper(), key)
        # 检查是否为修饰键
        if key in ('\ue009', '\ue008', '\ue00a', '\ue03d'):
            # 使用位异或运算移除修饰键标记
            self.modifier ^= modifierBit.get(key, 0)
            
            # 发送修饰键的实际释放事件
            # 注意：释放时的 modifier 已经被清除了
            data = make_input_data(self.modifier, key, True)
            if data:
                self.owner._run_cdp('Input.dispatchKeyEvent', **data)
            return self

        # 生成键盘事件数据（keyUp 事件）
        data = make_input_data(self.modifier, key, True)
        if not data:
            raise ValueError(_S._lang.join(_S._lang.NO_SUCH_KEY_, key))
        # 通过 CDP 协议发送键盘释放事件
        self.owner._run_cdp('Input.dispatchKeyEvent', **data)
        return self

    def type(self, keys, interval=0):
        """
        逐个输入键盘按键
        
        该方法会模拟真实的打字过程，依次按下并释放每个按键。
        支持输入普通字符、特殊按键和修饰键组合。
        
        Args:
            keys: 要输入的内容，可以是：
                - 字符串：普通文本或包含特殊按键的字符串
                - 列表/元组：多个按键的序列
                - 数字：会转换为字符串
            interval: 每个按键之间的间隔时间（秒），默认为 0
        
        Returns:
            self: 返回自身，支持链式调用
        
        Note:
            - 修饰键（Alt、Ctrl、Command、Shift）会在输入过程中保持按下状态，
              在所有字符输入完成后统一释放
            - 特殊按键使用 Unicode 私有区域编码（\ue009 等）
        """
        modifiers = []  # 记录使用的修饰键，最后需要释放
        # 确保 keys 是字符串、列表或元组类型
        if not isinstance(keys, (str, tuple, list)):
            keys = str(keys)
            
        # 遍历每个按键序列
        for i in keys:
            # 遍历序列中的每个字符
            for character in i:
                # 如果是修饰键，添加到修饰键状态中
                if character in ('\ue009', '\ue008', '\ue00a', '\ue03d'):
                    self.modifier |= modifierBit.get(character, 0)
                    modifiers.append(character)  # 记录修饰键，后续需要释放
                    
                # 生成按键事件数据
                data = make_input_data(self.modifier, character, False)
                if data:
                    # 发送按键按下事件
                    self.owner._run_cdp('Input.dispatchKeyEvent', **data)
                    # 如果不是修饰键，立即发送释放事件
                    if character not in ('\ue009', '\ue008', '\ue00a', '\ue03d'):
                        data['type'] = 'keyUp'
                        self.owner._run_cdp('Input.dispatchKeyEvent', **data)
                else:
                    # 无法生成按键数据的字符，使用字符输入事件
                    self.owner._run_cdp('Input.dispatchKeyEvent', type='char', text=character)
                    
                # 等待指定的间隔时间
                sleep(interval)

        # 释放所有修饰键
        for m in modifiers:
            self.key_up(m)
        return self

    def input(self, text):
        """
        快速输入文本
        
        该方法不模拟按键过程，直接将文本插入到当前焦点元素中，速度更快。
        适用于需要快速输入大量文本的场景。
        
        Args:
            text: 要输入的文本内容
        
        Returns:
            self: 返回自身，支持链式调用
        
        Note:
            - 该方法不会触发 keydown/keyup 事件
            - 对于需要按键事件的场景，应使用 type() 方法
        """
        input_text_or_keys(self.owner, text)
        return self

    def drag_in(self, ele_or_loc, files=None, text=None, title=None, baseURL=None):
        """
        将文件或文本拖放到指定元素
        
        该方法模拟拖放操作，可以用于：
        - 上传文件（通过拖放文件到上传区域）
        - 拖放文本到可编辑区域
        - 拖放链接
        
        Args:
            ele_or_loc: 目标元素或坐标
            files: 要拖放的文件路径，可以是单个路径字符串或路径列表
            text: 要拖放的文本内容
            title: 文本的标题（用于 URI 列表）
            baseURL: 文本的基础 URL（用于 URI 列表）
        
        Returns:
            self: 返回自身，支持链式调用
        
        Raises:
            ValueError: 如果既没有提供 files 也没有提供 text
        
        Note:
            - files 和 text 参数互斥，只能提供其中一个
            - 拖放文件时，dragOperationsMask=16 表示复制操作
            - 拖放文本时，dragOperationsMask=1 表示移动操作
        """
        ele_or_loc = self.owner(ele_or_loc)  # 确保获取到元素对象
        x, y = ele_or_loc.rect.viewport_midpoint  # 获取元素中心点坐标
        
        if files:
            # 文件拖放模式
            items = []
            paths = []
            # 确保 files 是列表
            if isinstance(files, str):
                files = [files]
            # 处理每个文件路径
            for file in files:
                path = str(Path(file).absolute())  # 转换为绝对路径
                item = {'mimeType': 'text/plain', 'data': path}
                items.append(item)
                paths.append(path)
            # 构建拖放数据，dragOperationsMask=16 表示复制操作
            data = {'items': items, 'files': paths, 'dragOperationsMask': 16}

        elif text:
            # 文本拖放模式
            item = {'data': text}
            if title is not None:
                # 带标题的 URI 列表
                item['title'] = title
                item['mimeType'] = 'text/uri-list'
            elif baseURL is not None:
                # 带基础 URL 的 URI 列表
                item['baseURL'] = baseURL
                item['mimeType'] = 'text/uri-list'
            else:
                # 纯文本
                item['mimeType'] = 'text/plain'
            # 构建拖放数据，dragOperationsMask=1 表示移动操作
            data = {'items': [item], 'dragOperationsMask': 1}

        else:
            raise ValueError(_S._lang.NEED_FILES_OR_TEXT_ARG)

        # 发送拖放事件序列
        # 1. dragEnter：拖动进入目标元素
        self._dr.run('Input.dispatchDragEvent', type='dragEnter', x=x, y=y, data=data, modifiers=self.modifier)
        # 2. drop：在目标元素上释放
        self._dr.run('Input.dispatchDragEvent', type='drop', x=x, y=y, data=data, modifiers=self.modifier)
        return self

    def wait(self, second, scope=None):
        """
        等待指定时间
        
        Args:
            second: 等待的秒数
            scope: 等待的作用域（传递给页面的 wait 方法）
        
        Returns:
            self: 返回自身，支持链式调用
        """
        self.owner.wait(second=second, scope=scope)
        return self

    def open_chrome_menu(self):
        """
        打开 Chrome 浏览器菜单
        
        使用快捷键 Alt+F 打开 Chrome 的三点菜单（汉堡菜单）。
        这是 Chrome 在 Windows/Linux 上的标准快捷键。
        
        Returns:
            self: 返回自身，支持链式调用
        
        Note:
            macOS 上的 Chrome 没有打开三点菜单的键盘快捷键，
            此方法在 macOS 上可能无法工作。
        """
        return self.open_chrome_menu_windows()

    def open_chrome_menu_windows(self):
        """
        在 Windows 上打开 Chrome 菜单
        
        使用快捷键 Alt+F 打开 Chrome 的三点菜单（汉堡菜单）。
        这是 Chrome 在 Windows 上的标准快捷键。
        
        Returns:
            self: 返回自身，支持链式调用
        """
        # 按下 Alt，按下 f，释放 f，释放 Alt
        self.key_down(Keys.ALT).key_down('f').key_up('f').key_up(Keys.ALT)
        self.wait(.1)  # 等待菜单打开
        return self


def location_to_client(page, lx, ly):
    """
    将页面坐标转换为视口坐标
    
    页面坐标是相对于整个文档的绝对位置（包括滚动区域），
    视口坐标是相对于浏览器可见区域的位置（不包括滚动的部分）。
    
    Args:
        page: 页面对象
        lx: 页面 x 坐标
        ly: 页面 y 坐标
    
    Returns:
        tuple: (视口 x 坐标, 视口 y 坐标)
    
    算法：
        视口坐标 = 页面坐标 - 滚动偏移量
    """
    # 获取页面的水平滚动位置
    scroll_x = page._run_js('return document.documentElement.scrollLeft;')
    # 获取页面的垂直滚动位置
    scroll_y = page._run_js('return document.documentElement.scrollTop;')
    # 计算视口坐标
    return lx - scroll_x, ly - scroll_y
