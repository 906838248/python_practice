import pyautogui
import keyboard
import ctypes
from ctypes import wintypes
from tkinter import END
from ui import Win

# Windows API 常量
KEYEVENTF_UNICODE = 0x0004
KEYEVENTF_KEYUP = 0x0002

class Controller:
    ui: Win
    
    def __init__(self):
        # 获取SendInput函数
        self.SendInput = ctypes.windll.user32.SendInput
        self.PUL = ctypes.POINTER(ctypes.c_ulong)
        
        class KeyBdInput(ctypes.Structure):
            _fields_ = [
                ("wVk", wintypes.WORD),
                ("wScan", wintypes.WORD),
                ("dwFlags", wintypes.DWORD),
                ("time", wintypes.DWORD),
                ("dwExtraInfo", self.PUL)
            ]
        
        class INPUT(ctypes.Structure):
            _fields_ = [
                ("type", wintypes.DWORD),
                ("ki", KeyBdInput),
                ("padding", ctypes.c_ubyte * 8)
            ]
        
        self.INPUT = INPUT
        self.KeyBdInput = KeyBdInput

    def _send_unicode_char(self, char):
        """发送单个Unicode字符"""
        scan_code = ord(char)
        
        extra = ctypes.c_ulong(0)
        ii_ = self.KeyBdInput(0, scan_code, KEYEVENTF_UNICODE, 0, ctypes.pointer(extra))
        x = self.INPUT(ctypes.c_ulong(1), ii_)
        self.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))
        
        # 释放按键
        ii_ = self.KeyBdInput(0, scan_code, KEYEVENTF_UNICODE | KEYEVENTF_KEYUP, 0, ctypes.pointer(extra))
        x = self.INPUT(ctypes.c_ulong(1), ii_)
        self.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

    def _send_unicode_text(self, text):
        """发送Unicode文本（支持中文）"""
        for char in text:
            self._send_unicode_char(char)
            # 添加小延迟，避免输入太快
            pyautogui.sleep(0.01)

    def init(self, ui):
        self.ui = ui
        # 注册热键
        keyboard.add_hotkey('F8', self.input_text)
        keyboard.add_hotkey('F9', self.input_stick)
        # 不拦截热键事件，避免影响其他应用
        keyboard._listener.suppress_key_events = False
        # 注册窗口关闭事件
        self.ui.protocol("WM_DELETE_WINDOW", self._on_close)

    # 窗口关闭事件处理函数
    def _on_close(self):
        keyboard.unhook_all_hotkeys()
        self.ui.destroy()

    # 输入文本（支持中文）
    def input_text(self, event=None):
        current_focus = self.ui.focus_get()
        try:
            text = self.ui.tk_text_1.get("1.0", END).strip()
        except:
            text = ""
        
        if text:
            self._send_unicode_text(text)
        
        if current_focus:
            current_focus.focus_set()
    
    # 粘贴剪贴板（支持中文）
    def input_stick(self, event=None):
        current_focus = self.ui.focus_get()
        try:
            clipboard_text = self.ui.clipboard_get()
        except:
            clipboard_text = ""
        
        if clipboard_text:
            self._send_unicode_text(clipboard_text)
        
        if current_focus:
            current_focus.focus_set()
