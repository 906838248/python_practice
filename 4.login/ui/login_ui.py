"""
登录窗口
包含邮箱和密码输入框，以及登录和取消按钮。
"""
import PySimpleGUI as psg
from util.login_util import *
from util.universal_util import update_button_async
from ui.universal_ui import message_window
import threading
import time

# 设置字体和主题
psg.set_options(font=('Arial Bold', 16))
psg.theme('SystemDefaultForReal')


def login_window():
    """
        layout:登录窗口布局
        控件：
        Column:列布局，用于垂直排列控件
            pad:控件间距
            element_justification:控件对齐方式
        Text:文本标签
            size:文本大小
        Input:输入框
            expand_x:是否水平扩展
            password_char:密码字符，用于隐藏输入
        Push:弹簧，用于调整控件间距
        OK:登录按钮
        Cancel:取消按钮
    """
    layout = [

       [psg.Column([[psg.Text('邮箱 '), psg.Input(expand_x=True,pad=(30,0))]],         
                pad=(0,0), element_justification='left')],
       [psg.Column([[psg.Text('密码 '), psg.Input(expand_x=True, password_char='*',pad=(30,0))]], 
                pad=(0,0), element_justification='left')],
        [psg.Push(),psg.OK('登录'), psg.Cancel('取消'),psg.Button('注册'),psg.Push()]
    ]
    # 创建窗口
    window = psg.Window('错题本', layout, size=(450,150))
    # 事件循环
    while True:
        # 读取事件和值
        event, values = window.read()
        # 处理事件

        # 注册按钮事件处理
        if event == '注册':
            window.hide()
            register_window()
            window.un_hide()
            continue
        # 退出登录窗口
        if event == psg.WINDOW_CLOSED or event == '取消':
            break
        # 登录
        if event == '登录':
            email = values[0]
            password = values[1]
            # 验证登录信息
            if validate_login(email, password):
                # 登录成功，关闭窗口
                window.close()
                message_window('登录成功！')
                break
            else:
                message_window('登录失败！')
                continue

    # 关闭窗口
    window.close()

def register_window():
    """
    注册窗口
    包含邮箱和密码输入框，以及注册和取消按钮。
    """
    layout = [

        [psg.Column([[psg.Text('邮箱 ', size='70'), psg.Input(expand_x=True,key='邮箱')]],         
                pad=(0,0), element_justification='left')],
        [psg.Column([[psg.Text('用户名 ', size='70'), psg.Input(expand_x=True,key='用户名')]],         
                pad=(0,0), element_justification='left')],
        [psg.Column([[psg.Text('密码 ', size='70'), psg.Input(expand_x=True, password_char='*',key='密码')]], 
                pad=(0,0), element_justification='left')],
        [psg.Column([[psg.Text('确认密码 ', size='70'), psg.Input(expand_x=True, password_char='*',key='确认密码')]],  
                pad=(0,0), element_justification='left')],
        [psg.Column([[psg.Text('验证码 ', size='70'), psg.Input(expand_x=True,key='验证码')]], 
                pad=(0,0), element_justification='left')],
        [psg.Push(),psg.OK('注册'), psg.Cancel('取消'),psg.Button('获取验证码',key='获取验证码'),psg.Push()]
    ]
    # 创建窗口
    window = psg.Window('注册', layout, size=(450,250))
    # 事件循环
    while True:
       
        # 读取事件和值
        event, values = window.read()
        if event == psg.WINDOW_CLOSED or event == '取消':
            break

        email = values['邮箱']
        username = values['用户名']
        password = values['密码']
        confirm_password = values['确认密码']
        user_code = values['验证码']
        # 处理事件
        if event == '获取验证码':
            # 验证邮箱格式
            if not check_email(email):
                continue
            # 发送验证码到邮箱
            threading.Thread(target=send_verify_code, args=(email,),daemon=True).start()
            message_window(f'验证码已发送')
            # 禁用获取验证码按钮
            threading.Thread(target=update_button_async, args=(window,'获取验证码','获取验证码',True),daemon=True).start()

            continue
        if event == '注册':
            # 注册用户
            if not register_user(email, username, password, confirm_password, user_code):
                continue
            break
    # 关闭窗口
    window.close()
       

if __name__ == '__main__':
    login_window()