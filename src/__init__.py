#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=====================================================================
GLM-OCR Web UI 源代码包
GLM-OCR Web UI Source Code Package

这是一个模块化的源代码组织结构，用于更好地组织项目代码。
This is a modular source code organization structure for better project organization.

模块说明 | Module Description:
- models/     - 数据模型定义 | Data model definitions
- utils/      - 工具函数 | Utility functions
- handlers/   - 处理器和处理器 | Processors and handlers

=====================================================================
"""

__version__ = "1.0.0"
__author__ = "GLM-OCR Team"
__license__ = "MIT License"
__repository__ = "https://github.com/yourusername/glm-ocr-webui"

# 导入主要组件 | Import main components
from .models import *
from .utils import *
from .handlers import *

__all__ = [
    "__version__",
    "__author__",
    "__license__",
]
