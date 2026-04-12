import pyautogui
from tkinter import END

from ui import Win

class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: Win
    def __init__(self):
        pass
    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作
    def input_text(self, event=None):
        try:
            text = self.ui.tk_text_1.get("1.0", END).strip()
        except:
            text = ""
        pyautogui.typewrite(text)
    def input_stick(self, event=None):
        try:
            clipboard_text = self.ui.clipboard_get()
        except:
            clipboard_text = ""
        pyautogui.typewrite(clipboard_text)
