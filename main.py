import cv2
import setting
import back_handle

if __name__ == '__main__':
    cap = cv2.VideoCapture(setting.VIDEOCAPTURE)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        _, frame = cap.read()
        cv2.rectangle(frame, (200, 80), (440, 400), (0, 0, 255), 2)

        cv2.imshow("opencv", frame)

        frame2 = back_handle.handle('image/background.jpg', frame[80:400, 200:440])

        # cv2.imshow("opencv", frame2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
