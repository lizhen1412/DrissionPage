#! /usr/bin/env python3
# -*- coding:utf-8 -*-
"""
DrissionPage 项目打包配置文件
用于构建和分发 Python 包
"""
from setuptools import setup, find_packages
import re
from pathlib import Path

def get_version():
    """
    从 version.py 文件读取版本号，而不是导入包
    这样可以避免在构建时导入整个包，防止依赖问题
    """
    version_py = Path(__file__).parent / 'DrissionPage' / 'version.py'
    with open(version_py, 'r', encoding='utf-8') as f:
        content = f.read()
        # 使用正则表达式提取版本号
        match = re.search(r"__version__\s*=\s*['\"]([^'\"]+)['\"]", content)
        if match:
            return match.group(1)
    raise RuntimeError("Unable to find version string")

# 读取 README.md 作为包的详细描述
with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    # 包的基本信息
    name="DrissionPage",  # 包名，pip install 时使用的名称
    version=get_version(),  # ✅ 只读取文件，不导入包
    author="g1879",  # 作者
    author_email="g1879@qq.com",  # 作者邮箱
    
    # 包描述
    description="Python based web automation tool. It can control the browser and send and receive data packets.",  # 简短描述
    long_description=long_description,  # 详细描述（来自 README.md）
    long_description_content_type="text/markdown",  # 描述格式
    keywords="DrissionPage",  # 关键词
    url="https://DrissionPage.cn",  # 项目主页
    
    # 包配置
    include_package_data=True,  # 包含非 Python 文件（如配置文件）
    packages=find_packages(),  # 自动发现所有包
    zip_safe=False,  # 不建议以 zip 方式安装
    
    # 依赖包列表
    install_requires=[
        'lxml',  # XML/HTML 解析库
        'requests',  # HTTP 请求库
        'cssselect',  # CSS 选择器
        'DownloadKit>=2.0.7',  # 下载工具
        'websocket-client',  # WebSocket 客户端
        'click',  # 命令行工具
        'tldextract>=3.4.4',  # 域名提取
        'psutil'  # 系统信息
    ],
    
    # 分类信息
    classifiers=[
        "Programming Language :: Python :: 3.6",  # 支持的 Python 版本
        "Development Status :: 4 - Beta",  # 开发状态
        "Topic :: Utilities",  # 主题分类
        # "License :: OSI Approved :: BSD License",  # 许可证（已注释）
    ],
    
    # Python 版本要求
    python_requires='>=3.6',  # 最低 Python 版本要求
    
    # 命令行工具入口点
    entry_points={
        'console_scripts': [
            'dp = DrissionPage._functions.cli:main',  # 安装后可使用 'dp' 命令
        ],
    },
)
