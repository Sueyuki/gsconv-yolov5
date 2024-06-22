import tkinter as tk
from tkinter import messagebox
import time
import threading


def show_terror_message():
    # 等待5秒
    time.sleep(5)

    # 创建一个窗口
    root = tk.Tk()
    root.title("Warning")

    # 设置窗口的大小和颜色
    root.geometry("800x600")
    root.configure(bg='black')

    # 创建一个Label来显示恐怖信息
    label = tk.Label(root, text="You will die...", font=("Helvetica", 40), fg="red", bg="black")
    label.pack(expand=True)

    # 开始死循环打印恐怖信息
    def update_message():
        while True:
            label.config(text="You will die...")
            time.sleep(1)
            label.config(text="...")
            time.sleep(1)

    # 使用线程来运行死循环，以避免阻塞主线程
    t = threading.Thread(target=update_message)
    t.daemon = True
    t.start()

    # 启动主循环
    root.mainloop()


# 运行恐怖信息显示函数
show_terror_message()
