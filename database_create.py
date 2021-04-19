import cv2
import setting
import threading
import tkinter as tk

frame = 0
now = 0


def start():
    def job():
        global frame
        cap = cv2.VideoCapture(setting.VIDEOCAPTURE)

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        while True:
            _, frame = cap.read()
            cv2.imshow('NOW: 第 %d 張' % now, frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    threading.Thread(target=job).start()


def save():
    global now
    cv2.imwrite('database/%d.jpg' % now, frame)
    now += 1


def create():
    win = tk.Tk()

    btn = tk.Button(win, text='擷取', command=save)
    btn.pack()

    start()

    win.mainloop()
