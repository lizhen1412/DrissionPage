# DrissionPage 项目打包指南

## 项目概述

DrissionPage 是一个基于 Python 的网页自动化工具，当前版本为 4.1.1.2。项目支持 Python 3.6 及以上版本，完全兼容 Python 3.12。

### 项目结构
- **主要模块**: `DrissionPage/` - 核心功能模块
- **配置文件**: `setup.py`, `requirements.txt`, `MANIFEST.in`
- **文档**: `docs_cn/`, `docs_en/`
- **版本信息**: `DrissionPage/version.py`

### 依赖包
项目依赖以下Python包：
- lxml
- requests
- cssselect
- DownloadKit>=2.0.7
- websocket-client
- click
- tldextract>=3.4.4
- psutil

## Python 3.12 打包命令

### 1. 环境准备

确保已安装 Python 3.12 和必要的打包工具：

```bash
# 升级 pip
python -m pip install --upgrade pip

# 安装项目依赖（必须先安装）
pip install -r requirements.txt

# 安装构建工具
pip install build twine wheel setuptools
```

### 2. 清理构建文件

```bash
# 手动清理之前的构建文件
rmdir /s build dist *.egg-info  # Windows
# 或
rm -rf build/ dist/ *.egg-info/  # Linux/Mac
```

### 3. 源码分发包 (sdist)

生成源码分发包：

```bash
# 构建源码分发包
python -m build --sdist

# 或者使用传统方式
python setup.py sdist
```

### 4. 轮子包 (wheel)

生成轮子包（推荐）：

```bash
# 构建轮子包
python -m build --wheel

# 或者使用传统方式
python setup.py bdist_wheel
```

### 5. 同时构建源码包和轮子包

```bash
# 构建所有格式的包
python -m build

# 输出文件位置: dist/
# - DrissionPage-4.1.1.2.tar.gz (源码包)
# - DrissionPage-4.1.1.2-py3-none-any.whl (轮子包)
```

### 6. 安装构建的包

```bash
# 安装轮子包（推荐）
pip install dist/DrissionPage-4.1.1.2-py3-none-any.whl

# 或安装源码包
pip install dist/DrissionPage-4.1.1.2.tar.gz

# 从源码安装（开发模式）
pip install -e .
```

### 7. 发布到 PyPI

#### 测试发布到 TestPyPI

```bash
# 上传到测试环境
python -m twine upload --repository testpypi dist/*

# 从测试环境安装
pip install --index-url https://test.pypi.org/simple/ DrissionPage
```

#### 正式发布到 PyPI

```bash
# 上传到正式环境
python -m twine upload dist/*

# 验证上传的包
python -m twine check dist/*
```

### 8. 本地验证

```bash
# 验证包的有效性
python -m twine check dist/*

# 测试安装
pip install --force-reinstall dist/DrissionPage-4.1.1.2-py3-none-any.whl

# 验证安装
python -c "import DrissionPage; print(DrissionPage.__version__)"
```

## 高级打包选项

### 1. 自定义构建配置

创建 `pyproject.toml` 文件（可选）：

```toml
[build-system]
requires = ["setuptools>=45", "wheel", "setuptools_scm[toml]>=6.2"]
build-backend = "setuptools.build_meta"

[project]
name = "DrissionPage"
dynamic = ["version"]
description = "Python based web automation tool"
readme = "README.md"
requires-python = ">=3.6"
license = {text = "Custom License"}
authors = [
    {name = "g1879", email = "g1879@qq.com"}
]
keywords = ["automation", "web", "browser", "selenium"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Internet :: WWW/HTTP :: Browsers",
    "Topic :: Software Development :: Testing",
]

[project.urls]
Homepage = "https://DrissionPage.cn"
Repository = "https://github.com/g1879/DrissionPage"
Documentation = "https://DrissionPage.cn"

[project.scripts]
dp = "DrissionPage._functions.cli:main"

[tool.setuptools.dynamic]
version = {attr = "DrissionPage.__version__"}

[tool.setuptools.packages.find]
where = ["."]
include = ["DrissionPage*"]
```

### 2. 构建优化

```bash
# 使用缓存加速构建
python -m build --wheel --outdir dist/

# 跳过依赖检查（如果确定依赖已满足）
python setup.py bdist_wheel --skip-dependency-check

# 构建时排除测试文件
python setup.py bdist_wheel --exclude-tests
```

### 3. 多平台构建

```bash
# 构建通用轮子包（适用于所有平台）
python setup.py bdist_wheel --universal

# 构建特定平台的轮子包
python setup.py bdist_wheel --plat-name win-amd64
python setup.py bdist_wheel --plat-name linux-x86_64
python setup.py bdist_wheel --plat-name macosx-10.9-x86_64
```

## 常见问题解决

### 1. 构建失败

```bash
# 清理构建缓存
rmdir /s build dist *.egg-info  # Windows
# 或 rm -rf build/ dist/ *.egg-info/  # Linux/Mac

# 重新安装依赖
pip install -r requirements.txt

# 重新构建
python -m build
```

### 2. ModuleNotFoundError: No module named 'requests'

**问题原因**: 构建过程中缺少项目依赖

**解决方案**:
```bash
# 确保在正确的虚拟环境中
# 激活虚拟环境
.venv\Scripts\activate  # Windows
# 或 source .venv/bin/activate  # Linux/Mac

# 安装所有依赖
pip install -r requirements.txt

# 验证依赖安装
pip list | findstr requests  # Windows
# 或 pip list | grep requests  # Linux/Mac
```

### 3. 依赖问题

```bash
# 检查依赖
pip check

# 升级依赖
pip install --upgrade -r requirements.txt
```

### 4. 版本冲突

```bash
# 使用虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt
```

## 验证清单

打包完成后，请验证以下项目：

- [ ] 包能正常构建
- [ ] 包能正常安装
- [ ] 导入模块无错误
- [ ] 版本号正确
- [ ] 命令行工具可用 (`dp --help`)
- [ ] 基本功能测试通过

## 注意事项

1. **Python 版本兼容性**: 项目支持 Python 3.6+，Python 3.12 完全兼容
2. **依赖管理**: 确保所有依赖包版本兼容
3. **文件包含**: `MANIFEST.in` 确保配置文件正确包含
4. **测试**: 构建后务必进行功能测试
5. **文档**: 保持文档与代码同步更新

## 相关命令总结

```bash
# 完整构建流程
# 1. 安装依赖
pip install -r requirements.txt
pip install build twine wheel setuptools

# 2. 清理构建文件
rmdir /s build dist *.egg-info  # Windows
# 或 rm -rf build/ dist/ *.egg-info/  # Linux/Mac

# 3. 构建包
python -m build

# 4. 验证和安装
python -m twine check dist/*
pip install dist/DrissionPage-4.1.1.2-py3-none-any.whl
python -c "import DrissionPage; print('安装成功，版本:', DrissionPage.__version__)"
```

---

*最后更新: 2024年*
*适用于: DrissionPage 4.1.1.2, Python 3.12*
