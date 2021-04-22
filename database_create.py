import cv2
import setting
import threading
import back_handle
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

            cv2.rectangle(frame, (200, 80), (440, 400), (0, 0, 255), 2)

            if now == 0:
                cv2.imshow('background', frame)
            else:
                frame = back_handle.handle(frame)
                cv2.imshow('NOW: %d' % now, frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    threading.Thread(target=job).start()


def save():
    global now
    if now == 0:
        cv2.imwrite(setting.BG, frame)
    else:
        cv2.imwrite('database/%d.jpg' % now, frame)
    now += 1


def create():
    win = tk.Tk()
    win.geometry('50x25')

    btn = tk.Button(win, text='擷取', command=save)
    btn.pack()

    start()

    win.mainloop()
