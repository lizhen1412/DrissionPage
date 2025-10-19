#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Website  : https://DrissionPage.cn
@Copyright: (c) 2020 by g1879, Inc. All Rights Reserved.
"""
from typing import Union, Tuple, Any, Literal

from .._base.driver import Driver
from .._elements.chromium_element import ChromiumElement
from .._pages.chromium_base import ChromiumBase

KEYS = Literal['NULL', 'CANCEL', 'HELP', 'BACKSPACE', 'meta',
'TAB', 'CLEAR', 'RETURN', 'ENTER', 'SHIFT', 'CONTROL', 'command ',
'CTRL', 'ALT', 'PAUSE', 'ESCAPE', 'SPACE',
'PAGE_UP', 'PAGE_DOWN', 'END', 'HOME', 'LEFT', 'UP',
'RIGHT', 'DOWN', 'INSERT',
'DELETE', 'DEL', 'SEMICOLON', 'EQUALS', 'NUMPAD0', 'NUMPAD1', 'NUMPAD2',
'NUMPAD3', 'NUMPAD4', 'NUMPAD5', 'NUMPAD6', 'NUMPAD7', 'NUMPAD8', 'NUMPAD9',
'MULTIPLY', 'ADD', 'SUBTRACT', 'DECIMAL', 'DIVIDE', 'F1', 'F2',
'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'META', 'COMMAND ',
'null', 'cancel', 'help', 'backspace', 'tab', 'clear', 'return', 'enter',
'shift', 'control', 'ctrl', 'alt', 'pause',
'escape', 'space', 'page_up', 'page_down', 'end', 'home', 'left', 'up',
'right', 'down', 'insert', 'delete', 'del',
'semicolon', 'equals', 'numpad0', 'numpad1', 'numpad2', 'numpad3', 'numpad4', 'numpad5',
'numpad6', 'numpad7', 'numpad8', 'numpad9', 'multiply', 'add', 'subtract', 'decimal',
'divide', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12',
'\ue000', '\ue002', '\ue003', '\ue004', '\ue005', '\ue006', '\ue007', '\ue008', '\ue009',
'\ue009', '\ue00a', '\ue00b', '\ue00c', '\ue00d', '\ue00e', '\ue00f', '\ue010', '\ue011',
'\ue012', '\ue013', '\ue014', '\ue015', '\ue016', '\ue017', '\ue017', '\ue018', '\ue019',
'\ue01a', '\ue01b', '\ue01c', '\ue01d', '\ue01e', '\ue01f', '\ue020', '\ue021', '\ue022',
'\ue023', '\ue024', '\ue025', '\ue027', '\ue028', '\ue029', '\ue031', '\ue032', '\ue033', '\ue034',
'\ue035', '\ue036', '\ue037', '\ue038', '\ue039', '\ue03a', '\ue03b', '\ue03c', '\ue03d', '\ue03d',
'`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'q', 'w',
'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\', 'a', 's', 'd', 'f',
'g', 'h', 'j', 'k', 'l', ';', '\'', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',',
'.', '/', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+',
'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', 'A', 'S', 'D',
'F', 'G', 'H', 'J', 'K', 'L', ':', '"', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?'
]


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

    owner: ChromiumBase = ...
    _dr: Driver = ...
    modifier: int = ...  # 修饰键状态，使用位掩码表示：Alt=1, Ctrl=2, Meta/Command=4, Shift=8
    curr_x: float = ...  # 当前鼠标在视口中的 x 坐标
    curr_y: float = ...  # 当前鼠标在视口中的 y 坐标
    _holding: str = ...  # 当前按下的鼠标按键（'left'、'right' 或 'middle'）

    def __init__(self, owner: ChromiumBase):
        """
        初始化 Actions 对象
        
        :param owner: 拥有此 Actions 对象的页面对象（ChromiumPage 或 ChromiumTab）
        """
        ...

    def move_to(self, ele_or_loc: Union[ChromiumElement, Tuple[float, float], str],
                offset_x: float = 0, offset_y: float = 0, duration: float = .5) -> Actions:
        """
        将鼠标移动到指定元素或坐标位置
        
        该方法会自动处理滚动，确保目标位置在视口内可见。
        如果目标在视口外，会先滚动页面使其可见，然后再移动鼠标。
        
        :param ele_or_loc: 目标元素或坐标
            - ChromiumElement 对象：移动到元素位置
            - 定位符字符串：先查找元素，再移动到元素位置
            - (x, y) 坐标元组：移动到页面坐标（非视口坐标）
        :param offset_x: x 轴偏移量，默认为 0
            - None 且 offset_y 也为 None：移动到元素中心点
            - 0 或其他数值：在元素左上角基础上偏移
        :param offset_y: y 轴偏移量，默认为 0
        :param duration: 移动持续时间（秒），模拟真实鼠标移动速度，默认 0.5 秒
        :return: 返回自身，支持链式调用
        """
        ...

    def move(self, offset_x: float = 0, offset_y: float = 0, duration: float = .5) -> Actions:
        """
        相对当前位置移动鼠标
        
        该方法通过在起点和终点之间插入多个中间点，模拟真实的鼠标移动轨迹。
        移动速度是恒定的，每个中间点之间间隔约 0.02 秒（50fps）。
        
        :param offset_x: x 轴偏移量（像素），正值向右，负值向左
        :param offset_y: y 轴偏移量（像素），正值向下，负值向上
        :param duration: 移动持续时间（秒），默认 0.5 秒
        :return: 返回自身，支持链式调用
        """
        ...

    def click(self, on_ele: Union[ChromiumElement, str] = None, times: int = 1) -> Actions:
        """
        左键单击（或多次点击）
        
        :param on_ele: 要点击的元素或坐标，None 表示在当前位置点击
        :param times: 点击次数，用于实现双击、三击等，默认为 1
        :return: 返回自身，支持链式调用
        """
        ...

    def r_click(self, on_ele: Union[ChromiumElement, str] = None, times: int = 1) -> Actions:
        """
        右键单击（或多次点击）
        
        :param on_ele: 要点击的元素或坐标，None 表示在当前位置点击
        :param times: 点击次数，默认为 1
        :return: 返回自身，支持链式调用
        """
        ...

    def m_click(self, on_ele: Union[ChromiumElement, str] = None, times: int = 1) -> Actions:
        """
        中键单击（或多次点击）
        
        :param on_ele: 要点击的元素或坐标，None 表示在当前位置点击
        :param times: 点击次数，默认为 1
        :return: 返回自身，支持链式调用
        """
        ...

    def hold(self, on_ele: Union[ChromiumElement, str] = None) -> Actions:
        """
        按住鼠标左键
        
        常用于拖拽操作：hold() -> move_to() -> release()
        
        :param on_ele: 要按住的元素或坐标，None 表示在当前位置按住
        :return: 返回自身，支持链式调用
        """
        ...

    def release(self, on_ele: Union[ChromiumElement, str] = None) -> Actions:
        """
        释放鼠标左键
        
        :param on_ele: 释放位置的元素或坐标，None 表示在当前位置释放
        :return: 返回自身，支持链式调用
        """
        ...

    def r_hold(self, on_ele: Union[ChromiumElement, str] = None) -> Actions:
        """
        按住鼠标右键
        
        :param on_ele: 要按住的元素或坐标，None 表示在当前位置按住
        :return: 返回自身，支持链式调用
        """
        ...

    def r_release(self, on_ele: Union[ChromiumElement, str] = None) -> Actions:
        """
        释放鼠标右键
        
        :param on_ele: 释放位置的元素或坐标，None 表示在当前位置释放
        :return: 返回自身，支持链式调用
        """
        ...

    def m_hold(self, on_ele: Union[ChromiumElement, str] = None) -> Actions:
        """
        按住鼠标中键
        
        :param on_ele: 要按住的元素或坐标，None 表示在当前位置按住
        :return: 返回自身，支持链式调用
        """
        ...

    def m_release(self, on_ele: Union[ChromiumElement, str] = None) -> Actions:
        """
        释放鼠标中键
        
        :param on_ele: 释放位置的元素或坐标，None 表示在当前位置释放
        :return: 返回自身，支持链式调用
        """
        ...

    def _hold(self,
              on_ele: Union[ChromiumElement, str] = None,
              button: str = 'left',
              count: int = 1) -> Actions:
        """
        内部方法：按下鼠标按键
        
        :param on_ele: 要按住的元素或坐标，None 表示在当前位置按住
        :param button: 按键类型，'left'、'right' 或 'middle'
        :param count: 点击次数，用于实现双击、三击等
        :return: 返回自身，支持链式调用
        """
        ...

    def _release(self, button: str) -> Actions:
        """
        内部方法：释放鼠标按键
        
        :param button: 按键类型，'left'、'right' 或 'middle'
        :return: 返回自身，支持链式调用
        """
        ...

    def scroll(self, delta_y: int = 0, delta_x: int = 0,
               on_ele: Union[ChromiumElement, str] = None) -> Actions:
        """
        在当前位置或指定元素上执行滚轮操作
        
        :param delta_y: 垂直滚动量，正值向下滚动，负值向上滚动
        :param delta_x: 水平滚动量，正值向右滚动，负值向左滚动
        :param on_ele: 要滚动的元素或坐标，None 表示在当前位置滚动
        :return: 返回自身，支持链式调用
        """
        ...

    def up(self, pixel: int) -> Actions:
        """
        向上移动鼠标
        
        :param pixel: 移动的像素数
        :return: 返回自身，支持链式调用
        """
        ...

    def down(self, pixel: int) -> Actions:
        """
        向下移动鼠标
        
        :param pixel: 移动的像素数
        :return: 返回自身，支持链式调用
        """
        ...

    def left(self, pixel: int) -> Actions:
        """
        向左移动鼠标
        
        :param pixel: 移动的像素数
        :return: 返回自身，支持链式调用
        """
        ...

    def right(self, pixel: int) -> Actions:
        """
        向右移动鼠标
        
        :param pixel: 移动的像素数
        :return: 返回自身，支持链式调用
        """
        ...

    def key_down(self, key: Union[KEYS, str]) -> Actions:
        """
        按下键盘按键（不释放）
        
        该方法用于模拟按住某个键，常用于组合键操作。
        例如：key_down('ctrl').key_down('c').key_up('c').key_up('ctrl')
        
        :param key: 按键名称，可以是：
            - Keys 类中的常量名（如 'ENTER'、'TAB'）
            - 字符（如 'a'、'1'）
            - 修饰键（ALT、CTRL、META/COMMAND、SHIFT）
        :return: 返回自身，支持链式调用
        
        注意：
            修饰键（Alt、Ctrl、Command、Shift）会被记录到 modifier 状态中，
            影响后续的鼠标和键盘事件。
        """
        ...

    def key_up(self, key: Union[KEYS, str]) -> Actions:
        """
        释放键盘按键
        
        该方法用于释放之前按下的按键。
        
        :param key: 按键名称，可以是：
            - Keys 类中的常量名（如 'ENTER'、'TAB'）
            - 字符（如 'a'、'1'）
            - 修饰键（ALT、CTRL、META/COMMAND、SHIFT）
        :return: 返回自身，支持链式调用
        
        注意：
            修饰键（Alt、Ctrl、Command、Shift）释放时会从 modifier 状态中移除。
        """
        ...

    def type(self,
             keys: Union[KEYS, str, list, tuple],
             interval: float = 0) -> Actions:
        """
        逐个输入键盘按键
        
        该方法会模拟真实的打字过程，依次按下并释放每个按键。
        支持输入普通字符、特殊按键和修饰键组合。
        
        :param keys: 要输入的内容，可以是：
            - 字符串：普通文本或包含特殊按键的字符串
            - 列表/元组：多个按键的序列
            - 数字：会转换为字符串
        :param interval: 每个按键之间的间隔时间（秒），默认为 0
        :return: 返回自身，支持链式调用
        
        注意：
            - 修饰键（Alt、Ctrl、Command、Shift）会在输入过程中保持按下状态，
              在所有字符输入完成后统一释放
            - 特殊按键使用 Unicode 私有区域编码（\ue009 等）
        """
        ...

    def input(self, text: Any) -> Actions:
        """
        快速输入文本
        
        该方法不模拟按键过程，直接将文本插入到当前焦点元素中，速度更快。
        适用于需要快速输入大量文本的场景。
        
        :param text: 要输入的文本内容
        :return: 返回自身，支持链式调用
        
        注意：
            - 该方法不会触发 keydown/keyup 事件
            - 对于需要按键事件的场景，应使用 type() 方法
        """
        ...

    def drag_in(self, ele_or_loc: Union[str, ChromiumElement], files: Union[str, list, tuple] = None,
                text: str = None, title: str = None, baseURL: str = None) -> Actions:
        """
        将文件或文本拖放到指定元素
        
        该方法模拟拖放操作，可以用于：
        - 上传文件（通过拖放文件到上传区域）
        - 拖放文本到可编辑区域
        - 拖放链接
        
        :param ele_or_loc: 目标元素或坐标
        :param files: 要拖放的文件路径，可以是单个路径字符串或路径列表
        :param text: 要拖放的文本内容
        :param title: 文本的标题（用于 URI 列表）
        :param baseURL: 文本的基础 URL（用于 URI 列表）
        :return: 返回自身，支持链式调用
        
        注意：
            - files 和 text 参数互斥，只能提供其中一个
            - 拖放文件时，dragOperationsMask=16 表示复制操作
            - 拖放文本时，dragOperationsMask=1 表示移动操作
        """
        ...

    def wait(self, second: float, scope: float = None) -> Actions:
        """
        等待指定时间
        
        :param second: 等待的秒数
        :param scope: 等待的作用域（传递给页面的 wait 方法）
        :return: 返回自身，支持链式调用
        """
        ...

    def open_chrome_menu(self) -> Actions:
        """
        打开 Chrome 浏览器菜单
        
        使用快捷键 Alt+F 打开 Chrome 的三点菜单（汉堡菜单）。
        这是 Chrome 在 Windows/Linux 上的标准快捷键。
        
        :return: 返回自身，支持链式调用
        
        注意：
            macOS 上的 Chrome 没有打开三点菜单的键盘快捷键，
            此方法在 macOS 上可能无法工作。
        """
        ...

    def open_chrome_menu_windows(self) -> Actions:
        """
        在 Windows 上打开 Chrome 菜单
        
        使用快捷键 Alt+F 打开 Chrome 的三点菜单（汉堡菜单）。
        这是 Chrome 在 Windows 上的标准快捷键。
        
        :return: 返回自身，支持链式调用
        """
        ...


def location_to_client(page: ChromiumBase, lx: int, ly: int) -> tuple:
    """
    将页面坐标转换为视口坐标
    
    页面坐标是相对于整个文档的绝对位置（包括滚动区域），
    视口坐标是相对于浏览器可见区域的位置（不包括滚动的部分）。
    
    :param page: 页面对象
    :param lx: 页面 x 坐标
    :param ly: 页面 y 坐标
    :return: (视口 x 坐标, 视口 y 坐标) 元组
    
    算法：
        视口坐标 = 页面坐标 - 滚动偏移量
    """
    ...
