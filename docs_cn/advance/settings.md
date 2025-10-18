🌏 全局设置
---

## 📚 什么是全局设置？

全局设置是 DrissionPage 提供的系统级配置选项，可以影响整个库的行为和默认值。

通过全局设置，您可以自定义错误处理、超时时间、语言设置等，让 DrissionPage 更好地适应您的需求。

---

## 🎯 主要设置项

### 错误处理设置

```python
from DrissionPage import Settings

# 设置元素未找到时是否抛出异常
Settings.set_raise_when_ele_not_found(True)

# 设置等待超时时是否抛出异常
Settings.set_raise_when_timeout(True)

# 设置网络错误时是否抛出异常
Settings.set_raise_when_network_error(True)
```

### 超时设置

```python
# 设置 CDP 通信超时时间（秒）
Settings.set_cdp_timeout(30)

# 设置页面加载超时时间（秒）
Settings.set_page_load_timeout(60)

# 设置脚本执行超时时间（秒）
Settings.set_script_timeout(30)
```

### 语言设置

```python
# 设置错误信息语言
Settings.set_language('zh')  # 中文
Settings.set_language('en')  # 英文

# 获取当前语言设置
current_lang = Settings.get_language()
print(f"当前语言: {current_lang}")
```

---

## 🔧 详细配置

### 错误处理配置

```python
from DrissionPage import Settings

# 元素未找到时的行为
Settings.set_raise_when_ele_not_found(True)   # 抛出异常
Settings.set_raise_when_ele_not_found(False)  # 返回 None

# 等待超时时的行为
Settings.set_raise_when_timeout(True)   # 抛出异常
Settings.set_raise_when_timeout(False)  # 返回 False

# 网络错误时的行为
Settings.set_raise_when_network_error(True)   # 抛出异常
Settings.set_raise_when_network_error(False)  # 返回 None
```

### 超时配置

```python
# CDP 通信超时
Settings.set_cdp_timeout(30)  # 30 秒

# 页面加载超时
Settings.set_page_load_timeout(60)  # 60 秒

# 脚本执行超时
Settings.set_script_timeout(30)  # 30 秒

# 元素查找超时
Settings.set_ele_timeout(10)  # 10 秒
```

### 语言配置

```python
# 设置错误信息语言
Settings.set_language('zh')  # 中文错误信息
Settings.set_language('en')  # 英文错误信息

# 获取支持的语言列表
supported_langs = Settings.get_supported_languages()
print(f"支持的语言: {supported_langs}")
```

---

## 🎨 自定义设置

### 创建自定义设置

```python
from DrissionPage import Settings

# 自定义设置类
class CustomSettings(Settings):
    # 自定义超时时间
    custom_timeout = 45
    
    # 自定义重试次数
    custom_retry_count = 3
    
    # 自定义等待间隔
    custom_wait_interval = 2
    
    @classmethod
    def set_custom_timeout(cls, timeout):
        cls.custom_timeout = timeout
        return cls
    
    @classmethod
    def set_custom_retry_count(cls, count):
        cls.custom_retry_count = count
        return cls
    
    @classmethod
    def set_custom_wait_interval(cls, interval):
        cls.custom_wait_interval = interval
        return cls

# 使用自定义设置
CustomSettings.set_custom_timeout(60)
CustomSettings.set_custom_retry_count(5)
CustomSettings.set_custom_wait_interval(3)
```

### 应用自定义设置

```python
# 在页面对象中应用自定义设置
from DrissionPage import WebPage

page = WebPage()

# 应用自定义超时
page.set.timeout(CustomSettings.custom_timeout)

# 应用自定义重试
page.get('https://www.example.com', 
         retry=CustomSettings.custom_retry_count,
         interval=CustomSettings.custom_wait_interval)
```

---

## 🔍 设置查询

### 获取当前设置

```python
# 获取所有当前设置
current_settings = Settings.get_all_settings()
print(f"当前设置: {current_settings}")

# 获取特定设置
cdp_timeout = Settings.get_cdp_timeout()
print(f"CDP 超时: {cdp_timeout}")

ele_timeout = Settings.get_ele_timeout()
print(f"元素超时: {ele_timeout}")

language = Settings.get_language()
print(f"当前语言: {language}")
```

### 设置验证

```python
# 验证设置是否有效
def validate_settings():
    try:
        # 检查超时设置
        if Settings.get_cdp_timeout() <= 0:
            print("CDP 超时设置无效")
            return False
        
        # 检查语言设置
        if Settings.get_language() not in Settings.get_supported_languages():
            print("语言设置无效")
            return False
        
        print("所有设置有效")
        return True
    except Exception as e:
        print(f"设置验证失败: {e}")
        return False

# 执行验证
validate_settings()
```

---

## 🎯 设置应用

### 全局应用

```python
# 在程序开始时设置全局配置
from DrissionPage import Settings

# 设置全局错误处理
Settings.set_raise_when_ele_not_found(True)
Settings.set_raise_when_timeout(True)

# 设置全局超时
Settings.set_cdp_timeout(30)
Settings.set_page_load_timeout(60)
Settings.set_script_timeout(30)

# 设置语言
Settings.set_language('zh')

print("全局设置已应用")
```

### 局部应用

```python
# 在特定操作中临时修改设置
from DrissionPage import Settings, WebPage

# 保存原始设置
original_timeout = Settings.get_cdp_timeout()
original_raise = Settings.get_raise_when_ele_not_found()

try:
    # 临时修改设置
    Settings.set_cdp_timeout(60)
    Settings.set_raise_when_ele_not_found(False)
    
    # 执行操作
    page = WebPage()
    page.get('https://www.example.com')
    
finally:
    # 恢复原始设置
    Settings.set_cdp_timeout(original_timeout)
    Settings.set_raise_when_ele_not_found(original_raise)
```

---

## 🚨 错误处理

### 设置错误

```python
from DrissionPage.errors import SettingsError

try:
    # 尝试设置无效值
    Settings.set_cdp_timeout(-1)
except SettingsError as e:
    print(f"设置错误: {e}")
except Exception as e:
    print(f"其他错误: {e}")
```

### 设置恢复

```python
# 重置所有设置为默认值
Settings.reset_to_default()

# 重置特定设置
Settings.reset_cdp_timeout()
Settings.reset_language()
Settings.reset_raise_when_ele_not_found()
```

---

## 💡 最佳实践

### 1. 设置管理

```python
# 好的做法：集中管理设置
class AppSettings:
    @staticmethod
    def apply_production_settings():
        Settings.set_cdp_timeout(30)
        Settings.set_page_load_timeout(60)
        Settings.set_raise_when_ele_not_found(True)
        Settings.set_language('zh')
    
    @staticmethod
    def apply_development_settings():
        Settings.set_cdp_timeout(60)
        Settings.set_page_load_timeout(120)
        Settings.set_raise_when_ele_not_found(False)
        Settings.set_language('en')

# 根据环境应用设置
import os
if os.getenv('ENV') == 'production':
    AppSettings.apply_production_settings()
else:
    AppSettings.apply_development_settings()
```

### 2. 设置验证

```python
# 好的做法：验证设置
def validate_and_apply_settings():
    try:
        Settings.set_cdp_timeout(30)
        Settings.set_language('zh')
        
        # 验证设置是否生效
        assert Settings.get_cdp_timeout() == 30
        assert Settings.get_language() == 'zh'
        
        print("设置验证成功")
        return True
    except Exception as e:
        print(f"设置验证失败: {e}")
        return False
```

### 3. 设置备份

```python
# 好的做法：备份和恢复设置
class SettingsBackup:
    def __init__(self):
        self.backup = {}
    
    def backup_settings(self):
        self.backup = {
            'cdp_timeout': Settings.get_cdp_timeout(),
            'page_load_timeout': Settings.get_page_load_timeout(),
            'script_timeout': Settings.get_script_timeout(),
            'language': Settings.get_language(),
            'raise_when_ele_not_found': Settings.get_raise_when_ele_not_found(),
        }
    
    def restore_settings(self):
        for key, value in self.backup.items():
            getattr(Settings, f'set_{key}')(value)

# 使用备份
backup = SettingsBackup()
backup.backup_settings()

# 修改设置
Settings.set_cdp_timeout(60)

# 恢复设置
backup.restore_settings()
```

---

## 🎯 常见问题

### Q1: 设置不生效怎么办？

**A:** 请检查：
- 设置是否在页面对象创建之前应用
- 设置值是否有效
- 是否有其他代码覆盖了设置

### Q2: 如何重置所有设置？

**A:** 使用重置方法：
```python
# 重置所有设置
Settings.reset_to_default()

# 或者逐个重置
Settings.reset_cdp_timeout()
Settings.reset_language()
Settings.reset_raise_when_ele_not_found()
```

### Q3: 设置会影响性能吗？

**A:** 设置本身不影响性能，但：
- 过短的超时可能导致操作失败
- 过长的超时可能导致等待时间过长
- 建议根据实际需求调整

---

## 📖 下一步

现在您已经了解了全局设置的基本用法，可以：

1. [学习配置文件用法](ini_file.md)
2. [了解错误处理](errors.md)
3. [掌握命令行工具](commands.md)
4. [学习性能优化](accelerate_reading.md)

祝您使用愉快！🎉
