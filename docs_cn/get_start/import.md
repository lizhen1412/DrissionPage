# 🌏 导入模块
---

## ✅️ 页面类

页面类是用于控制浏览器或收发数据包的主要工具。

`DrissionPage` 包含三个主要页面类。请根据您的需求选择其中一个。

### 📌 `ChromiumPage`

如果您只需要控制浏览器，请导入 `ChromiumPage`。

```python
from DrissionPage import ChromiumPage
```

---

### 📌 `SessionPage`

如果您只需要收发数据包，请导入 `SessionPage`。

```python
from DrissionPage import SessionPage
```

---

### 📌 `WebPage`

`WebPage` 是最全面的页面类，允许您控制浏览器和收发数据包。

```python
from DrissionPage import WebPage
```

---

## ✅️ 配置工具

### 📌 `ChromiumOptions`

`ChromiumOptions` 类用于设置浏览器启动选项。

这些选项仅在启动浏览器时生效，不会影响已运行的浏览器。

```python
from DrissionPage import ChromiumOptions
```

---

### 📌 `SessionOptions`

`SessionOptions` 类用于设置 `Session` 对象的启动选项。

用于配置 `SessionPage` 或 `WebPage` 模式的连接参数。

```python
from DrissionPage import SessionOptions
```

---

### 📌 `Settings`

`Settings` 用于设置全局运行时配置，例如当元素未找到时是否抛出异常。

```python
from DrissionPage.common import Settings
```

---

## ✅️ 其他工具

其他可能使用的工具位于 `DrissionPage.common` 路径。

### 📌 `Keys`

`Keys` 类表示键盘按键，用于模拟按下 Ctrl、Alt 等按键。

```python
from DrissionPage.common import Keys
```

---

### 📌 `Actions`

`Actions` 类表示动作序列。

它已经内置在浏览器页面对象中，除非特别需要，否则不需要显式导入。

```python
from DrissionPage.common import Actions
```

---

### 📌 `By`

`By` 类类似于 Selenium 中使用的类，便于项目迁移。

```python
from DrissionPage.common import By
```

---

### 📌 其他工具

- `wait_until`: 等待直到给定方法返回 `True`
- `make_session_ele`: 从 HTML 字符串生成 `ChromiumElement` 对象
- `configs_to_here`: 将配置文件复制到当前路径
- `get_blob`: 获取指定的 blob 资源

```python
from DrissionPage.common import wait_until
from DrissionPage.common import make_session_ele
from DrissionPage.common import configs_to_here
```

---

## ✅️ 异常

异常位于 `DrissionPage.errors` 路径。

有关异常完整列表，请参考高级用法部分。

```python
from DrissionPage.errors import ElementNotFoundError
```

---

## ✅️ 派生对象类型

Tab 和 Element 等对象是从 Page 对象生成的。要在开发过程中进行类型检查，请从 `DrissionPage.items` 路径导入这些类型。

```python
from DrissionPage.items import SessionElement
from DrissionPage.items import ChromiumElement
from DrissionPage.items import ShadowRoot
from DrissionPage.items import NoneElement
from DrissionPage.items import ChromiumTab
from DrissionPage.items import WebPageTab
from DrissionPage.items import ChromiumFrame
```
