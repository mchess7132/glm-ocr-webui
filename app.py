#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=====================================================================
GLM-OCR Web UI - 主应用程序文件
GLM-OCR Web UI - Main Application File

基于 Gradio 构建的 Web 界面，用于与 GLM-OCR 模型进行交互，
支持图片、PDF 和 Word 文档的 OCR 识别。

功能特性：
- 多格式文件支持（图片、PDF、Word）
- 批量文件处理
- Markdown 格式输出
- 本地运行，数据隐私保护

Author: GLM-OCR Team
License: MIT License
Repository: https://github.com/yourusername/glm-ocr-webui
=====================================================================
"""

# 标准库导入 | Standard Library Imports
import gradio as gr  # Gradio Web UI 框架
from ollama_client import OllamaOCR  # Ollama OCR 客户端
from pypdf import PdfReader  # PDF 文件读取
from datetime import datetime  # 日期时间处理
import re  # 正则表达式

# 初始化 OCR 客户端
# Initialize OCR client
ocr_client = OllamaOCR()


def is_pdf_file(file_path: str) -> bool:
    """
    检查文件是否为 PDF 格式
    Check if the file is a PDF format

    Args:
        file_path: 文件路径 | File path

    Returns:
        bool: 如果是 PDF 文件返回 True | Returns True if PDF file
    """
    return file_path.lower().endswith('.pdf')


def is_doc_file(file_path: str) -> bool:
    """
    检查文件是否为 Word 文档格式（.doc 或 .docx）
    Check if the file is a Word document (.doc or .docx)

    Args:
        file_path: 文件路径 | File path

    Returns:
        bool: 如果是 Word 文档返回 True | Returns True if Word document
    """
    return file_path.lower().endswith(('.doc', '.docx'))


def process_doc_file(file_path: str) -> str:
    """
    从 Word 文档中提取文本内容
    Extract text content from Word documents

    Args:
        file_path: Word 文档路径 | Word document path

    Returns:
        str: 提取的文本内容 | Extracted text content
    """
    try:
        from docx import Document
        doc = Document(file_path)
        text = '\n'.join([para.text for para in doc.paragraphs])
        return text if text.strip() else "[未提取到文本 | No text extracted]"
    except ImportError:
        return "[错误：未安装 python-docx，请运行：pip install python-docx | Error: python-docx not installed]"
    except Exception as e:
        return f"[处理文档时出错 | Error processing document: {str(e)}]"


def clean_pdf_text(text: str) -> str:
    """
    清理 PDF 提取的文本
    Clean up extracted PDF text

    保留原始行结构，仅移除过多的空行。
    Preserves original line structure, removes excessive blank lines only.

    Args:
        text: 原始文本 | Raw text

    Returns:
        str: 清理后的文本 | Cleaned text
    """
    if not text:
        return text

    # 移除超过 3 个连续空行
    # Remove excessive blank lines (3+ blank lines -> 2 blank lines)
    text = re.sub(r'\n\s*\n\s*\n\s*', '\n\n', text)
    return text.strip()


def process_pdf_pages(
    pdf_path: str,
    output_mode: str = "合并为一个文件",
    show_page_markers: bool = True
) -> str | list:
    """
    处理 PDF 文件并返回 OCR 结果
    Process PDF file and return OCR results

    Args:
        pdf_path: PDF 文件路径 | Path to PDF file
        output_mode: 输出模式 | Output mode
            - "合并为一个文件" 或 "merge": 合并所有页面
            - "每页独立文件" 或 "separate": 逐页输出
        show_page_markers: 是否显示页面标记 | Whether to show page markers

    Returns:
        str | list: 合并的字符串或页面列表 | Combined string or list of strings
    """
    try:
        from pdf2image import convert_from_path
        reader = PdfReader(pdf_path)
        total_pages = len(reader.pages)

        # 支持中英文模式值
        # Support both Chinese and English values
        is_merge = output_mode in ["合并为一个文件", "merge"]
        is_separate = output_mode in ["每页独立文件", "separate"]

        if is_merge:
            results = []
            for i, page in enumerate(reader.pages):
                text = page.extract_text()

                # 如果没有提取到文本，使用 OCR 识别页面图片
                # If no text found, use OCR to recognize the page image
                if not text or not text.strip():
                    try:
                        # 将页面转换为图片
                        # Convert page to image
                        images = convert_from_path(
                            pdf_path,
                            first_page=i + 1,
                            last_page=i + 1
                        )
                        if images:
                            # 保存临时图片并进行 OCR 识别
                            # Save temporary image and use OCR
                            import tempfile
                            import os
                            temp_path = os.path.join(
                                tempfile.gettempdir(),
                                f"pdf_page_{i}.png"
                            )
                            images[0].save(temp_path, 'PNG')
                            text = ocr_client.recognize(temp_path)
                            text = clean_pdf_text(text)

                            # 清理临时文件
                            # Clean up temporary file
                            try:
                                os.remove(temp_path)
                            except:
                                pass
                    except Exception as ocr_err:
                        text = f"[OCR 错误 | OCR Error: {str(ocr_err)}]"
                else:
                    # 清理文本 - 移除过多的换行
                    text = clean_pdf_text(text)

                if text and text.strip():
                    if show_page_markers:
                        results.append(
                            f"--- 第 {i + 1}/{total_pages} 页 | Page {i + 1}/{total_pages} ---\n\n{text}"
                        )
                    else:
                        results.append(text)
                else:
                    if show_page_markers:
                        results.append(
                            f"--- 第 {i + 1}/{total_pages} 页 | Page {i + 1}/{total_pages} ---\n\n"
                            "[未提取到文本 - 可能是图片型 PDF | No text extracted - may be image-only PDF]"
                        )
                    else:
                        results.append(
                            "[未提取到文本 - 可能是图片型 PDF | No text extracted - may be image-only PDF]"
                        )

            # 添加页面分隔符
            # Add page separator between pages
            if not show_page_markers:
                return '\n\n'.join(results)
            return "\n\n".join(results)

        elif is_separate:
            # 分离模式 - 返回标签页列表
            # Separate mode - return list for tabs
            results = []
            for i, page in enumerate(reader.pages):
                text = page.extract_text()

                # 如果没有提取到文本，使用 OCR
                # If no text found, use OCR
                if not text or not text.strip():
                    try:
                        from pdf2image import convert_from_path
                        images = convert_from_path(
                            pdf_path,
                            first_page=i + 1,
                            last_page=i + 1
                        )
                        if images:
                            import tempfile
                            import os
                            temp_path = os.path.join(
                                tempfile.gettempdir(),
                                f"pdf_page_{i}.png"
                            )
                            images[0].save(temp_path, 'PNG')
                            text = ocr_client.recognize(temp_path)
                            text = clean_pdf_text(text)
                            try:
                                os.remove(temp_path)
                            except:
                                pass
                    except Exception as ocr_err:
                        text = f"[OCR 错误 | OCR Error: {str(ocr_err)}]"
                else:
                    text = clean_pdf_text(text)

                if text and text.strip():
                    results.append(text)
                else:
                    results.append(
                        "[未提取到文本 - 可能是图片型 PDF | No text extracted - may be image-only PDF]"
                    )
            return results
        else:
            # 默认使用合并模式
            # Default to merge mode
            return process_pdf_pages(pdf_path, "合并为一个文件", show_page_markers)

    except ImportError:
        return "[错误：未安装 pdf2image，请运行：pip install pdf2image | Error: pdf2image not installed]"
    except Exception as e:
        return f"处理 PDF 时出错 | Error processing PDF: {str(e)}"


def process_single_file(
    file,
    pdf_output_mode: str = "合并为一个文件",
    show_page_markers: bool = True
) -> str:
    """
    处理单个上传的文件并返回 OCR 结果
    Process a single uploaded file and return OCR results

    Args:
        file: Gradio 上传的文件对象 | Gradio file upload object
        pdf_output_mode: PDF 输出模式 | PDF output mode
        show_page_markers: 是否显示页面标记 | Whether to show page markers

    Returns:
        str: OCR 识别结果 | OCR recognition result
    """
    if file is None:
        return ""

    try:
        file_path = file.name

        # 处理 PDF 文件
        # Handle PDF files
        if is_pdf_file(file_path):
            return process_pdf_pages(file_path, pdf_output_mode, show_page_markers)

        # 处理 Word 文档
        # Handle Word documents
        if is_doc_file(file_path):
            return process_doc_file(file_path)

        # 处理图片文件
        # Handle image files
        return ocr_client.recognize(file_path)

    except Exception as e:
        return f"错误 | Error: {str(e)}"


def process_multiple_files(
    files,
    pdf_output_mode: str = "合并为一个文件",
    show_page_markers: bool = True
) -> str:
    """
    处理多个上传的文件并返回合并的 OCR 结果
    Process multiple uploaded files and return combined OCR results

    Args:
        files: Gradio 上传的文件列表 | List of Gradio file upload objects
        pdf_output_mode: PDF 输出模式 | PDF output mode
        show_page_markers: 是否显示页面标记 | Whether to show page markers

    Returns:
        str: 合并的 OCR 结果 | Combined OCR results
    """
    if files is None or len(files) == 0:
        return ""

    results = []
    for file in files:
        try:
            file_path = file.name

            if is_pdf_file(file_path):
                result = process_pdf_pages(file_path, pdf_output_mode, show_page_markers)
                results.append(f"## {file.name}\n\n{result}")
            else:
                result = ocr_client.recognize(file_path)
                results.append(f"## {file.name}\n\n{result}")

        except Exception as e:
            results.append(f"## {file.name}\n\n错误 | Error: {str(e)}")

    return "\n\n---\n\n".join(results)


# ============================================================================
# Gradio Web UI 界面构建
# Gradio Web UI Interface Construction
# ============================================================================

with gr.Blocks(
    title="GLM-OCR Web UI",
    theme=gr.themes.Soft(),
    css="""
    .gradio-container {
        max-width: 1200px !important;
    }
    """
) as demo:
    # 页面标题 | Page Title
    gr.Markdown(
        """
        # 🖼️ GLM-OCR Web UI
        基于 Gradio 的 OCR 识别工具 | OCR Recognition Tool based on Gradio

        支持图片、PDF 和 Word 文档的文字识别 | Supports image, PDF and Word document recognition
        """
    )

    with gr.Row():
        with gr.Column(scale=1):
            # 文件上传组件 | File upload component
            file_upload = gr.File(
                label="📁 上传文件 | Upload Files",
                file_types=['image/*', '.pdf', '.doc', '.docx'],
                file_count="multiple",
                elem_id="file-upload",
                info="支持的格式 | Supported formats: PNG, JPG, PDF, DOC, DOCX"
            )

            # 转换按钮 | Convert button
            convert_button = gr.Button(
                "🔄 开始转换 | Start Conversion",
                variant="primary",
                size="lg"
            )

            # PDF 输出模式选择器 | PDF output mode selector
            pdf_output_mode = gr.Radio(
                label="📄 PDF 输出模式 | PDF Output Mode",
                choices=["合并为一个文件 | Merge to Single File", "每页独立文件 | Separate Pages"],
                value="合并为一个文件 | Merge to Single File",
                elem_id="pdf-output-mode",
                info="选择如何处理多页 PDF | Choose how to handle multi-page PDFs"
            )

            # 页面标记开关 | Page marker toggle
            show_page_markers = gr.Checkbox(
                label="📑 显示页面标记 | Show Page Markers",
                value=True,
                elem_id="show-page-markers",
                info="显示 '--- 第 X/Y 页 ---' 标记 | Show '--- Page X/Y ---' markers"
            )

            # 隐藏组件 - 存储原始 OCR 结果
            # Hidden components - store raw OCR result
            raw_ocr_result = gr.Textbox(
                visible=False,
                elem_id="raw-ocr-result"
            )

            # 隐藏组件 - 存储页面数量
            # Hidden component - store page count
            pdf_page_count = gr.Number(
                visible=False,
                elem_id="pdf-page-count"
            )

            # PDF 文件路径存储
            # PDF file path storage
            pdf_file_path = gr.Textbox(
                visible=False,
                elem_id="pdf-file-path"
            )

        with gr.Column(scale=2):
            # 结果显示 | Results display
            result_output = gr.Textbox(
                label="📝 OCR 识别结果 | OCR Recognition Results",
                lines=20,
                elem_id="result-output",
                show_copy_button=True,
                info="识别结果将以 Markdown 格式显示 | Results will be displayed in Markdown format"
            )

            # 复制按钮和状态 | Copy button and status
            with gr.Row():
                copy_button = gr.Button(
                    "📋 复制到剪贴板 | Copy to Clipboard",
                    variant="secondary"
                )
                copy_status = gr.Textbox(
                    label="状态 | Status",
                    interactive=False,
                    lines=1,
                    elem_id="copy-status",
                    placeholder="点击按钮后显示状态 | Status will appear here"
                )

            # 导出按钮 | Export button
            export_button = gr.Button(
                "💾 导出为 Markdown | Export as Markdown",
                variant="secondary"
            )

            # 导出状态 | Export status
            export_status = gr.Textbox(
                label="导出状态 | Export Status",
                value="点击 '导出为 Markdown' 按钮下载文件 | Click 'Export as Markdown' to download",
                interactive=False,
                lines=1,
                elem_id="export-status"
            )

    # JavaScript 用于剪贴板复制
    # JavaScript for clipboard copy
    copy_js = """
    async () => {
        try {
            const text = document.querySelector('#result-output textarea').value;
            await navigator.clipboard.writeText(String(text));
            return "已复制到剪贴板 | Copied to clipboard!";
        } catch (err) {
            return "复制失败 | Copy failed: " + err.message;
        }
    }
    """

    # 绑定复制按钮事件
    # Wire up copy button event
    copy_button.click(fn=None, js=copy_js, outputs=copy_status)

    # 文件转换处理函数
    # File conversion handler
    def process_handler(files, pdf_mode, show_markers):
        if files is None or len(files) == 0:
            return "", "", ""
        if len(files) == 1:
            result = process_single_file(
                files[0],
                pdf_mode,
                show_page_markers=False
            )
            return result, result, files[0].name
        else:
            result = process_multiple_files(
                files,
                pdf_mode,
                show_page_markers=False
            )
            return result, result, "multiple"

    # 页面标记切换处理函数
    # Page marker toggle handler
    def toggle_markers(raw_result, show_markers):
        if not raw_result or not raw_result.strip():
            return raw_result

        if show_markers:
            # 将分隔符转换为带编号的标记
            # Convert separators to numbered markers
            pages = raw_result.split('\n\n--- Page Separator ---\n\n')
            marked_pages = []
            total = len([p for p in pages if p.strip()])
            for i, page in enumerate(pages):
                if page.strip():
                    marked_pages.append(
                        f"--- 第 {i + 1}/{total} 页 | Page {i + 1}/{total} ---\n\n{page}"
                    )
                else:
                    marked_pages.append(page)
            return '\n\n'.join(marked_pages)
        else:
            # 不带编号标记显示
            # Show without numbered markers
            return raw_result

    # 绑定转换按钮 - 存储原始结果到隐藏组件
    # Wire up convert button - stores raw result to hidden component
    convert_button.click(
        fn=process_handler,
        inputs=[file_upload, pdf_output_mode, show_page_markers],
        outputs=[result_output, raw_ocr_result, pdf_file_path]
    )

    # 绑定页面标记复选框 - 快速切换，不重新进行 OCR
    # Wire up page marker checkbox - fast toggle, no OCR
    show_page_markers.change(
        fn=toggle_markers,
        inputs=[raw_ocr_result, show_page_markers],
        outputs=result_output
    )

    # JavaScript 用于导出文件
    # JavaScript for exporting files
    export_js = """
    async () => {
        try {
            const text = document.querySelector('#result-output textarea').value;
            if (!text || !text.trim()) {
                return "没有内容可导出 | No content to export";
            }

            // 创建 Blob 并下载
            // Create blob and download
            const blob = new Blob([text], { type: 'text/markdown;charset=utf-8' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;

            // 使用时间戳生成文件名
            // Generate filename with timestamp
            const timestamp = new Date().toISOString().slice(0, 19).replace(/[:-]/g, '');
            a.download = 'ocr_result_' + timestamp + '.md';

            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);

            return "已下载: ocr_result_" + timestamp + ".md | Downloaded: ocr_result_" + timestamp + ".md";
        } catch (err) {
            return "导出失败 | Export failed: " + err.message;
        }
    }
    """

    # 绑定导出按钮
    # Wire up export button
    export_button.click(fn=None, js=export_js, outputs=export_status)

    # 页脚 | Footer
    gr.Markdown(
        """
        ---
        ## 📖 使用说明 | Usage Guide

        1. **上传文件** - 点击上传区域或拖拽文件
        2. **选择选项** - 设置 PDF 输出模式和页面标记
        3. **开始转换** - 点击转换按钮
        4. **查看结果** - 在右侧查看识别结果
        5. **导出结果** - 点击导出按钮保存为 Markdown

        ---

        **🔗 相关链接 | Links**

        - [GLM-OCR GitHub](https://github.com/zai-org/glm-ocr)
        - [Ollama 官网](https://ollama.com/)
        - [Gradio 文档](https://www.gradio.app/)
        """
    )

# ============================================================================
# 程序入口点
# Program Entry Point
# ============================================================================

if __name__ == "__main__":
    demo.launch()
