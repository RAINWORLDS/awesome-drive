# 🚀 AwesomeDrive - 开源 1TB 黑科技风格网盘系统

一个炫酷、可扩展、支持多方式登录的免费网盘系统，支持上传、下载、版本控制、回收站、多语言、标签等功能，适合自建和分享。

## ✨ 特性

- 支持电话、邮箱、GitHub 登录
- 文件上传/下载/删除/预览
- 文件夹管理 & 回收站
- 多语言 UI（中文 / English）
- 自动标签 + 文件版本控制
- 进度条、批量上传、打包下载
- 开源、可自由部署扩展

## 🚀 快速开始

```bash
# 安装后端依赖
cd backend
pip install -r requirements.txt
uvicorn app:app --reload

# 前端用浏览器打开 frontend/index.html
🧠 技术栈
前端：HTML + CSS + JavaScript

后端：FastAPI + SQLAlchemy

数据库：SQLite / PostgreSQL

其他：Twilio（短信验证）、SMTP、GitHub OAuth
