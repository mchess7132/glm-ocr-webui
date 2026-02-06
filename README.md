<div align="center">

# 🖼️ GLM-OCR Web UI

[![GitHub Stars](https://img.shields.io/github/stars/mchess7132/glm-ocr-webui?style=flat-square&logo=github)](https://github.com/mchess7132/glm-ocr-webui/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/mchess7132/glm-ocr-webui?style=flat-square&logo=github)](https://github.com/mchess7132/glm-ocr-webui/network/members)
[![License](https://img.shields.io/github/license/mchess7132/glm-ocr-webui?style=flat-square)](https://github.com/mchess7132/glm-ocr-webui/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.10+-blue?style=flat-square&logo=python)](https://www.python.org/downloads/)
[![Gradio](https://img.shields.io/badge/Gradio-5.0+-orange?style=flat-square)](https://www.gradio.app/)

---

## 📖 简介 | Introduction

GLM-OCR Web UI 是一个基于 **Gradio** 构建的现代化 Web OCR 应用程序，它利用 **Ollama** 本地部署的 **GLM-OCR** 模型，实现对图片、PDF 文档和 Word 文档的高精度文字识别。

GLM-OCR Web UI is a modern Web OCR application built with **Gradio**, utilizing the locally deployed **GLM-OCR** model through **Ollama** to achieve high-precision text recognition for images, PDF documents, and Word documents.

### ✨ 核心特性 | Key Features

| 特性 | Feature | 描述 | Description |
|------|---------|------|-------------|
| 📁 多格式支持 | Multi-format Support | 图片、PDF、Word 文档 | Images, PDF, Word documents |
| 🌐 本地运行 | Local Running | 数据不离开你的电脑 | Data stays on your machine |
| 📝 Markdown 输出 | Markdown Output | 结构化的识别结果 | Structured recognition results |
| 🔄 批量处理 | Batch Processing | 一次性处理多个文件 | Process multiple files at once |
| 🎨 美观界面 | Beautiful UI | 响应式设计，支持深色模式 | Responsive design with dark mode support |
| 📋 一键复制 | One-click Copy | 快速复制识别结果 | Quickly copy recognition results |
| 💾 导出功能 | Export Function | 导出为 Markdown 文件 | Export as Markdown file |

---

## 🚀 快速开始 | Quick Start

### 环境要求 | Prerequisites

- **Python**: 3.10 或更高版本 | 3.10 or higher
- **Ollama**: 已安装并运行 | Installed and running
- **GLM-OCR 模型**: 已通过 Ollama 下载 | Downloaded via Ollama
- **系统依赖**: poppler（用于 PDF 处理）| poppler (for PDF processing)

### 1️⃣ 安装步骤 | Installation Steps

```bash
# 克隆或下载本项目 | Clone or download this project
git clone https://github.com/mchess7132/glm-ocr-webui.git
cd glm-ocr-webui

# 创建虚拟环境（推荐）| Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/macOS
# 或 | or
venv\Scripts\activate  # Windows

# 安装依赖 | Install dependencies
pip install -r requirements.txt
```

### 2️⃣ 安装 GLM-OCR 模型 | Install GLM-OCR Model

```bash
# 确保 Ollama 服务正在运行 | Ensure Ollama service is running
ollama serve

# 下载 GLM-OCR 模型 | Download GLM-OCR model
ollama pull glm-ocr

# 验证模型安装 | Verify model installation
ollama list
```

### 3️⃣ 配置说明 | Configuration

创建 `.env` 文件进行自定义配置（可选）：

Create `.env` file for custom configuration (optional):

```env
# Ollama 服务器地址 | Ollama server address
OLLAMA_BASE_URL=http://localhost:11434

# 日志级别 | Log level
LOG_LEVEL=INFO
```

### 4️⃣ 启动应用 | Launch Application

```bash
# 启动 Web 应用 | Start web application
python app.py

# 应用将在以下地址运行 | Application will run at
# http://localhost:7860
```

---

## 📖 使用指南 | User Guide

### 界面说明 | Interface Overview

```
┌─────────────────────────────────────────────────────────┐
│                    GLM-OCR Web UI                       │
├─────────────────────────────────────────────────────────┤
│  📁 上传文件                                               │
│  ┌─────────────────────────────────────────────────┐    │
│  │  拖拽文件到这里 或 点击选择                        │    │
│  │  支持: PNG, JPG, PDF, DOC, DOCX                │    │
│  └─────────────────────────────────────────────────┘    │
│                                                         │
│  🔄 开始转换                                              │
│                                                         │
│  📄 PDF 输出模式                                          │
│  ○ 合并为一个文件                                        │
│  ○ 每页独立文件                                          │
│                                                         │
│  📑 显示页面标记                                         │
│  └─────────────────────────────────────────────────────┘
│                                                         │
│  📝 OCR 识别结果                                         │
│  ┌─────────────────────────────────────────────────┐    │
│  │                                                 │    │
│  │        识别结果将显示在这里                        │    │
│  │                                                 │    │
│  └─────────────────────────────────────────────────┘    │
│                                                         │
│  📋 复制到剪贴板    💾 导出为 Markdown                    │
└─────────────────────────────────────────────────────────┘
```

### 操作步骤 | Step-by-step Guide

#### 步骤一：上传文件 | Step 1: Upload Files

- **拖拽上传**：将文件拖拽到上传区域
- **点击选择**：点击上传区域选择文件
- **批量上传**：支持同时选择多个文件

#### 步骤二：设置选项 | Step 2: Configure Options

- **PDF 输出模式**：
  - `合并为一个文件`：所有页面合并为一个输出
  - `每页独立文件`：每页分别显示在独立标签页

- **页面标记**：选择是否显示页面编号标记

#### 步骤三：开始识别 | Step 3: Start Recognition

点击 `🔄 开始转换` 按钮，程序将自动处理文件。

#### 步骤四：查看和导出结果 | Step 4: View and Export Results

- **查看结果**：识别结果显示在右侧文本框
- **复制结果**：点击 `📋 复制到剪贴板`
- **导出文件**：点击 `💾 导出为 Markdown`

---

## 📁 项目结构 | Project Structure

```
glm-ocr-webui/
├── 📄 app.py                 # 主应用程序 | Main application
├── 📄 ollama_client.py       # Ollama 客户端 | Ollama client
├── 📄 requirements.txt        # 依赖列表 | Dependencies list
├── 📄 .gitignore            # Git 忽略配置 | Git ignore config
├── 📄 LICENSE               # 许可证 | License
├── 📄 README.md             # 英文 README | English README
├── 📄 README_CN.md          # 中文 README | Chinese README
├── 📄 CONTRIBUTING.md       # 贡献指南 | Contributing guide
├── 📁 src/                  # 源代码目录 | Source code directory
│   ├── 📄 __init__.py       # 包初始化 | Package initialization
│   ├── 📁 models/           # 数据模型 | Data models
│   ├── 📁 utils/            # 工具函数 | Utility functions
│   └── 📁 handlers/         # 处理器 | Handlers
├── 📁 tests/                # 测试文件 | Test files
├── 📁 docs/                 # 文档目录 | Documentation
└── 📁 examples/             # 示例文件 | Example files
```

---

## 🛠️ 技术栈 | Tech Stack

| 技术 | Technology | 用途 | Purpose |
|------|------------|------|---------|
| **Python** | Python | 主要开发语言 | Primary language |
| **Gradio** | Gradio | Web UI 框架 | Web UI framework |
| **Ollama** | Ollama | 本地 LLM 部署 | Local LLM deployment |
| **GLM-OCR** | GLM-OCR | OCR 识别模型 | OCR recognition model |
| **pypdf** | pypdf | PDF 处理 | PDF processing |
| **python-docx** | python-docx | Word 文档处理 | Word document processing |
| **pdf2image** | pdf2image | PDF 转图片 | PDF to image conversion |
| **requests** | requests | HTTP 客户端 | HTTP client |
| **Pillow** | Pillow | 图像处理 | Image processing |

---

## ❓ 常见问题 | FAQ

### Q: 上传文件后没有反应？

**A**: 请检查以下内容：

1. Ollama 服务是否正在运行：
   ```bash
   ollama list
   ```

2. GLM-OCR 模型是否已安装：
   ```bash
   ollama list | grep glm-ocr
   ```

3. 查看控制台错误信息

---

### Q: 识别结果为空或乱码？

**A**: 可能的原因和解决方案：

1. **图片质量问题**：
   - 确保图片清晰度足够
   - 检查图片是否包含可识别的文字

2. **PDF 是图片型**：
   - 纯图片扫描的 PDF 需要先转换为图片
   - 使用 OCR 功能时会自动尝试识别

3. **模型问题**：
   - 重新安装模型：`ollama pull glm-ocr`
   - 检查 Ollama 服务状态

---

### Q: 识别速度很慢？

**A**: GLM-OCR 模型较大，首次运行需要加载模型：

- 首次识别可能需要 1-3 分钟
- 后续识别会快很多（模型已加载）
- 建议使用 GPU 加速（如果可用）

---

### Q: 内存不足怎么办？

**A**: GLM-OCR 模型需要约 4GB 内存：

- 关闭其他占用内存的程序
- 使用更小的图片尺寸
- 分批处理大量文件

---

### Q: 如何处理多语言混合文档？

**A**: GLM-OCR 对多语言支持良好：

- 自动检测语言
- 保持原文的语言结构
- 支持中英文混合识别

---

## 🔧 故障排除 | Troubleshooting

### 问题 1：ModuleNotFoundError

```bash
# 解决方案 | Solution
pip install -r requirements.txt --upgrade
```

### 问题 2：Ollama 服务器不可用

```bash
# 1. 确保 Ollama 运行 | Ensure Ollama is running
ollama serve

# 2. 检查端口 | Check port (默认 11434 | default 11434)
netstat -an | grep 11434

# 3. 验证模型 | Verify model
ollama list
```

### 问题 3：PDF 处理失败

```bash
# 1. 确认 PDF 未损坏 | Confirm PDF is not corrupted
# 2. 确保 PDF 未加密 | Ensure PDF is not encrypted
# 3. 安装系统依赖 | Install system dependencies

# Ubuntu/Debian
sudo apt-get install poppler-utils

# macOS
brew install poppler

# Windows
# 下载并安装 poppler for Windows
```

### 问题 4：内存不足

```bash
# 减少同时处理的图片数量
# Reduce number of images processed simultaneously
# 或 | or
# 使用更小的图片
# Use smaller images
```

---

## 🤝 贡献指南 | Contributing Guide

我们欢迎社区贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

We welcome community contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### 贡献方式 | Ways to Contribute

- 🐛 **报告 Bug**：发现问题时提交 Issue
- 💡 **提出建议**：功能建议或改进意见
- 📝 **完善文档**：改进文档或添加翻译
- 💻 **提交代码**：修复 bug 或添加功能

---

## 📝 更新日志 | Changelog

查看 [CHANGELOG.md](CHANGELOG.md) 了解版本历史。

See [CHANGELOG.md](CHANGELOG.md) for version history.

---

## 📄 许可证 | License

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## 🙏 致谢 | Acknowledgments

- **[Gradio](https://www.gradio.app/)** - 优秀的机器学习 Web 界面框架
- **[Ollama](https://ollama.com/)** - 本地大语言模型部署工具
- **[GLM-OCR](https://github.com/zai-org/glm-ocr)** - 强大的 OCR 识别模型
- **[智谱 AI](https://www.zhipuai.com/)** - GLM 模型开发者

---

## 📞 联系方式 | Contact

- **GitHub Issues**：问题反馈和功能建议
- **GitHub Discussions**：社区讨论

---

<div align="center">

**如果这个项目对你有帮助，请给我们一个 ⭐ Star！**

**If this project helps you, please give us a ⭐ Star!**

</div>

</div>
