"""
通用UI模块
包含通用的UI组件，如消息框。
"""
import PySimpleGUI as psg

def message_window(message: str, title: str = '消息')-> None:
    """
    显示消息框
    参数：
        title：消息框标题
        message：消息框内容
    """
    layout = [
        [psg.Push(), psg.Text(message), psg.Push()],
        [psg.Push(), psg.Button('确定'), psg.Push()]
        ]
    window = psg.Window(title, layout, size=(200, 100))
    while True:
        event, values = window.read()
        if event == psg.WINDOW_CLOSED:
            break
        if event == '确定':
            break
    window.close()
            
