🌏 ChromiumPage 介绍
---

## 📚 什么是 ChromiumPage？

ChromiumPage 是 DrissionPage 中的浏览器模式页面对象，它基于 Chrome DevTools Protocol (CDP) 实现，可以直接控制浏览器进行各种操作。

与传统的 WebDriver 方式不同，ChromiumPage 不依赖浏览器驱动，而是通过 WebSocket 与浏览器通信，具有更高的性能和更丰富的功能。

---

## 🎯 主要特性

### 1. 无需驱动
- 不需要下载和配置浏览器驱动
- 自动适配不同版本的 Chrome/Edge 浏览器
- 减少了配置和维护的复杂性

### 2. 高性能
- 基于 CDP 协议，通信效率高
- 支持并发操作多个标签页
- 内存占用相对较少

### 3. 功能丰富
- 支持完整的浏览器操作
- 可以处理 JavaScript 动态内容
- 支持文件上传下载、截图录制等高级功能

### 4. 跨 iframe 操作
- 可以直接在 iframe 中查找元素
- 无需手动切换 iframe
- 逻辑更清晰，操作更简单

---

## 🚀 基本用法

### 创建页面对象

```python
from DrissionPage import ChromiumPage

# 创建页面对象
page = ChromiumPage()

# 访问网页
page.get('https://www.example.com')

# 关闭浏览器
page.quit()
```

### 配置浏览器

```python
from DrissionPage import ChromiumOptions, ChromiumPage

# 创建配置对象
options = ChromiumOptions()

# 设置浏览器路径
options.set_browser_path('C:/Program Files/Google/Chrome/Application/chrome.exe')

# 设置无头模式
options.headless(True)

# 设置代理
options.set_proxy('http://proxy.example.com:8080')

# 创建页面对象
page = ChromiumPage(options)
```

---

## 🎭 页面操作

### 访问网页

```python
# 访问网页
page.get('https://www.example.com')

# 访问网页并等待加载完成
page.get('https://www.example.com', timeout=30)

# 刷新页面
page.refresh()

# 后退
page.back()

# 前进
page.forward()
```

### 页面信息

```python
# 获取当前 URL
current_url = page.url
print(f"当前 URL: {current_url}")

# 获取页面标题
title = page.title
print(f"页面标题: {title}")

# 获取页面 HTML
html = page.html
print(f"页面 HTML: {html}")

# 获取页面文本
text = page.text
print(f"页面文本: {text}")
```

---

## 🔍 元素操作

### 查找元素

```python
# 通过 ID 查找
element = page.ele('#username')

# 通过 class 查找
element = page.ele('.btn-primary')

# 通过标签查找
element = page.ele('tag:div')

# 通过文本查找
element = page.ele('text:登录')

# 通过属性查找
element = page.ele('@name=username')
```

### 元素交互

```python
# 输入文本
page.ele('#username').input('admin')

# 点击元素
page.ele('#login-btn').click()

# 清空内容
page.ele('#username').clear()

# 获取文本
text = page.ele('#title').text

# 获取属性
href = page.ele('a').attr('href')
```

### 高级操作

```python
# 悬停
page.ele('#menu').hover()

# 拖拽
page.ele('#draggable').drag(100, 100)

# 右键点击
page.ele('#button').click.right()

# 双击
page.ele('#button').click.multi(2)

# 执行 JavaScript
result = page.ele('#input').run_js('return this.value;')
```

---

## ⏰ 等待机制

### 页面等待

```python
# 等待页面加载完成
page.wait.doc_loaded()

# 等待 URL 变化
page.wait.url_change('success')

# 等待标题变化
page.wait.title_change('新标题')
```

### 元素等待

```python
# 等待元素出现
page.wait.ele_displayed('#loading')

# 等待元素消失
page.wait.ele_hidden('#loading')

# 等待元素可点击
page.wait.ele_clickable('#button')
```

### 自定义等待

```python
# 等待自定义条件
page.wait.until(lambda: page.ele('#status').text == '完成')

# 等待函数返回 True
def check_condition():
    return page.ele('#result').text != ''

page.wait.until(check_condition)
```

---

## 📁 文件操作

### 文件上传

```python
# 上传单个文件
page.ele('#file-input').upload('path/to/file.txt')

# 上传多个文件
page.ele('#file-input').upload(['file1.txt', 'file2.txt'])

# 上传并等待完成
page.ele('#file-input').upload('file.txt')
page.wait.ele_displayed('.upload-success')
```

### 文件下载

```python
# 点击下载链接
page.ele('#download-link').click.to_download('downloads/')

# 等待下载开始
page.wait.download_begin()

# 等待下载完成
page.wait.downloads_done()

# 获取下载的文件信息
downloads = page.downloads
for download in downloads:
    print(f"文件名: {download.name}")
    print(f"状态: {download.status}")
```

---

## 🎬 截图和录制

### 截图功能

```python
# 保存页面截图
page.get_screenshot('page.png')

# 保存元素截图
page.ele('#button').get_screenshot('button.png')

# 保存整个页面截图（包括视口外部分）
page.get_screenshot('full_page.png', full_page=True)
```

### 屏幕录制

```python
# 开始录制
page.start_recording('video.mp4')

# 执行操作
page.ele('#button').click()
page.ele('#input').input('Hello')

# 停止录制
page.stop_recording()
```

---

## 🎭 多标签页操作

### 标签页管理

```python
# 打开新标签页
new_tab = page.new_tab('https://www.google.com')

# 获取所有标签页
tabs = page.get_tabs()
print(f"当前有 {len(tabs)} 个标签页")

# 切换到指定标签页
page.activate_tab(1)

# 关闭标签页
new_tab.close()

# 关闭所有标签页
page.close_tabs()
```

### 标签页操作

```python
# 在新标签页中操作
new_tab = page.new_tab()
new_tab.get('https://www.example.com')
new_tab.ele('#search').input('Python')

# 切换回原标签页
page.activate_tab(0)
page.ele('#button').click()
```

---

## 🖼️ iframe 操作

### iframe 查找

```python
# 获取 iframe
iframe = page.get_frame('#iframe-id')

# 在 iframe 中查找元素
element = iframe.ele('#input')

# 在 iframe 中操作
iframe.ele('#input').input('Hello')
iframe.ele('#button').click()
```

### 跨 iframe 操作

```python
# 直接跨 iframe 查找元素
element = page.ele('#iframe-id #input')

# 跨 iframe 操作
page.ele('#iframe-id #input').input('Hello')
page.ele('#iframe-id #button').click()
```

---

## 🌐 网络监听

### 监听网络请求

```python
# 开始监听
page.listen.start()

# 执行操作触发请求
page.ele('#button').click()

# 获取监听到的请求
requests = page.listen.wait()
for req in requests:
    print(f"URL: {req.url}")
    print(f"方法: {req.method}")
    print(f"状态: {req.response.status_code}")
```

### 拦截网络请求

```python
# 拦截特定请求
page.listen.start()
page.listen.wait('https://api.example.com/data')

# 修改请求
page.listen.modify('https://api.example.com/data', 
                   {'method': 'POST', 'data': {'key': 'value'}})
```

---

## 🎨 动作链

### 复杂操作

```python
from DrissionPage import Actions

# 创建动作链
actions = Actions(page)

# 执行复杂操作
actions.move_to('#menu').click('#submenu').drag('#slider', 100, 0)

# 键盘操作
actions.type('Hello World').key('Enter')
```

### 鼠标操作

```python
# 鼠标移动
actions.move_to('#button')

# 鼠标点击
actions.click('#button')

# 鼠标拖拽
actions.drag('#draggable', 100, 100)

# 鼠标滚轮
actions.scroll(0, 100)
```

---

## 🔧 配置选项

### 浏览器配置

```python
from DrissionPage import ChromiumOptions

options = ChromiumOptions()

# 基本设置
options.set_browser_path('C:/Program Files/Google/Chrome/Application/chrome.exe')
options.headless(True)
options.set_proxy('http://proxy.example.com:8080')

# 高级设置
options.set_argument('--disable-web-security')
options.set_argument('--disable-features=VizDisplayCompositor')
options.set_pref('profile.default_content_settings.popups', 0)

# 创建页面对象
page = ChromiumPage(options)
```

### 超时设置

```python
# 设置各种超时时间
page.set.timeouts(base=10, page_load=30, script=30)

# 获取当前超时设置
timeouts = page.timeouts
print(f"基础超时: {timeouts.base}")
print(f"页面加载超时: {timeouts.page_load}")
print(f"脚本超时: {timeouts.script}")
```

---

## 🚨 错误处理

### 常见错误

```python
from DrissionPage.errors import ElementNotFoundError, WaitTimeoutError

try:
    page.get('https://www.example.com')
    page.ele('#button').click()
except ElementNotFoundError:
    print("元素未找到")
except WaitTimeoutError:
    print("等待超时")
except Exception as e:
    print(f"其他错误: {e}")
```

### 错误处理最佳实践

```python
# 检查元素是否存在
if page.ele('#button', timeout=0):
    page.ele('#button').click()
else:
    print("按钮不存在")

# 使用等待机制
if page.wait.ele_displayed('#loading', timeout=5):
    print("页面加载完成")
else:
    print("页面加载超时")
```

---

## 💡 最佳实践

### 1. 资源管理

```python
# 好的做法：确保关闭浏览器
page = ChromiumPage()
try:
    page.get('https://www.example.com')
    # 执行操作
finally:
    page.quit()
```

### 2. 合理使用等待

```python
# 好的做法：等待元素出现
page.wait.ele_displayed('#content')
content = page.ele('#content').text

# 避免：固定等待时间
import time
time.sleep(5)
```

### 3. 异常处理

```python
# 好的做法：异常处理
try:
    page.ele('#button').click()
except ElementNotFoundError:
    print("按钮未找到，跳过点击")
except Exception as e:
    print(f"其他错误: {e}")
```

### 4. 性能优化

```python
# 好的做法：批量操作
elements = page.eles('.item')
for element in elements:
    print(element.text)

# 避免：重复查找
for i in range(10):
    element = page.ele('.item')  # 每次都重新查找
    print(element.text)
```

---

## 🎯 常见问题

### Q1: 浏览器启动失败怎么办？

**A:** 请检查：
- 浏览器路径是否正确
- 是否有权限访问浏览器
- 端口是否被占用
- 防火墙是否阻止连接

### Q2: 元素操作失败怎么办？

**A:** 建议：
- 检查元素定位是否正确
- 等待元素加载完成
- 检查元素是否可见
- 使用等待机制

### Q3: 如何提高性能？

**A:** 优化建议：
- 使用无头模式
- 禁用图片加载
- 合理设置超时时间
- 避免不必要的等待

---

## 📖 下一步

现在您已经了解了 ChromiumPage 的基本用法，可以：

1. [学习页面操作](page_operation.md)
2. [了解元素操作](element_operation.md)
3. [掌握等待机制](waiting.md)
4. [学习高级功能](actions.md)

祝您使用愉快！🎉
