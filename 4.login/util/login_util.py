"""
登录工具模块
包含登录验证和验证码发送功能。
"""
from database import db_connect
import smtplib
from email.mime.text import MIMEText
import random
from ui.universal_ui import message_window

SENDER_EMAIL = 'your_email_here'
SENDER_PASSWORD = 'your_password_here'


def validate_login(email: str, password: str) -> bool:
    """
    验证登录信息
    参数：
        email：用户邮箱
        password：用户密码
    返回值：
        True：登录成功
        False：登录失败
    """
    # 验证登录信息
    # 连接数据库
    db = db_connect()
    cursor = db.cursor()
    sql = "SELECT * FROM user WHERE email = %s AND password = %s AND password IS NOT NULL"
    cursor.execute(sql, (email, password))
    db.close()
    # 检查查询结果是否为空
    result = cursor.fetchall()

    if result:
        return True
    else:
        return False

def send_verify_code(email: str) -> int:
    """
    发送验证码到邮箱
    参数：
        email：用户邮箱
    返回值：
        verify_code：验证码
    """
    # 生成验证码
    verify_code = random.randint(1000, 9999)
    # 更新数据库中的验证码
    db = db_connect()
    cursor = db.cursor()
    sql = "INSERT INTO user (email, verify_code) VALUES (%s, %s) ON DUPLICATE KEY UPDATE verify_code = %s"
    cursor.execute(sql, (email, verify_code, verify_code))
    db.commit()
    db.close()


    # 发送验证码到邮箱

    # 构建邮件内容
    msg = MIMEText(f'你的验证码是：{verify_code}', 'plain', 'utf-8')
    # 设置邮件头
    msg['From'] = SENDER_EMAIL
    # 设置收件人邮箱
    msg['To'] = email
    # 设置邮件主题
    msg['Subject'] = '验证码'
    # 发送邮件
    with smtplib.SMTP('smtp.qq.com', 587) as server:
        # 启用TLS加密
        server.starttls()
        # 登录邮箱
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        # 发送邮件
        server.sendmail(SENDER_EMAIL, email, msg.as_string())
    return verify_code
    
def check_email(email: str) -> bool:
    """
    检查邮箱是否存在
    参数：
        email：用户邮箱
    返回值：
        True：邮箱存在
        False：邮箱不存在
    """
    # 检查邮箱是否存在
    db = db_connect()
    cursor = db.cursor()
    sql = "SELECT password FROM user WHERE email = %s AND password IS NOT NULL"
    cursor.execute(sql, (email,))
    # 检查查询结果是否为空
    result = cursor.fetchall()
    db.close()
    if result:
        message_window(f'邮箱已存在')
        return False
    else:
        if('@' in email and '.com' in email):
            return True
        else:
            message_window(f'邮箱格式错误')
            return False

def register_user(email: str, username: str, password: str, confirm_password: str, user_code: str) -> bool:
    """
    注册用户
    参数：
        email：用户邮箱
        username：用户名
        password：用户密码
        confirm_password：确认密码
        user_code：用户输入的验证码
    返回值：
        True：注册成功
        False：注册失败
    """
    # 获取数据库中的验证码
    db = db_connect()
    cursor = db.cursor()
    sql = "SELECT verify_code FROM user WHERE email = %s AND verify_code IS NOT NULL"
    cursor.execute(sql, (email,))
    result = cursor.fetchall()
    db.close()
    if not check_email(email):
        return False
    if not result:
        message_window('请获取验证码')
        return False
    verify_code = result[0][0]
    print(verify_code)
    # 验证验证码
    if verify_code != user_code:
        message_window('验证码错误')
        return False

    # 验证密码是否一致
    if not password:
        message_window('密码不能为空')
        return False
    if not confirm_password:
        message_window('确认密码不能为空')
        return False
    if password != confirm_password:
        message_window('两次输入密码不一致')
        return False
    
    if not username:
        message_window('用户名不能为空')
        return False

    # 注册用户
    db = db_connect()
    cursor = db.cursor()
    sql = "UPDATE user SET password = %s, verify_code = NULL, username = %s WHERE email = %s"
    cursor.execute(sql, (password, username, email))
    db.commit()
    db.close()
    message_window('注册成功')
    return True

