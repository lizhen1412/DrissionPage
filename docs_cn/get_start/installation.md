🌏 安装
---

## ✅️️ 系统要求

操作系统：Windows、Linux 或 Mac。

Python 版本：3.6 及以上。

支持的浏览器：基于 Chromium 的浏览器（如 Chrome 和 Edge）。

---

## ✅️️ 安装

请使用 pip 安装 DrissionPage：

```shell
pip install DrissionPage
```

---

## ✅️️ 升级

### 📌 升级到最新稳定版本

```shell
pip install DrissionPage --upgrade
```

---

### 📌 升级到指定版本

```shell
pip install DrissionPage==4.0.0b17
```

---

## ✅️️ 验证安装

安装完成后，可以通过以下方式验证安装是否成功：

```python
from DrissionPage import ChromiumPage

# 创建页面对象
page = ChromiumPage()

# 访问网页
page.get('https://www.baidu.com')

# 获取页面标题
print(page.title)

# 关闭浏览器
page.quit()
```

如果程序能正常运行并输出页面标题，说明安装成功。

---

## ✅️️ 常见问题

### Q1: 安装失败怎么办？

**A:** 请检查以下几点：
- 确保 Python 版本为 3.6 及以上
- 确保网络连接正常
- 尝试使用国内镜像源：`pip install DrissionPage -i https://pypi.tuna.tsinghua.edu.cn/simple/`

### Q2: 找不到 Chrome 浏览器怎么办？

**A:** DrissionPage 会自动查找系统中的 Chrome 浏览器，如果找不到，请：
- 确保已安装 Chrome 或 Edge 浏览器
- 手动指定浏览器路径（详见浏览器配置章节）

### Q3: 权限错误怎么办？

**A:** 如果遇到权限错误，请：
- 使用管理员权限运行命令提示符
- 或者使用用户安装：`pip install DrissionPage --user`

---

## ✅️️ 卸载

如果需要卸载 DrissionPage：

```shell
pip uninstall DrissionPage
```

---

## ✅️️ 依赖说明

DrissionPage 的主要依赖包括：

- `requests` - HTTP 请求库
- `lxml` - XML/HTML 解析库
- `cssselect` - CSS 选择器支持
- `DownloadKit` - 下载工具
- `websocket-client` - WebSocket 客户端
- `click` - 命令行工具
- `tldextract` - 域名解析
- `psutil` - 系统进程管理

这些依赖会在安装 DrissionPage 时自动安装。
