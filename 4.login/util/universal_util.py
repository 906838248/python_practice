"""
通用工具模块
包含通用的函数，如更新按钮文本和禁用状态。
"""
import time
import PySimpleGUI as psg
def update_button_async(window: psg.Window,key: str,text: str, disabled: bool = False)-> None:
    """
    更新按钮文本和禁用状态
    参数：
        window：窗口对象
        key：按钮键值
        text：按钮文本
        disabled：是否禁用按钮
    """
    for i in range(60, 0, -1):
        window[key].update(f'{i}s 后重试', disabled=disabled)
        time.sleep(1)
    window[key].update(text, disabled=False)
