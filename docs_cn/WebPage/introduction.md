🌏 WebPage 介绍
---

## 📚 什么是 WebPage？

WebPage 是 DrissionPage 中的混合模式页面对象，它结合了 ChromiumPage（浏览器模式）和 SessionPage（请求模式）的优势。

WebPage 可以在两种模式间自由切换，让您既能享受浏览器自动化的便利性，又能获得 HTTP 请求的高效率。

---

## 🎯 主要特性

### 1. 模式切换
- 可以在浏览器模式和请求模式间自由切换
- 自动同步 Cookies 和会话状态
- 无缝切换，无需重新初始化

### 2. 智能选择
- 根据操作类型自动选择最佳模式
- 浏览器模式处理复杂交互
- 请求模式处理简单数据获取

### 3. 功能完整
- 拥有两种模式的所有功能
- 支持文件上传下载
- 支持截图录制
- 支持网络监听

### 4. 使用简单
- 统一的 API 接口
- 自动处理模式切换
- 减少代码复杂度

---

## 🚀 基本用法

### 创建页面对象

```python
from DrissionPage import WebPage

# 创建页面对象（默认浏览器模式）
page = WebPage()

# 访问网页
page.get('https://www.example.com')

# 关闭浏览器
page.quit()
```

### 指定初始模式

```python
# 创建页面对象并指定初始模式
page = WebPage(mode='s')  # 请求模式
page.get('https://www.example.com')

# 或者
page = WebPage(mode='d')  # 浏览器模式
page.get('https://www.example.com')
```

---

## 🔄 模式切换

### 手动切换

```python
# 切换到浏览器模式
page.change_mode('d')

# 切换到请求模式
page.change_mode('s')

# 切换模式并同步 Cookies
page.change_mode('d', copy_cookies=True)
```

### 自动切换

```python
# WebPage 会根据操作类型自动选择模式
page.get('https://www.example.com')  # 使用当前模式

# 浏览器模式操作
page.ele('#button').click()  # 自动使用浏览器模式

# 请求模式操作
page.post('https://api.example.com/data', json={'key': 'value'})  # 自动使用请求模式
```

### 检查当前模式

```python
# 检查当前模式
current_mode = page.mode
print(f"当前模式: {current_mode}")

# 检查是否为浏览器模式
if page.mode == 'd':
    print("当前是浏览器模式")
else:
    print("当前是请求模式")
```

---

## 🍪 Cookies 同步

### 自动同步

```python
# WebPage 会自动同步 Cookies
page.get('https://www.example.com')

# 在浏览器模式中登录
page.change_mode('d')
page.ele('#username').input('admin')
page.ele('#password').input('123456')
page.ele('#login').click()

# 切换到请求模式，Cookies 自动同步
page.change_mode('s')
page.get('https://www.example.com/profile')  # 自动携带登录状态
```

### 手动同步

```python
# 从浏览器同步 Cookies 到请求模式
page.cookies_to_session()

# 从请求模式同步 Cookies 到浏览器
page.cookies_to_browser()

# 同步特定域名的 Cookies
page.cookies_to_session('example.com')
page.cookies_to_browser('example.com')
```

### 同步用户代理

```python
# 同步用户代理
page.cookies_to_session(copy_user_agent=True)
```

---

## 🌐 HTTP 请求

### GET 请求

```python
# 基本 GET 请求
page.get('https://www.example.com')

# 带参数的 GET 请求
page.get('https://www.example.com/search', 
         params={'q': 'Python', 'limit': 10})

# 带请求头的 GET 请求
page.get('https://www.example.com', 
         headers={'Authorization': 'Bearer token'})
```

### POST 请求

```python
# 发送 JSON 数据
page.post('https://api.example.com/data', 
          json={'name': 'John', 'age': 30})

# 发送表单数据
page.post('https://www.example.com/login', 
          data={'username': 'admin', 'password': '123456'})

# 发送文件
page.post('https://www.example.com/upload', 
          files={'file': open('test.txt', 'rb')})
```

### 其他 HTTP 方法

```python
# PUT 请求
page.put('https://api.example.com/user/1', 
         json={'name': 'John Updated'})

# DELETE 请求
page.delete('https://api.example.com/user/1')

# PATCH 请求
page.patch('https://api.example.com/user/1', 
           json={'name': 'John Patched'})
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

# 创建页面对象
page = WebPage(chromium_options=options)
```

### 会话配置

```python
from DrissionPage import SessionOptions

options = SessionOptions()

# 设置请求头
options.set_headers({'User-Agent': 'Custom Browser'})

# 设置代理
options.set_proxy('http://proxy.example.com:8080')

# 创建页面对象
page = WebPage(session_or_options=options)
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

### 1. 模式选择

```python
# 好的做法：根据操作类型选择模式
page.get('https://www.example.com')

# 简单数据获取使用请求模式
page.change_mode('s')
data = page.ele('#content').text

# 复杂交互使用浏览器模式
page.change_mode('d')
page.ele('#button').click()
```

### 2. Cookies 同步

```python
# 好的做法：及时同步 Cookies
page.change_mode('d')
page.ele('#login').click()
page.wait.url_change('dashboard')

# 同步 Cookies 到请求模式
page.cookies_to_session()
page.change_mode('s')
page.get('https://www.example.com/profile')
```

### 3. 资源管理

```python
# 好的做法：确保关闭浏览器
page = WebPage()
try:
    page.get('https://www.example.com')
    # 执行操作
finally:
    page.quit()
```

### 4. 性能优化

```python
# 好的做法：合理使用模式
# 批量数据获取使用请求模式
page.change_mode('s')
for url in urls:
    page.get(url)
    print(page.title)

# 复杂交互使用浏览器模式
page.change_mode('d')
page.ele('#complex-button').click()
```

---

## 🎯 常见问题

### Q1: 什么时候使用哪种模式？

**A:** 建议：
- **请求模式**：简单数据获取、API 调用、批量处理
- **浏览器模式**：复杂交互、JavaScript 处理、用户操作
- **混合模式**：需要两种功能的场景

### Q2: 模式切换会影响性能吗？

**A:** 模式切换本身很快，但：
- 频繁切换可能影响性能
- 建议批量操作时保持同一模式
- 合理规划操作顺序

### Q3: 如何处理模式切换失败？

**A:** 处理建议：
- 检查网络连接
- 确认浏览器状态
- 使用异常处理
- 必要时重新初始化

---

## 📖 下一步

现在您已经了解了 WebPage 的基本用法，可以：

1. [学习模式切换](mode_switch.md)
2. [了解独有功能](webpage_function.md)
3. [掌握配置选项](create_page_object.md)
4. [学习高级功能](advance/)

祝您使用愉快！🎉
