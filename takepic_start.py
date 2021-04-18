import tkinter as tk
import cv2
import setting
import threading
import database_create

from PIL import ImageTk, Image

frame = 0

if __name__ == '__main__':
    win = tk.Tk()
    win.title('初始設定')
    win.geometry('640x480')

    # ================================Img===============================

    def image():
        cap = cv2.VideoCapture(setting.VIDEOCAPTURE)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        def video_button():
            global frame
            ret, frame = cap.read()
            if ret:
                video_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img_frame = ImageTk.PhotoImage(Image.fromarray(video_frame))
                image_canvas.create_image(0, 0, anchor='nw', image=img_frame)
                image_canvas.img = img_frame
            cap.release()
        video_button()


    # 建立canvas 顯示圖片
    image_canvas = tk.Canvas(win, bg='#333f50', height=500, width=640)
    image_canvas.pack()

    # ================================Menu===============================
    menu = tk.Menu(win)
    win.config(menu=menu)

    menu.add_command(label='擷取', command=lambda: threading.Thread(target=image).start())
    menu.add_command(label='完成', command=lambda: cv2.imwrite('image/background.jpg', frame))
    menu.add_command(label='開始')
    menu.add_command(label='資料庫創建', command=lambda: database_create.create())

    win.mainloop()
