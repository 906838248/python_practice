# 登录界面——数据库

本项目是数据库课程期末作业的一个部分，用于实现利用数据库存储用户信息并实现用户登录的登录界面。ui采用pysimplegui库。

## 功能说明

- **用户登录**：用户输入用户名和密码，点击登录按钮后验证用户信息是否正确。
- **注册用户**：用户可以点击注册按钮，填写注册信息后注册账号。


## 使用方法

1. 修改`database.py`中的数据库连接信息，将`your_username_here`、`your_password_here`、`your_database`替换为自己的数据库连接信息。
2. 修改`util/login_util.py`中的邮箱和密码，替换为自己的邮箱和密码，注意本项目使用的是qq邮箱需要开启smtp服务。
3. 安装依赖：
```bash
pip install -r requirements.txt
```
4. 运行`main.py`

## 依赖环境

- Python 3.11
- 详细见`requirements.txt`


