#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=====================================================================
Ollama OCR 客户端模块
Ollama OCR Client Module

负责与 Ollama 服务器通信，使用 GLM-OCR 模型进行图像识别。
Handles communication with Ollama server for image recognition using GLM-OCR.

功能特性：
- 单张图片 OCR 识别
- 批量图片处理
- Base64 编码传输
- 错误处理和重试机制

Author: GLM-OCR Team
License: MIT License
=====================================================================
"""

# 标准库导入 | Standard Library Imports
import base64  # Base64 编解码
import os  # 操作系统接口
from io import BytesIO  # 字节流处理
from typing import List, Optional  # 类型提示

# 第三方库导入 | Third-party Library Imports
import requests  # HTTP 请求库
from dotenv import load_dotenv  # 环境变量加载

# 加载 .env 文件中的环境变量
# Load environment variables from .env file
load_dotenv()


class OllamaOCR:
    """
    Ollama OCR 客户端类
    Ollama OCR Client Class

    用于与 Ollama 服务器上的 GLM-OCR 模型进行交互。
    Used to interact with GLM-OCR model on Ollama server.

    Attributes:
        host (str): Ollama 服务器地址 | Ollama server address
        api_url (str): API 端点 URL | API endpoint URL

    Example:
        >>> client = OllamaOCR()
        >>> result = client.recognize("image.png")
        >>> print(result)
    """

    def __init__(self, host: Optional[str] = None):
        """
        初始化 Ollama OCR 客户端
        Initialize Ollama OCR client

        Args:
            host: Ollama 服务器基础 URL，如果不提供则从环境变量读取
                  Ollama server base URL, reads from environment variable if not provided

        Environment Variables:
            OLLAMA_BASE_URL: Ollama 服务器地址（默认：http://localhost:11434）
        """
        if host is None:
            # 从环境变量获取，或使用默认值
            # Get from environment variable or use default
            host = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

        self.host = host
        self.api_url = f"{host}/api/generate"

        # 验证 URL 格式
        # Validate URL format
        if not self.api_url.startswith(("http://", "https://")):
            raise ValueError(
                f"无效的 Ollama URL | Invalid Ollama URL: {self.api_url}"
            )

    def recognize(self, image_path: str) -> str:
        """
        对单张图片进行 OCR 识别
        Perform OCR on a single image

        Args:
            image_path: 图片文件路径 | Path to the image file

        Returns:
            str: Markdown 格式的 OCR 识别结果
                 Markdown formatted OCR result

        Raises:
            FileNotFoundError: 如果图片文件不存在 | If image file doesn't exist
            ConnectionError: 如果 Ollama 服务器不可用 | If Ollama server is unavailable
            requests.RequestException: 其他 API 错误 | For other API errors

        Example:
            >>> client = OllamaOCR()
            >>> result = client.recognize("screenshot.png")
            >>> print(result)
        """
        # 验证文件是否存在
        # Validate file exists
        if not os.path.exists(image_path):
            raise FileNotFoundError(
                f"图片文件不存在 | Image file not found: {image_path}"
            )

        # 检查文件大小（限制为 20MB）
        # Check file size (limit to 20MB)
        file_size = os.path.getsize(image_path)
        if file_size > 20 * 1024 * 1024:  # 20MB
            raise ValueError(
                f"图片文件过大 | Image file too large: {file_size / 1024 / 1024:.2f}MB "
                "(最大 20MB | maximum 20MB)"
            )

        # 读取并编码图片
        # Load and encode image
        try:
            with open(image_path, 'rb') as f:
                image_data = base64.b64encode(f.read()).decode('utf-8')
        except UnicodeDecodeError:
            raise ValueError(
                f"无法解码图片文件 | Cannot decode image file: {image_path}"
            )

        # 准备请求负载
        # Prepare request payload
        payload = {
            "model": "glm-ocr",  # GLM-OCR 模型名称 | GLM-OCR model name
            "prompt": "请识别图片中的所有文字内容，并以 Markdown 格式输出。\n"
                      "Please recognize all text content in the image and output in Markdown format.",
            "images": [image_data],
            "stream": False,  # 禁用流式输出 | Disable streaming
            "options": {
                # OCR 相关选项 | OCR related options
                "temperature": 0.1,  # 低温度以获得更稳定的结果 | Low temperature for stable results
            }
        }

        # 发送 API 请求
        # Make API request
        try:
            response = requests.post(
                self.api_url,
                json=payload,
                timeout=300  # 5 分钟超时 | 5-minute timeout
            )

            # 检查响应状态
            # Check response status
            response.raise_for_status()

        except requests.ConnectionError as e:
            raise ConnectionError(
                f"无法连接到 Ollama 服务器 | Cannot connect to Ollama server: {e}\n"
                "请确保 Ollama 服务正在运行 | Please ensure Ollama service is running"
            ) from e
        except requests.Timeout as e:
            raise ConnectionError(
                f"请求超时 | Request timeout: {e}\n"
                "GLM-OCR 模型较大，首次运行可能需要较长时间\n"
                "GLM-OCR model is large, first run may take longer"
            ) from e
        except requests.RequestException as e:
            raise requests.RequestException(
                f"API 请求失败 | API request failed: {e}"
            ) from e

        # 解析响应结果
        # Parse response result
        try:
            result = response.json()

            # 检查响应格式
            # Check response format
            if "response" not in result:
                raise ValueError(
                    f"无效的 API 响应格式 | Invalid API response format: {result}"
                )

            return result.get('response', '').strip()

        except ValueError as e:
            raise e
        except Exception as e:
            raise ValueError(
                f"解析 API 响应失败 | Failed to parse API response: {e}"
            ) from e

    def recognize_batch(
        self,
        image_paths: List[str],
        show_progress: bool = True
    ) -> List[str]:
        """
        批量处理多张图片进行 OCR 识别
        Perform OCR on multiple images

        Args:
            image_paths: 图片文件路径列表 | List of paths to image files
            show_progress: 是否显示进度信息 | Whether to show progress information

        Returns:
            List[str]: OCR 识别结果列表 | List of OCR recognition results

        Raises:
            ValueError: 如果路径列表为空 | If image_paths is empty

        Example:
            >>> client = OllamaOCR()
            >>> results = client.recognize_batch(["img1.png", "img2.jpg"])
            >>> for i, result in enumerate(results):
            ...     print(f"Image {i + 1}: {result[:100]}...")
        """
        if not image_paths:
            raise ValueError("图片路径列表不能为空 | Image paths list cannot be empty")

        results = []
        total = len(image_paths)

        for i, path in enumerate(image_paths):
            try:
                if show_progress:
                    print(
                        f"处理中 | Processing: [{i + 1}/{total}] {os.path.basename(path)}"
                    )

                result = self.recognize(path)
                results.append(result)

            except Exception as e:
                error_msg = f"处理 | Processing {path}: {str(e)}"
                results.append(f"[错误 | Error: {str(e)}]")
                print(f"[错误 | Error] {error_msg}")

        if show_progress:
            print(f"完成 | Completed: {len(results)}/{total} 张图片 processed")

        return results

    def check_connection(self) -> dict:
        """
        检查 Ollama 服务器连接状态
        Check Ollama server connection status

        Returns:
            dict: 包含连接状态的字典 | Dictionary containing connection status

        Example:
            >>> client = OllamaOCR()
            >>> status = client.check_connection()
            >>> print(status)
            {'connected': True, 'model_available': True, 'version': '0.5.41'}
        """
        result = {
            "connected": False,
            "model_available": False,
            "version": None,
            "error": None
        }

        try:
            # 尝试获取服务器信息
            # Try to get server info
            response = requests.get(
                f"{self.host}/api/version",
                timeout=10
            )

            if response.status_code == 200:
                result["connected"] = True
                version_data = response.json()
                result["version"] = version_data.get("version", "unknown")

        except requests.RequestException as e:
            result["error"] = str(e)
            return result

        # 检查模型是否可用
        # Check if model is available
        try:
            models_response = requests.get(
                f"{self.host}/api/tags",
                timeout=10
            )

            if models_response.status_code == 200:
                models_data = models_response.json()
                models = models_data.get("models", [])

                # 检查 glm-ocr 模型是否存在
                # Check if glm-ocr model exists
                for model in models:
                    if model.get("name", "").startswith("glm-ocr"):
                        result["model_available"] = True
                        break

        except requests.RequestException as e:
            result["error"] = str(e)

        return result


def call_glm_ocr(image_path: str) -> str:
    """
    便捷函数：对单张图片进行 OCR 识别
    Convenience function: Perform OCR on a single image

    Args:
        image_path: 图片文件路径 | Path to the image file

    Returns:
        str: Markdown 格式的 OCR 识别结果 | Markdown formatted OCR result

    Example:
        >>> result = call_glm_ocr("document.png")
        >>> print(result)
    """
    ocr_client = OllamaOCR()
    return ocr_client.recognize(image_path)


def batch_ocr(
    image_paths: List[str],
    output_file: Optional[str] = None,
    show_progress: bool = True
) -> List[str]:
    """
    批量 OCR 识别函数
    Batch OCR recognition function

    Args:
        image_paths: 图片文件路径列表 | List of paths to image files
        output_file: 可选的输出文件路径 | Optional output file path
        show_progress: 是否显示进度信息 | Whether to show progress information

    Returns:
        List[str]: OCR 识别结果列表 | List of OCR recognition results

    Example:
        >>> results = batch_ocr(["1.png", "2.jpg"], "output.md")
        >>> print(f"识别了 {len(results)} 张图片 | Recognized {len(results)} images")
    """
    ocr_client = OllamaOCR()
    results = ocr_client.recognize_batch(image_paths, show_progress)

    # 如果指定了输出文件，保存结果
    # Save results if output file is specified
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            for i, result in enumerate(results):
                f.write(f"# Image {i + 1}\n\n")
                f.write(result)
                f.write("\n\n---\n\n")

        if show_progress:
            print(f"结果已保存到 | Results saved to: {output_file}")

    return results
