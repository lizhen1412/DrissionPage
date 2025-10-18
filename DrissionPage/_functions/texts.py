#! /usr/bin/env python3
# -*- coding:utf-8 -*-
"""
DrissionPage 文本处理模块
提供国际化文本支持和错误消息管理

@Author   : g1879
@Contact  : g1879@qq.com
@Website  : https://DrissionPage.cn
@Copyright: (c) 2020 by g1879, Inc. All Rights Reserved.
"""


class TextClass:
    """
    文本处理类
    
    用于管理项目中的各种文本消息，包括错误消息、提示信息等。
    支持多语言切换和参数化消息。
    """
    
    def __init__(self, texts_dict=None):
        """
        初始化文本处理类
        
        Args:
            texts_dict (dict, optional): 文本字典，包含各种文本消息的键值对
                                      如果为 None，则使用空字典
        """
        self._texts = texts_dict or {}
    
    def get(self, key, default=None):
        """
        获取指定键的文本消息
        
        Args:
            key (str): 文本消息的键
            default: 如果键不存在时返回的默认值
            
        Returns:
            str: 对应的文本消息，如果键不存在则返回默认值
        """
        return self._texts.get(key, default)
    
    def join(self, *args, **kwargs):
        """
        连接多个文本参数
        
        将传入的参数连接成一个字符串，过滤掉空值。
        主要用于构建包含参数的复杂消息。
        
        Args:
            *args: 要连接的文本参数
            **kwargs: 关键字参数（当前未使用，保留用于扩展）
            
        Returns:
            str: 连接后的文本字符串
        """
        if not args:
            return ""
        # 过滤掉空值并转换为字符串
        return " ".join(str(arg) for arg in args if arg)


def get_txt_class(code=None):
    """
    获取文本处理类实例
    
    根据语言代码返回对应的文本处理类。
    目前支持默认的英文文本，未来可扩展支持多语言。
    
    Args:
        code (str, optional): 语言代码，如 'en', 'zh' 等
                           目前未使用，保留用于未来的多语言支持
            
    Returns:
        TextClass: 文本处理类实例，包含默认的英文文本消息
    """
    # 默认文本字典 - 包含项目中常用的错误消息和提示信息
    default_texts = {
        # 元素相关错误
        'ELEMENTNOTFOUNDERROR': 'Element not found',  # 元素未找到
        'ELEMENTLOSTERROR': 'Element lost',  # 元素丢失
        
        # 浏览器相关错误
        'ALERTEXISTSERROR': 'Alert exists',  # 存在警告框
        'CONTEXTLOSTERROR': 'Context lost',  # 上下文丢失
        'CDPERROR': 'CDP error',  # CDP 协议错误
        'PAGEDISCONNECTEDERROR': 'Page disconnected',  # 页面断开连接
        
        # JavaScript 相关错误
        'JAVASCRIPTERROR': 'JavaScript error',  # JavaScript 错误
        
        # 几何相关错误
        'NORECTERROR': 'No rect error',  # 无矩形信息错误
        
        # 通用错误
        'GET_OBJ_FAILED': 'Failed to get object',  # 获取对象失败
        'INVALID_URL': 'Invalid URL',  # 无效的 URL
    }
    
    # 返回包含默认文本的 TextClass 实例
    return TextClass(default_texts)
