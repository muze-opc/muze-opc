# Changelog

所有重要的项目更新都会记录在这里。

---
## v0.9.0

### Added
- 支持平台选择
- 支持平台 Prompt
- Prompt 模板支持平台变量

## v0.8.0（开发中）

### Added
- 新增 platforms.json
- 新增平台选择菜单
- 支持抖音、视频号、小红书配置

## [v0.6.0] - 2026-07-18

### ✨ 新增（Added）

- 新增 `styles.json` 风格配置文件
- 支持将创作风格从 Python 代码中独立出来
- 支持动态读取 JSON 配置
- 支持菜单自动根据 `styles.json` 显示所有可用风格

### ♻️ 重构（Changed）

- 重构 `prompts.py`
  - 改为读取 `styles.json`
  - 不再使用硬编码风格配置
- 重构 `main.py`
  - 自动读取风格菜单
  - 新增风格无需修改 Python 代码

### ✅ 优化（Improved）

- 项目结构更加模块化
- 提高了后续扩展能力
- 新增创作风格仅需修改配置文件

---

## [v0.5.0] - 2026-07-18

### ✨ 新增（Added）

- 支持多种 AI 创作风格
- 新增：
  - 爆款短视频
  - 故事分享
  - 干货教学
  - 产品测评
  - 木泽OPC 风格

### ♻️ 重构（Changed）

- `build_prompt()` 支持接收风格参数
- `main.py` 增加风格选择菜单

---

## [v0.4.0] - 2026-07-18

### ✨ 新增（Added）

- AI 生成内容自动保存 Markdown
- 自动创建 Output 目录
- 自动按日期和关键词命名文件

---

## [v0.3.0] - 2026-07-17

### ✨ 新增（Added）

- 成功接入 GPT-5.5 API
- 完成 AI Topic Generator
- Prompt 模板生成
- 输出视频标题、Hook、脚本和标签

---

## [v0.2.0] - 2026-07-17

### ✨ 新增（Added）

- 完成项目目录初始化
- 新增：
  - config.py
  - llm.py
  - prompts.py
  - save.py
  - main.py

---

## [v0.1.0] - 2026-07-17

### 🎉 初始版本（Initial Release）

- 初始化 MuzeOPC 项目
- 建立 Git 仓库
- 配置 Python 虚拟环境
- 配置 .env
- 完成基础开发环境