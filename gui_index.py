import tkinter as tk
from tkinter import filedialog
from  host_file_util import moveHost
from file import  openFile
import os.path
def select_file():

    home = os.path.expanduser("~")

    initialdir = os.path.join(home,"Documents") +"\hosts"
    if not os.path.exists(initialdir):
        os.makedirs(initialdir)
    else:
        print("is exists !")
    filetypes = (
        ('text files', '*.*'),
        ('All files', '*.*')
    )
    filename = filedialog.askopenfilename(
        title=' Select host file !',
        initialdir=initialdir,
        filetypes=filetypes)
    if filename:
        moveHost(filename)
    openFile("C:\Windows\System32\drivers\etc\hosts")



root = tk.Tk()
root.withdraw()  # 隐藏主窗口

select_file()  # 调用函数打开文件选择对话框