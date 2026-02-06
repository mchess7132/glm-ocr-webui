# 🤝 贡献指南 | Contributing Guide

感谢您对 GLM-OCR Web UI 项目的兴趣！我们欢迎社区成员贡献代码、文档、建议和反馈。

Thank you for your interest in the GLM-OCR Web UI project! We welcome contributions from the community including code, documentation, suggestions, and feedback.

---

## 📋 目录 | Table of Contents

- [如何贡献 | How to Contribute](#如何贡献--how-to-contribute)
- [开发环境设置 | Development Setup](#开发环境设置--development-setup)
- [代码规范 | Code Standards](#代码规范--code-standards)
- [提交规范 | Commit Standards](#提交规范--commit-standards)
- [Pull Request 流程 | Pull Request Process](#pull-request-流程--pull-request-process)
- [报告问题 | Reporting Issues](#报告问题--reporting-issues)

---

## 💻 如何贡献 | How to Contribute

### 🐛 报告 Bug | Report Bugs

如果您发现了 bug，请通过以下步骤报告：

If you find a bug, please report it by following these steps:

1. **搜索现有 Issue**：在提交新 Issue 之前，请先搜索是否已有相同的 bug 报告
   - Search existing Issues: Before creating a new Issue, please search if there's already a similar bug report

2. **创建新 Issue**：使用 Bug Report 模板，提供以下信息：
   - Create a new Issue: Use the Bug Report template and provide:
     - Bug 的清晰描述 | Clear description of the bug
     - 复现步骤 | Steps to reproduce
     - 预期行为 | Expected behavior
     - 实际行为 | Actual behavior
     - 截图或日志（如果适用）| Screenshots or logs (if applicable)
     - 环境信息（操作系统、Python 版本等）| Environment info (OS, Python version, etc.)

### 💡 提出建议 | Suggest Features

如果您有功能建议，请使用 Feature Request 模板：

If you have feature suggestions, please use the Feature Request template:

- 功能描述 | Feature description
- 使用场景 | Use case
- 可能的解决方案（可选）| Possible solutions (optional)
- 其他说明（可选）| Additional notes (optional)

### 📝 完善文档 | Improve Documentation

文档改进包括：
Documentation improvements include:
- 修正拼写和语法错误 | Fix spelling and grammar errors
- 改进现有文档的清晰度 | Improve clarity of existing documentation
- 添加缺少的文档 | Add missing documentation
- 翻译文档到其他语言 | Translate documentation to other languages

### 💻 编写代码 | Write Code

1. Fork 本仓库 | Fork this repository
2. 创建功能分支 | Create a feature branch
3. 编写代码 | Write code
4. 添加测试 | Add tests
5. 提交更改 | Commit changes
6. 推送分支 | Push branch
7. 创建 Pull Request | Create Pull Request

---

## 🛠️ 开发环境设置 | Development Setup

### 前置条件 | Prerequisites

- **Python**: 3.10 或更高版本 | 3.10 or higher
- **Git**: 版本控制 | Version control
- **Ollama**: 用于本地测试 | For local testing
- **GLM-OCR 模型**: 用于集成测试 | For integration testing

### 克隆仓库 | Clone Repository

```bash
# 1. Fork 本仓库 | Fork this repository
# 2. 克隆你的 Fork | Clone your fork
git clone https://github.com/YOUR-USERNAME/glm-ocr-webui.git
cd glm-ocr-webui

# 3. 添加上游仓库 | Add upstream repository
git remote add upstream https://github.com/original-owner/glm-ocr-webui.git
```

### 创建虚拟环境 | Create Virtual Environment

```bash
# 创建虚拟环境 | Create virtual environment
python -m venv venv

# 激活虚拟环境 | Activate virtual environment
# Linux/macOS:
source venv/bin/activate

# Windows:
venv\Scripts\activate

# 安装开发依赖 | Install development dependencies
pip install -r requirements.txt
```

### 安装预提交钩子 | Install Pre-commit Hooks

```bash
# 安装 pre-commit | Install pre-commit
pip install pre-commit

# 配置 pre-commit 钩子 | Configure pre-commit hooks
pre-commit install
```

---

## 📏 代码规范 | Code Standards

### Python 代码风格 | Python Code Style

本项目使用 **Black** 进行代码格式化，**isort** 进行导入排序：

This project uses **Black** for code formatting and **isort** for import sorting:

```bash
# 格式化代码 | Format code
black .

# 排序导入 | Sort imports
isort .
```

### 类型注解 | Type Annotations

所有函数应包含类型注解：

All functions should include type annotations:

```python
# ✅ 正确 | Correct
def process_file(file_path: str, mode: str) -> str:
    ...

# ❌ 错误 | Incorrect
def process_file(file_path, mode):
    ...
```

### 文档字符串 | Docstrings

使用 Google 风格的文档字符串：

Use Google-style docstrings:

```python
def example_function(param1: int, param2: str) -> bool:
    """简要描述函数功能。

    详细描述函数的工作原理、参数和返回值。

    Args:
        param1: 参数1的描述
        param2: 参数2的描述

    Returns:
        返回值的描述

    Raises:
        ValueError: 当参数无效时
        FileNotFoundError: 当文件不存在时

    Example:
        >>> result = example_function(1, "test")
        >>> print(result)
        True
    """
    ...
```

### 注释规范 | Comment Standards

- 使用中文注释和英文说明 | Use Chinese comments with English descriptions
- 复杂逻辑必须添加注释 | Complex logic must be commented
- 注释应及时更新 | Comments should be kept up to date
- 避免显而易见的注释 | Avoid obvious comments

```python
# ✅ 正确 | Correct
# 将图片转换为 Base64 编码
# Convert image to Base64 encoding
image_data = base64.b64encode(f.read()).decode('utf-8')

# ❌ 错误 | Incorrect
# 编码图片
# Encode image
image_data = base64.b64encode(f.read()).decode('utf-8')
```

---

## 📝 提交规范 | Commit Standards

### 提交信息格式 | Commit Message Format

```
<类型>(<范围>): <描述>

[可选的正文]

[可选的脚注]
```

### 类型 | Types

| 类型 | Type | 描述 | Description |
|------|------|------|-------------|
| feat | feat | 新功能 | New feature |
| fix | fix | Bug 修复 | Bug fix |
| docs | docs | 文档更新 | Documentation |
| style | style | 代码格式（不影响功能）| Code style (no functional change) |
| refactor | refactor | 重构 | Refactoring |
| perf | perf | 性能优化 | Performance improvement |
| test | test | 测试相关 | Testing |
| chore | chore | 构建工具或辅助工具 | Build tool or auxiliary tool |

### 示例 | Examples

```bash
# 功能提交 | Feature commit
git commit -m "feat(ui): 添加深色模式支持"

# 修复提交 | Fix commit
git commit -m "fix(ocr): 修复 PDF 多页处理错误"

# 文档提交 | Documentation commit
git commit -m "docs(readme): 更新安装说明"
```

---

## 🔄 Pull Request 流程 | Pull Request Process

### 创建 Pull Request | Create Pull Request

1. **保持同步**：在开始工作前，确保你的分支与上游同步
   - Keep in sync: Before starting work, ensure your branch is synchronized with upstream

```bash
git checkout main
git fetch upstream
git merge upstream/main
```

2. **创建分支**：从最新的 main 分支创建功能分支
   - Create branch: Create feature branch from latest main

```bash
git checkout -b feature/your-feature-name
```

3. **开发并测试**：完成开发后，运行测试确保没有破坏现有功能
   - Develop and test: After development, run tests to ensure no existing functionality is broken

```bash
# 运行所有测试 | Run all tests
pytest

# 运行特定测试 | Run specific tests
pytest tests/test_ocr.py
```

4. **提交更改**：使用清晰的提交信息提交更改
   - Commit changes: Commit changes with clear commit messages

5. **推送分支**：将分支推送到你的 Fork
   - Push branch: Push branch to your fork

```bash
git push origin feature/your-feature-name
```

6. **创建 PR**：在 GitHub 上创建 Pull Request
   - Create PR: Create Pull Request on GitHub

### PR 描述模板 | PR Description Template

```markdown
## 描述 | Description
<!-- 请描述您的更改 -->

## 更改类型 | Type of Change
- [ ] 🐛 Bug 修复 (Bug fix)
- [ ] ✨ 新功能 (New feature)
- [ ] 📝 文档更新 (Documentation update)
- [ ] 🎨 代码格式 (Code style update)
- [ ] ♻️ 重构 (Refactoring)
- [ ] ⚡ 性能优化 (Performance improvement)
- [ ] ✅ 测试 (Test)

## 测试 | Testing
<!-- 请描述您如何测试此更改 -->

## 截图（如果适用）| Screenshots (if applicable)
```

### PR 审查流程 | PR Review Process

1. 维护者会审查您的 PR
   - Maintainers will review your PR

2. 可能需要根据反馈进行修改
   - Modifications may be required based on feedback

3. 通过所有检查后，维护者会合并您的 PR
   - After all checks pass, maintainers will merge your PR

---

## 🐛 报告问题 | Reporting Issues

### Issue 模板 | Issue Templates

#### Bug Report

```markdown
## Bug 描述 | Bug Description
<!-- 清晰描述 bug -->

## 复现步骤 | Steps to Reproduce
1. <!-- 步骤 1 -->
2. <!-- 步骤 2 -->
3. <!-- 步骤 3 -->

## 预期行为 | Expected Behavior
<!-- 应该发生什么 -->

## 实际行为 | Actual Behavior
<!-- 实际发生了什么 -->

## 环境信息 | Environment
- 操作系统 | OS:
- Python 版本 | Python version:
- GLM-OCR Web UI 版本 | Version:

## 截图 | Screenshots
<!-- 如果适用 -->

## 日志 | Logs
<!-- 如果适用 -->
```

#### Feature Request

```markdown
## 功能描述 | Feature Description
<!-- 描述您想要的功能 -->

## 使用场景 | Use Case
<!-- 为什么要这个功能 -->

## 可能的解决方案 | Possible Solution
<!-- 您的想法（可选）| Your ideas (optional) -->

## 其他说明 | Additional Notes
<!-- 其他信息（可选）| Additional info (optional) -->
```

---

## 📚 资源链接 | Resource Links

- [代码规范指南](https://google.github.io/styleguide/pyguide.html)
- [Git 最佳实践](https://git-scm.com/book/zh/v2)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [如何编写 Git Commit Message](https://chris.beams.io/posts/git-commit/)

---

## 💬 联系方式 | Contact

如果您有任何问题，请随时通过以下方式联系：

If you have any questions, feel free to contact us:

- **GitHub Issues**：技术问题和 bug 报告
- **GitHub Discussions**：一般性讨论
- **邮件**：your-email@example.com

---

<div align="center">

**感谢您的贡献！| Thank you for your contribution!**

</div>
