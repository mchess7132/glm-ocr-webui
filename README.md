<div align="center">

<!-- Animated Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:4A90E2,100:7B68EE&height=200&section=header&text=GLM-OCR%20Web%20UI&fontSize=50&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=🖼️%20智能OCR识别%20·%20本地部署%20·%20隐私安全&descAlignY=55&descSize=18" alt="GLM-OCR Web UI Banner" />

<br>

<!-- Badges Row -->
<p align="center">
  <a href="https://github.com/mchess7132/glm-ocr-webui/stargazers">
    <img src="https://img.shields.io/github/stars/mchess7132/glm-ocr-webui?style=for-the-badge&logo=github&color=FFD700" alt="GitHub Stars" />
  </a>
  <a href="https://github.com/mchess7132/glm-ocr-webui/network/members">
    <img src="https://img.shields.io/github/forks/mchess7132/glm-ocr-webui?style=for-the-badge&logo=github&color=4ECDC4" alt="GitHub Forks" />
  </a>
  <a href="https://github.com/mchess7132/glm-ocr-webui/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/mchess7132/glm-ocr-webui?style=for-the-badge&color=FF6B6B" alt="License" />
  </a>
  <br>
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  </a>
  <a href="https://www.gradio.app/">
    <img src="https://img.shields.io/badge/Gradio-5.0+-FF6B6B?style=for-the-badge&logo=gradio&logoColor=white" alt="Gradio" />
  </a>
  <a href="https://ollama.com/">
    <img src="https://img.shields.io/badge/Ollama-本地部署-4A90E2?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/GLM--OCR-智谱AI-7B68EE?style=for-the-badge" alt="GLM-OCR" />
  </a>
</p>

<!-- Quick Links -->
<p align="center">
  <a href="#-快速开始--quick-start">🚀 快速开始</a> •
  <a href="#-功能演示--demo">🎬 功能演示</a> •
  <a href="#-核心特性--features">✨ 核心特性</a> •
  <a href="#-常见问题--faq">❓ 常见问题</a> •
  <a href="#-技术栈--tech-stack">🛠️ 技术栈</a>
</p>

---

</div>

## 🌟 简介 | Introduction

**GLM-OCR Web UI** 是一个基于 **Gradio** 构建的现代化 Web OCR 应用程序，它利用 **Ollama** 本地部署的 **GLM-OCR** 模型，实现对图片、PDF 文档和 Word 文档的高精度文字识别。

<p align="center">
  <strong>🔒 数据本地处理 · 🚀 开箱即用 · 🎯 高精度识别 · 🌍 多语言支持</strong>
</p>

<details>
<summary>🌐 <strong>English Description</strong></summary>

GLM-OCR Web UI is a modern Web OCR application built with **Gradio**, utilizing the locally deployed **GLM-OCR** model through **Ollama** to achieve high-precision text recognition for images, PDF documents, and Word documents.

</details>

---

## 🎬 功能演示 | Demo

<div align="center">

<!-- Demo Section Placeholder - 可添加截图或GIF -->

| 📄 PDF 识别 | 🖼️ 图片识别 | 📝 Word 文档 |
|:-----------:|:-----------:|:------------:|
| 支持多页PDF处理<br>自动分页识别 | 支持常见图片格式<br>高精度文字提取 | 完整保留文档结构<br>格式转换Markdown |

<!-- Screenshot placeholder - 用户可以替换为实际截图 -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://via.placeholder.com/800x400/2d2d2d/ffffff?text=Dark+Mode+Screenshot">
  <source media="(prefers-color-scheme: light)" srcset="https://via.placeholder.com/800x400/f5f5f5/333333?text=Light+Mode+Screenshot">
  <img alt="App Screenshot" src="https://via.placeholder.com/800x400/4A90E2/ffffff?text=GLM-OCR+Web+UI+Demo" width="80%">
</picture>

<p><i>💡 提示：您可以添加实际应用截图替换上方占位图</i></p>

</div>

---

## ✨ 核心特性 | Features

<table>
<tr>
<td width="50%">

### 🎯 智能识别
- 📁 **多格式支持** - 图片、PDF、Word 文档
- 🌐 **本地运行** - 数据不离开你的电脑
- 📝 **Markdown 输出** - 结构化的识别结果
- 🌍 **多语言** - 支持中英混合识别

</td>
<td width="50%">

### 🚀 高效便捷
- 🔄 **批量处理** - 一次性处理多个文件
- 🎨 **美观界面** - 响应式设计，深色模式
- 📋 **一键复制** - 快速复制识别结果
- 💾 **导出功能** - 导出为 Markdown 文件

</td>
</tr>
</table>

---

## 🚀 快速开始 | Quick Start

### 环境要求 | Prerequisites

| 依赖 | 版本 | 说明 |
|------|------|------|
| Python | 3.10+ | 主要开发语言 |
| Ollama | 最新版 | 本地 LLM 部署 |
| GLM-OCR | 最新版 | 通过 Ollama 下载 |
| poppler | - | PDF 处理依赖 |

### 📦 安装步骤 | Installation

```bash
# 1️⃣ 克隆项目
$ git clone https://github.com/mchess7132/glm-ocr-webui.git
$ cd glm-ocr-webui

# 2️⃣ 创建虚拟环境（推荐）
$ python -m venv venv

# Windows
$ venv\Scripts\activate

# Linux/macOS
$ source venv/bin/activate

# 3️⃣ 安装依赖
$ pip install -r requirements.txt

# 4️⃣ 安装 GLM-OCR 模型
$ ollama pull glm-ocr

# 5️⃣ 启动应用
$ python app.py

# 🎉 访问 http://localhost:7860
```

<details>
<summary>🔧 <strong>高级配置</strong>（可选）</summary>

创建 `.env` 文件进行自定义配置：

```env
# Ollama 服务器地址
OLLAMA_BASE_URL=http://localhost:11434

# 日志级别
LOG_LEVEL=INFO
```

</details>

---

## 📖 使用指南 | User Guide

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
│  📄 PDF 输出模式    ○ 合并    ○ 分页                      │
│  📑 显示页面标记    [✓] 启用                              │
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

### 三步上手

1. **📤 上传文件** - 拖拽或点击选择文件（支持批量）
2. **⚙️ 设置选项** - 选择 PDF 输出模式、是否显示页码
3. **▶️ 开始识别** - 点击转换按钮，等待结果

---

## 🛠️ 技术栈 | Tech Stack

<div align="center">

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://python.org)
[![Gradio](https://img.shields.io/badge/Gradio-FF6B6B?logo=gradio&logoColor=white)](https://gradio.app)
[![Ollama](https://img.shields.io/badge/Ollama-4A90E2?logo=ollama&logoColor=white)](https://ollama.com)
[![pypdf](https://img.shields.io/badge/pypdf-2C5F7C?logo=python&logoColor=white)](https://pypdf.readthedocs.io)
[![Pillow](https://img.shields.io/badge/Pillow-8B4513?logo=python&logoColor=white)](https://python-pillow.org)

</div>

| 组件 | 用途 |
|------|------|
| **Gradio** | Web UI 框架，快速构建交互界面 |
| **Ollama** | 本地 LLM 部署，保护数据隐私 |
| **GLM-OCR** | 智谱 AI 开源 OCR 模型 |
| **pypdf/pdf2image** | PDF 解析和转换 |
| **python-docx** | Word 文档处理 |
| **Pillow** | 图像处理和预处理 |

---

## 📁 项目结构 | Project Structure

```
glm-ocr-webui/
├── 📄 app.py                 # 主应用程序
├── 📄 ollama_client.py       # Ollama 客户端封装
├── 📄 requirements.txt        # Python 依赖
├── 📄 .env.example           # 环境变量示例
├── 📄 LICENSE                # MIT 许可证
├── 📄 README.md              # 项目文档
├── 📄 CHANGELOG.md           # 更新日志
├── 📄 CONTRIBUTING.md        # 贡献指南
├── 📁 src/                   # 源代码
│   ├── 📁 models/            # 数据模型
│   ├── 📁 utils/             # 工具函数
│   └── 📁 handlers/          # 处理器
├── 📁 tests/                 # 测试文件
└── 📁 docs/                  # 文档
```

---

## ❓ 常见问题 | FAQ

<details>
<summary><strong>Q: 上传文件后没有反应？</strong></summary>

请检查以下内容：
1. Ollama 服务是否正在运行：`ollama list`
2. GLM-OCR 模型是否已安装：`ollama list | grep glm-ocr`
3. 查看控制台错误信息

</details>

<details>
<summary><strong>Q: 识别结果为空或乱码？</strong></summary>

可能的原因和解决方案：
1. **图片质量问题** - 确保图片清晰度足够
2. **PDF 是图片型** - 扫描版 PDF 会自动尝试 OCR
3. **模型问题** - 重新安装：`ollama pull glm-ocr`

</details>

<details>
<summary><strong>Q: 识别速度很慢？</strong></summary>

GLM-OCR 模型较大，首次运行需要加载：
- 首次识别可能需要 1-3 分钟
- 后续识别会快很多（模型已缓存）
- 建议使用 GPU 加速（如果可用）

</details>

<details>
<summary><strong>Q: 内存不足怎么办？</strong></summary>

GLM-OCR 模型需要约 4GB 内存：
- 关闭其他占用内存的程序
- 使用更小的图片尺寸
- 分批处理大量文件

</details>

---

## 🔧 故障排除 | Troubleshooting

| 问题 | 解决方案 |
|------|----------|
| `ModuleNotFoundError` | `pip install -r requirements.txt --upgrade` |
| Ollama 连接失败 | 确保服务运行：`ollama serve`，检查端口 11434 |
| PDF 处理失败 | 安装 poppler：`apt-get install poppler-utils` (Ubuntu) / `brew install poppler` (macOS) |

---

## 🤝 贡献指南 | Contributing

我们欢迎社区贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

<p align="center">
  <a href="https://github.com/mchess7132/glm-ocr-webui/issues">🐛 报告 Bug</a> •
  <a href="https://github.com/mchess7132/glm-ocr-webui/issues">💡 功能建议</a> •
  <a href="https://github.com/mchess7132/glm-ocr-webui/pulls">🔀 提交代码</a>
</p>

---

## 📊 项目统计 | Stats

<div align="center">

![GitHub last commit](https://img.shields.io/github/last-commit/mchess7132/glm-ocr-webui?style=flat-square)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/mchess7132/glm-ocr-webui?style=flat-square)
![Code size](https://img.shields.io/github/languages/code-size/mchess7132/glm-ocr-webui?style=flat-square)
![Languages](https://img.shields.io/github/languages/top/mchess7132/glm-ocr-webui?style=flat-square)

</div>

---

## 📝 许可证 | License

本项目采用 [MIT](LICENSE) 许可证。

---

## 🙏 致谢 | Acknowledgments

- [Gradio](https://www.gradio.app/) - 优秀的机器学习 Web 界面框架
- [Ollama](https://ollama.com/) - 本地大语言模型部署工具
- [GLM-OCR](https://github.com/zai-org/glm-ocr) - 智谱 AI 开源 OCR 模型
- [智谱 AI](https://www.zhipuai.com/) - GLM 模型开发者

---

<div align="center">

<!-- Animated Footer -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7B68EE,100:4A90E2&height=100&section=footer" alt="Footer" />

### ⭐ 如果这个项目对你有帮助，请给我们一个 Star！

**Made with ❤️ by [mchess7132](https://github.com/mchess7132)**

</div>
