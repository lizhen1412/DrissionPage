🌏 Gitee 登录自动化示例
---

## 📚 示例介绍

本示例演示如何使用 DrissionPage 自动化登录 Gitee 网站，包括：

- 打开登录页面
- 输入用户名和密码
- 处理验证码（如果需要）
- 点击登录按钮
- 验证登录结果

---

## 🚀 完整代码

```python
from DrissionPage import ChromiumPage
from DrissionPage.errors import ElementNotFoundError, WaitTimeoutError
import time

def login_gitee(username, password):
    """
    自动化登录 Gitee
    
    Args:
        username (str): 用户名
        password (str): 密码
    
    Returns:
        bool: 登录是否成功
    """
    page = ChromiumPage()
    
    try:
        # 访问 Gitee 登录页面
        print("正在访问 Gitee 登录页面...")
        page.get('https://gitee.com/login')
        
        # 等待页面加载完成
        page.wait.ele_displayed('#user_login')
        
        # 输入用户名
        print("正在输入用户名...")
        username_input = page.ele('#user_login')
        username_input.clear()
        username_input.input(username)
        
        # 输入密码
        print("正在输入密码...")
        password_input = page.ele('#user_password')
        password_input.clear()
        password_input.input(password)
        
        # 检查是否需要验证码
        captcha_element = page.ele('#captcha', timeout=2)
        if captcha_element:
            print("检测到验证码，请手动输入...")
            # 等待用户手动输入验证码
            input("请在浏览器中输入验证码，然后按回车键继续...")
        
        # 点击登录按钮
        print("正在点击登录按钮...")
        login_button = page.ele('input[type="submit"]')
        login_button.click()
        
        # 等待登录结果
        print("等待登录结果...")
        
        # 检查是否登录成功
        try:
            # 等待跳转到首页或用户页面
            page.wait.url_change('gitee.com', timeout=10)
            
            # 检查是否还在登录页面
            if 'login' in page.url:
                print("登录失败：仍在登录页面")
                return False
            
            # 检查是否有错误信息
            error_element = page.ele('.error-message', timeout=2)
            if error_element:
                error_text = error_element.text
                print(f"登录失败：{error_text}")
                return False
            
            # 检查是否有用户头像或用户名
            user_element = page.ele('.user-avatar', timeout=5)
            if user_element:
                print("登录成功！")
                return True
            else:
                print("登录状态不明确")
                return False
                
        except WaitTimeoutError:
            print("登录超时")
            return False
            
    except ElementNotFoundError as e:
        print(f"元素未找到：{e}")
        return False
    except Exception as e:
        print(f"登录过程中发生错误：{e}")
        return False
    finally:
        # 关闭浏览器
        page.quit()

def main():
    """主函数"""
    print("=== Gitee 登录自动化示例 ===")
    
    # 获取用户输入
    username = input("请输入用户名：")
    password = input("请输入密码：")
    
    # 执行登录
    success = login_gitee(username, password)
    
    if success:
        print("登录成功！")
    else:
        print("登录失败！")

if __name__ == "__main__":
    main()
```

---

## 🎯 代码解析

### 1. 导入模块

```python
from DrissionPage import ChromiumPage
from DrissionPage.errors import ElementNotFoundError, WaitTimeoutError
import time
```

- `ChromiumPage`: 浏览器模式页面对象
- `ElementNotFoundError`: 元素未找到异常
- `WaitTimeoutError`: 等待超时异常

### 2. 创建页面对象

```python
page = ChromiumPage()
```

创建浏览器页面对象，用于控制浏览器。

### 3. 访问登录页面

```python
page.get('https://gitee.com/login')
page.wait.ele_displayed('#user_login')
```

访问 Gitee 登录页面并等待用户名输入框出现。

### 4. 输入用户名和密码

```python
# 输入用户名
username_input = page.ele('#user_login')
username_input.clear()
username_input.input(username)

# 输入密码
password_input = page.ele('#user_password')
password_input.clear()
password_input.input(password)
```

查找用户名和密码输入框，清空后输入相应内容。

### 5. 处理验证码

```python
# 检查是否需要验证码
captcha_element = page.ele('#captcha', timeout=2)
if captcha_element:
    print("检测到验证码，请手动输入...")
    input("请在浏览器中输入验证码，然后按回车键继续...")
```

检查是否存在验证码，如果存在则等待用户手动输入。

### 6. 点击登录按钮

```python
login_button = page.ele('input[type="submit"]')
login_button.click()
```

查找并点击登录按钮。

### 7. 验证登录结果

```python
# 等待跳转到首页或用户页面
page.wait.url_change('gitee.com', timeout=10)

# 检查是否还在登录页面
if 'login' in page.url:
    print("登录失败：仍在登录页面")
    return False

# 检查是否有错误信息
error_element = page.ele('.error-message', timeout=2)
if error_element:
    error_text = error_element.text
    print(f"登录失败：{error_text}")
    return False

# 检查是否有用户头像或用户名
user_element = page.ele('.user-avatar', timeout=5)
if user_element:
    print("登录成功！")
    return True
```

通过多种方式验证登录是否成功。

---

## 🔧 高级功能

### 1. 无头模式

```python
from DrissionPage import ChromiumOptions

# 创建配置对象
options = ChromiumOptions()
options.headless(True)  # 启用无头模式

# 创建页面对象
page = ChromiumPage(options)
```

### 2. 自定义超时

```python
# 设置页面加载超时
page.set.timeouts(page_load=60)

# 设置元素查找超时
page.set.timeouts(base=20)
```

### 3. 截图调试

```python
# 保存登录页面截图
page.get_screenshot('login_page.png')

# 保存登录后页面截图
page.get_screenshot('after_login.png')
```

### 4. 网络监听

```python
# 开始监听网络请求
page.listen.start()

# 执行登录操作
page.ele('#user_login').input(username)
page.ele('#user_password').input(password)
page.ele('input[type="submit"]').click()

# 获取监听到的请求
requests = page.listen.wait()
for req in requests:
    print(f"请求URL: {req.url}")
    print(f"请求方法: {req.method}")
```

---

## 🚨 错误处理

### 1. 元素未找到

```python
try:
    username_input = page.ele('#user_login')
    username_input.input(username)
except ElementNotFoundError:
    print("用户名输入框未找到")
    return False
```

### 2. 等待超时

```python
try:
    page.wait.ele_displayed('#user_login', timeout=10)
except WaitTimeoutError:
    print("页面加载超时")
    return False
```

### 3. 网络错误

```python
try:
    page.get('https://gitee.com/login')
except Exception as e:
    print(f"网络错误: {e}")
    return False
```

---

## 💡 最佳实践

### 1. 资源管理

```python
# 好的做法：确保关闭浏览器
page = ChromiumPage()
try:
    # 执行登录操作
    success = login_gitee(username, password)
finally:
    page.quit()
```

### 2. 异常处理

```python
# 好的做法：完整的异常处理
try:
    page.get('https://gitee.com/login')
    page.wait.ele_displayed('#user_login')
    # 执行其他操作
except ElementNotFoundError:
    print("页面元素未找到")
except WaitTimeoutError:
    print("页面加载超时")
except Exception as e:
    print(f"其他错误: {e}")
```

### 3. 等待机制

```python
# 好的做法：使用智能等待
page.wait.ele_displayed('#user_login')
page.wait.ele_clickable('input[type="submit"]')

# 避免：固定等待时间
time.sleep(5)  # 不推荐
```

### 4. 元素定位

```python
# 好的做法：使用稳定的选择器
username_input = page.ele('#user_login')  # ID 选择器
login_button = page.ele('input[type="submit"]')  # 属性选择器

# 避免：使用不稳定的选择器
username_input = page.ele('text:用户名')  # 文本可能变化
```

---

## 🎯 扩展功能

### 1. 记住登录状态

```python
def save_login_state(page):
    """保存登录状态"""
    cookies = page.cookies
    with open('gitee_cookies.json', 'w') as f:
        json.dump(cookies, f)

def load_login_state(page):
    """加载登录状态"""
    try:
        with open('gitee_cookies.json', 'r') as f:
            cookies = json.load(f)
        page.set.cookies(cookies)
        return True
    except FileNotFoundError:
        return False
```

### 2. 多账号登录

```python
def login_multiple_accounts(accounts):
    """多账号登录"""
    results = {}
    
    for account in accounts:
        username = account['username']
        password = account['password']
        
        print(f"正在登录账号: {username}")
        success = login_gitee(username, password)
        results[username] = success
        
        if success:
            print(f"账号 {username} 登录成功")
        else:
            print(f"账号 {username} 登录失败")
    
    return results
```

### 3. 登录状态检查

```python
def check_login_status(page):
    """检查登录状态"""
    try:
        # 访问需要登录的页面
        page.get('https://gitee.com/profile')
        
        # 检查是否跳转到登录页面
        if 'login' in page.url:
            return False
        
        # 检查是否有用户信息
        user_element = page.ele('.user-avatar')
        return user_element is not None
        
    except Exception:
        return False
```

---

## 🎯 常见问题

### Q1: 登录失败怎么办？

**A:** 请检查：
- 用户名和密码是否正确
- 网络连接是否正常
- 是否需要验证码
- 页面元素是否发生变化

### Q2: 如何处理验证码？

**A:** 验证码处理方式：
- 手动输入（推荐）
- 使用第三方验证码识别服务
- 联系网站管理员获取测试账号

### Q3: 如何提高登录成功率？

**A:** 优化建议：
- 使用稳定的元素选择器
- 合理设置等待时间
- 处理各种异常情况
- 添加重试机制

---

## 📖 总结

本示例演示了如何使用 DrissionPage 自动化登录 Gitee 网站，包括：

1. **基本流程**：访问页面 → 输入信息 → 点击登录 → 验证结果
2. **错误处理**：异常捕获和错误提示
3. **等待机制**：智能等待页面加载和元素出现
4. **最佳实践**：资源管理、异常处理、元素定位

您可以根据实际需求修改和扩展这个示例，比如：
- 添加更多错误处理
- 支持更多登录方式
- 集成验证码识别
- 添加登录状态保存

祝您使用愉快！🎉
