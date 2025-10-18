🌏 SessionPage 介绍
---

## 📚 什么是 SessionPage？

SessionPage 是 DrissionPage 中的请求模式页面对象，它基于 Python 的 `requests` 库实现，用于发送 HTTP 请求和处理响应数据。

与浏览器模式不同，SessionPage 不启动浏览器，而是直接发送 HTTP 请求，具有更高的性能和更低的资源消耗。

---

## 🎯 主要特性

### 1. 高性能
- 不启动浏览器，启动速度快
- 内存占用少
- 网络请求效率高

### 2. 简单易用
- 语法简洁，易于理解
- 自动处理 Cookies 和会话
- 内置 HTML 解析功能

### 3. 功能丰富
- 支持各种 HTTP 方法
- 自动处理重定向
- 支持文件上传下载
- 内置 lxml 解析引擎

### 4. 无头操作
- 不需要图形界面
- 适合服务器环境
- 可以批量处理请求

---

## 🚀 基本用法

### 创建页面对象

```python
from DrissionPage import SessionPage

# 创建页面对象
page = SessionPage()

# 发送 GET 请求
page.get('https://www.example.com')

# 获取页面标题
print(page.title)
```

### 配置会话

```python
from DrissionPage import SessionOptions, SessionPage

# 创建配置对象
options = SessionOptions()

# 设置请求头
options.set_headers({'User-Agent': 'Custom Browser'})

# 设置代理
options.set_proxy('http://proxy.example.com:8080')

# 设置超时时间
options.set_timeout(30)

# 创建页面对象
page = SessionPage(options)
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

# 带超时的 GET 请求
page.get('https://www.example.com', timeout=30)
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

# 发送原始数据
page.post('https://www.example.com/data', 
          data='raw data content')
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

# HEAD 请求
page.head('https://www.example.com')

# OPTIONS 请求
page.options('https://www.example.com')
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

### 元素信息

```python
# 获取元素文本
text = page.ele('#title').text

# 获取元素 HTML
html = page.ele('#content').html

# 获取元素属性
href = page.ele('a').attr('href')
src = page.ele('img').attr('src')

# 获取元素标签名
tag = page.ele('#button').tag
```

### 查找多个元素

```python
# 查找所有匹配的元素
elements = page.eles('.item')

# 遍历元素
for element in elements:
    print(element.text)

# 获取元素数量
count = len(elements)
print(f"找到 {count} 个元素")
```

---

## 🍪 Cookies 管理

### 自动处理

```python
# SessionPage 自动处理 Cookies
page.get('https://www.example.com/login')
page.post('https://www.example.com/login', 
          data={'username': 'admin', 'password': '123456'})

# 后续请求会自动携带 Cookies
page.get('https://www.example.com/profile')
```

### 手动设置

```python
# 设置 Cookies
page.set.cookies({'session_id': 'abc123', 'user_id': '456'})

# 获取 Cookies
cookies = page.cookies
print(f"当前 Cookies: {cookies}")

# 清除 Cookies
page.clear.cookies()
```

### 从浏览器导入

```python
# 从浏览器导入 Cookies
page.cookies_to_session()

# 导入特定域名的 Cookies
page.cookies_to_session('example.com')
```

---

## 📁 文件操作

### 文件上传

```python
# 上传单个文件
page.post('https://www.example.com/upload', 
          files={'file': open('test.txt', 'rb')})

# 上传多个文件
page.post('https://www.example.com/upload', 
          files={'file1': open('test1.txt', 'rb'),
                 'file2': open('test2.txt', 'rb')})

# 上传文件并设置文件名
page.post('https://www.example.com/upload', 
          files={'file': ('custom_name.txt', open('test.txt', 'rb'))})
```

### 文件下载

```python
# 下载文件
response = page.get('https://www.example.com/file.pdf')

# 保存文件
with open('downloaded_file.pdf', 'wb') as f:
    f.write(response.content)

# 下载大文件
response = page.get('https://www.example.com/large_file.zip', stream=True)
with open('large_file.zip', 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)
```

---

## 🔧 高级功能

### 重试机制

```python
# 设置重试次数和间隔
page.get('https://www.example.com', retry=3, interval=1)

# 自定义重试条件
def should_retry(response):
    return response.status_code >= 500

page.get('https://www.example.com', retry=3, interval=1, 
         retry_condition=should_retry)
```

### 请求拦截

```python
# 拦截请求
def interceptor(request):
    print(f"请求 URL: {request.url}")
    print(f"请求方法: {request.method}")
    return request

page.set.request_interceptor(interceptor)
page.get('https://www.example.com')
```

### 响应处理

```python
# 处理响应
def response_handler(response):
    print(f"响应状态: {response.status_code}")
    print(f"响应头: {response.headers}")
    return response

page.set.response_handler(response_handler)
page.get('https://www.example.com')
```

---

## ⏰ 超时设置

### 全局超时

```python
# 设置全局超时时间
page.set.timeout(30)

# 获取当前超时设置
timeout = page.timeout
print(f"当前超时: {timeout} 秒")
```

### 请求超时

```python
# 为特定请求设置超时
page.get('https://www.example.com', timeout=60)

# 设置连接超时和读取超时
page.get('https://www.example.com', timeout=(10, 30))
```

---

## 🌐 代理设置

### HTTP 代理

```python
# 设置 HTTP 代理
page.set.proxy('http://proxy.example.com:8080')

# 设置带认证的代理
page.set.proxy('http://username:password@proxy.example.com:8080')
```

### SOCKS 代理

```python
# 设置 SOCKS 代理
page.set.proxy('socks5://proxy.example.com:1080')

# 设置带认证的 SOCKS 代理
page.set.proxy('socks5://username:password@proxy.example.com:1080')
```

---

## 🔍 响应处理

### 响应信息

```python
# 获取响应状态码
status_code = page.response.status_code
print(f"状态码: {status_code}")

# 获取响应头
headers = page.response.headers
print(f"响应头: {headers}")

# 获取响应内容
content = page.response.content
text = page.response.text
```

### 响应解析

```python
# 解析 JSON 响应
json_data = page.response.json()
print(f"JSON 数据: {json_data}")

# 解析 XML 响应
xml_data = page.response.xml()
print(f"XML 数据: {xml_data}")

# 解析 HTML 响应
html_data = page.response.html()
print(f"HTML 数据: {html_data}")
```

---

## 🚨 错误处理

### 常见错误

```python
from DrissionPage.errors import RequestError, TimeoutError

try:
    page.get('https://www.example.com')
except RequestError as e:
    print(f"请求错误: {e}")
except TimeoutError as e:
    print(f"超时错误: {e}")
except Exception as e:
    print(f"其他错误: {e}")
```

### 错误处理最佳实践

```python
# 检查响应状态
response = page.get('https://www.example.com')
if response.status_code == 200:
    print("请求成功")
else:
    print(f"请求失败，状态码: {response.status_code}")

# 使用重试机制
try:
    page.get('https://www.example.com', retry=3, interval=1)
except Exception as e:
    print(f"重试后仍然失败: {e}")
```

---

## 💡 最佳实践

### 1. 会话管理

```python
# 好的做法：复用会话
page = SessionPage()
page.get('https://www.example.com/login')
page.post('https://www.example.com/login', data={'username': 'admin'})
page.get('https://www.example.com/profile')  # 自动携带 Cookies

# 避免：每次创建新会话
page1 = SessionPage()
page1.get('https://www.example.com/login')
page2 = SessionPage()  # 新会话，丢失 Cookies
page2.get('https://www.example.com/profile')
```

### 2. 异常处理

```python
# 好的做法：异常处理
try:
    page.get('https://www.example.com')
    data = page.ele('#content').text
except Exception as e:
    print(f"获取数据失败: {e}")
    data = None
```

### 3. 性能优化

```python
# 好的做法：批量操作
urls = ['https://www.example.com/page1', 'https://www.example.com/page2']
for url in urls:
    page.get(url)
    print(page.title)

# 避免：重复创建页面对象
for url in urls:
    page = SessionPage()  # 每次都创建新对象
    page.get(url)
    print(page.title)
```

### 4. 资源管理

```python
# 好的做法：及时关闭连接
page = SessionPage()
try:
    page.get('https://www.example.com')
    # 执行操作
finally:
    page.close()  # 关闭连接
```

---

## 🎯 常见问题

### Q1: 如何处理 JavaScript 渲染的内容？

**A:** SessionPage 无法处理 JavaScript，建议：
- 使用 ChromiumPage 处理动态内容
- 或者使用 WebPage 混合模式
- 分析网络请求，直接调用 API

### Q2: 如何处理验证码？

**A:** 对于验证码：
- 使用 ChromiumPage 手动处理
- 集成第三方验证码识别服务
- 使用 WebPage 混合模式

### Q3: 如何提高请求速度？

**A:** 优化建议：
- 使用连接池
- 启用 HTTP/2
- 合理设置超时时间
- 使用异步请求

---

## 📖 下一步

现在您已经了解了 SessionPage 的基本用法，可以：

1. [学习页面操作](visit_web_page.md)
2. [了解元素操作](get_elements.md)
3. [掌握配置选项](session_options.md)
4. [学习高级功能](set_session.md)

祝您使用愉快！🎉
