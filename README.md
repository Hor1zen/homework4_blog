# Hz Blog Project

一个基于 Django 的博客系统，支持用户注册、登录、创建和管理博客文章。

## 项目链接

- GitHub: https://github.com/Hor1zen/homework4_blog

## 功能特性

- 用户注册和登录系统
- 博客文章的创建、编辑和删除
- 搜索功能（支持按标题和用户名搜索）
- 权限控制（用户只能编辑和删除自己的文章）
- Markdown 支持（支持代码块、表格、任务列表等）
- 响应式设计，支持移动端浏览
- 分页功能

## 依赖项

- Python 3.11.9
- Django==4.2.27
- django-bootstrap5==25.3
- django-markdownify==0.9.6
- pymdown-extensions==10.19.1

## 环境要求

- Python 3.11.9
- pip

## 本地部署和运行

### 1. 克隆项目

```bash
git clone https://github.com/Hor1zen/homework4_blog.git
cd homework4_blog
```

### 2. 创建虚拟环境

```bash
python -m venv venv
```

### 3. 激活虚拟环境

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. 安装依赖

```bash
pip install -r requirements.txt
```

### 5. 数据库迁移

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. 创建超级用户（可选）

```bash
python manage.py createsuperuser
```

### 7. 运行开发服务器

```bash
python manage.py runserver
```

服务器将在 `http://127.0.0.1:8000/` 上运行。

## 使用说明

1. 访问 `http://127.0.0.1:8000/` 进入博客主页
2. 点击右上角的"注册"创建账户，或使用已有账户"登录"
3. 登录后可以点击"+ 写文章"创建新博客
4. 在主页可以看到所有博客文章，搜索框支持按标题或用户名搜索
5. 只有文章的作者才能编辑或删除自己的文章

## 项目结构

```
Blog/           # Django 项目配置
blogs/          # 博客应用
├── migrations/ # 数据库迁移文件
├── templates/  # 模板文件
└── static/     # 静态文件（如需要可创建）
users/          # 用户认证应用
├── migrations/ # 数据库迁移文件
├── templates/  # 模板文件
└── static/     # 静态文件（如需要可创建）
```

## 许可证

MIT License