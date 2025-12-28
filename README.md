# Hz Blog Project

一个基于 Django 的博客系统，支持用户注册、登录、创建和管理博客文章。

![爱丽丝](Sample Image/alice3.png)

## 项目链接

- GitHub: https://github.com/Hor1zen/homework4_blog

## 功能特性

- 用户注册和登录系统
- 博客文章的创建、编辑和删除
- 搜索功能（支持按标题搜索）
- 权限控制（用户只能编辑和删除自己的文章）
- Markdown 支持（支持代码块、表格、任务列表、删除线等）
- 响应式设计，支持移动端浏览
- 分页功能
- 字数限制显示（标题最多30字符，内容最多10000字符）
- 自动文本框高度扩展
- GitHub 链接展示

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

由于本项目已包含所有的数据库迁移文件（Migrations），你只需直接运行迁移命令来生成本地数据库：

```bash
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
4. 在主页可以看到所有博客文章，搜索框支持按标题搜索
5. 只有文章的作者才能编辑或删除自己的文章

## 项目结构

```
Blog/                    # Django 项目配置
├── asgi.py              # ASGI 配置
├── settings.py          # 项目设置（包含数据库、静态文件、中间件等配置）
├── urls.py             # 项目根 URL 配置
└── wsgi.py             # WSGI 配置
blogs/                   # 博客应用
├── migrations/         # 数据库迁移文件
│   ├── 0001_initial.py # 初始迁移文件
│   ├── 0002_blogpost_owner.py # 添加文章所有者字段的迁移
│   └── 0003_alter_blogpost_title.py # 修改标题字段长度的迁移
├── templates/blogs/    # 博客应用模板文件
│   ├── base.html       # 基础模板（包含导航栏、样式等）
│   ├── edit_post.html  # 编辑文章页面
│   ├── index.html      # 主页（包含文章列表、搜索功能、分页等）
│   ├── new_post.html   # 新建文章页面
│   └── not_owner.html  # 权限不足提示页面
├── admin.py            # 管理后台配置
├── apps.py             # 应用配置
├── forms.py            # 表单定义（包含标题和内容字段）
├── models.py           # 数据模型（BlogPost 模型）
├── tests.py            # 测试文件
├── urls.py             # 博客应用 URL 配置
├── views.py            # 视图函数（包含主页、新建、编辑、删除文章等逻辑）
└── static/             # 静态文件（如需要可创建）
users/                   # 用户认证应用
├── templates/          # 用户认证相关模板
│   ├── registration/   # Django 内置认证模板
│   │   └── login.html  # 登录页面
│   └── users/          # 自定义用户模板
│       └── register.html # 注册页面
├── admin.py            # 用户管理后台配置
├── apps.py             # 用户应用配置
├── models.py           # 用户模型（使用 Django 内置 User 模型）
├── tests.py            # 用户应用测试
├── urls.py             # 用户应用 URL 配置
├── views.py            # 用户视图函数（包含注册逻辑）
└── static/             # 用户相关静态文件（如需要可创建）
static/js/              # 公共静态文件
└── form_utils.js       # 表单相关的 JavaScript 工具函数（包含字数统计、自动扩展等功能）
README.md              # 项目说明文档
manage.py              # Django 管理命令工具
requirements.txt       # 项目依赖清单
.gitignore             # Git 忽略配置
db.sqlite3             # SQLite 数据库文件（运行后生成）
```

## 许可证

MIT License
