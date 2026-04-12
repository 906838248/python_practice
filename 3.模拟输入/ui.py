import random
import tkinter as tk
from tkinter import *
from tkinter.ttk import *

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_title = self.__tk_label_title(self)
        self.tk_text_1 = self.__tk_text_1(self)
        self.tk_label_text = self.__tk_label_text(self)
        self.tk_button_input_text = self.__tk_button_input_text(self)
        self.tk_label_stick = self.__tk_label_stick(self)
        self.tk_button_input_stick = self.__tk_button_input_stick(self)
    def __win(self):
        self.title("模拟输入")
        width = 650
        height = 420
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        self.configure(bg='#f0f0f0')
        
        self.canvas_decoration = Canvas(self, width=650, height=3, bg='#1976D2', 
                                        highlightthickness=0, cursor='none')
        self.canvas_decoration.place(x=0, y=55)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    
    def __tk_label_title(self, parent):
        label = tk.Label(parent, text="📝 模拟输入助手", font=("Microsoft YaHei", 18, "bold"), 
                        bg='#2196F3', fg='white', anchor="center", pady=15)
        label.pack(fill='x')
        return label
    
    def __tk_text_1(self,parent):
        text_frame = tk.Frame(parent, bg='#ffffff', bd=2, relief='groove')
        text_frame.place(x=40, y=70, width=560, height=110)
        
        text = Text(text_frame, font=("Microsoft YaHei", 12), relief='flat', 
                   padx=10, pady=10, wrap='word')
        text.pack(fill='both', expand=True)
        
        return text
    
    def __tk_label_text(self,parent):
        label = tk.Label(parent, text="文本输入", font=("Microsoft YaHei", 11), 
                        bg='#f0f0f0', fg='#333333', anchor="w")
        label.place(x=40, y=195, width=80, height=25)
        return label
    
    def __tk_button_input_text(self,parent):
        btn = tk.Button(parent, text="▶ 输入文本  (F8)", takefocus=False,
                       bg='#4CAF50', fg='white', font=("Microsoft YaHei", 9, "bold"),
                       relief='flat', cursor='hand2')
        btn.place(x=130, y=193, width=170, height=30)
        self.__bind_hover_effect(btn, '#45a049', '#4CAF50')
        return btn
    
    def __tk_label_stick(self,parent):
        label = tk.Label(parent, text="剪切板输入", font=("Microsoft YaHei", 11), 
                        bg='#f0f0f0', fg='#333333', anchor="w")
        label.place(x=40, y=240, width=90, height=25)
        return label
    
    def __tk_button_input_stick(self,parent):
        btn = tk.Button(parent, text="📋 输入剪切板  (F9)", takefocus=False,
                       bg='#2196F3', fg='white', font=("Microsoft YaHei", 9, "bold"),
                       relief='flat', cursor='hand2')
        btn.place(x=130, y=238, width=185, height=30)
        self.__bind_hover_effect(btn, '#1976D2', '#2196F3')
        return btn
    
    def __bind_hover_effect(self, btn, hover_color, normal_color):
        def on_enter(e):
            btn.configure(bg=hover_color)
        def on_leave(e):
            btn.configure(bg=normal_color)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    def __event_bind(self):
        self.tk_button_input_text.bind('<Button-1>',self.ctl.input_text)
        self.tk_button_input_stick.bind('<Button-1>',self.ctl.input_stick)
        pass
    def __style_config(self):
        self.tk_tip_label = tk.Label(self, 
                                    text="💡 提示：在上方输入文本后，点击按钮或使用快捷键即可自动输入内容", 
                                    font=("Microsoft YaHei", 9), 
                                    bg='#FFFDE7', fg='#F57C00', 
                                    anchor="w", padx=10, pady=8,
                                    bd=1, relief='solid')
        self.tk_tip_label.place(x=40, y=290, width=570, height=35)
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()