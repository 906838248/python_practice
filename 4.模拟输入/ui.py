"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import random
from tkinter import *
from tkinter.ttk import *
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_button_input_text = self.__tk_button_input_text(self)
        self.tk_button_input_stick = self.__tk_button_input_stick(self)
        self.tk_label_text = self.__tk_label_text(self)
        self.tk_label_stick = self.__tk_label_stick(self)
        self.tk_text_1 = self.__tk_text_1(self)
    def __win(self):
        self.title("模拟输入")
        # 设置窗口大小、居中
        width = 603
        height = 366
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        
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
    def __tk_button_input_text(self,parent):
        btn = Button(parent, text="输入文本框", takefocus=False,)
        btn.place(x=439, y=186, width=76, height=30)
        return btn
    def __tk_button_input_stick(self,parent):
        btn = Button(parent, text="输入剪切板", takefocus=False,)
        btn.place(x=439, y=245, width=79, height=30)
        return btn
    def __tk_label_text(self,parent):
        label = Label(parent,text="标签",anchor="center", )
        label.place(x=74, y=180, width=64, height=30)
        return label
    def __tk_label_stick(self,parent):
        label = Label(parent,text="标签",anchor="center", )
        label.place(x=66, y=254, width=50, height=30)
        return label
    def __tk_text_1(self,parent):
        text = Text(parent)
        text.place(x=37, y=36, width=514, height=100)
        return text
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
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()