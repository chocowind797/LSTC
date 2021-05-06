import tkinter as tk
import main
import setting
import database_create
from tkinter import messagebox


def test():
    print(setting.VIDEOCAPTURE)
    print(setting.ACCURACY)


def button_set_click():
    setting.VIDEOCAPTURE = choice.get()
    setting.ACCURACY = int(accuracy.get()) / 100.0

    if setting.VIDEOCAPTURE == choice.get() and setting.ACCURACY == int(accuracy.get()) / 100.0:
        messagebox.showinfo(title='提示', message='設定成功')


if __name__ == '__main__':
    win = tk.Tk()
    win.title('初始設定')
    win.geometry('580x400')

    # ================================Menu===============================
    menu = tk.Menu(win)
    win.config(menu=menu)

    menu.add_command(label='資料庫創建', command=lambda: database_create.create())

    # ===========================camera choose===========================
    frame_cam = tk.Frame(win)
    frame_cam.pack()

    label_cam = tk.Label(frame_cam, text='鏡頭:  ', font=('Arial', 20))

    choice = tk.IntVar()
    radiobutton0 = tk.Radiobutton(frame_cam, text='電腦自帶', variable=choice, value=0, font=('Arial', 20))
    radiobutton1 = tk.Radiobutton(frame_cam, text='其他鏡頭', variable=choice, value=1, font=('Arial', 20))

    label_cam.pack(side=tk.LEFT)
    radiobutton0.pack(side=tk.LEFT)
    radiobutton1.pack(side=tk.LEFT)

    # ==============================accuracy=============================
    frame_accuracy = tk.Frame(win)
    frame_accuracy.pack()

    label_accuracy = tk.Label(frame_accuracy, text='精準度:  ', font=('Arial', 20))
    label_percent = tk.Label(frame_accuracy, text='%', font=('Arial', 20))

    accuracy = tk.DoubleVar()
    spinbox_accuracy = tk.Spinbox(frame_accuracy, from_=1, to=100, font=('Arial', 20), width=10, textvariable=accuracy)
    accuracy.set(int(setting.ACCURACY*100))

    label_accuracy.pack(side=tk.LEFT)
    spinbox_accuracy.pack(side=tk.LEFT)
    label_percent.pack(side=tk.LEFT, ipadx=10)

    # ===============================Button==============================
    frame_set = tk.Frame(win)
    frame_set.pack(side=tk.BOTTOM, ipady=20)

    button_set = tk.Button(frame_set, text='設定', command=button_set_click, font=('Arial', 20))
    button_start = tk.Button(frame_set, text='開始', command=main.run, font=('Arial', 20))

    button_set.pack(side=tk.LEFT, padx=30)
    button_start.pack(side=tk.RIGHT, padx=30)

    win.mainloop()
