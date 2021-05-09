import cv2
import setting
import back_handle
import similarity_check


def check(frame):
    i = 0
    for i in range(1, 11):
        num = similarity_check.runAllImageSimilaryFun(frame, "database/%d.jpg" % i)
        if num:
            return i
    return 0


def run():
    cap = cv2.VideoCapture(setting.VIDEOCAPTURE)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        _, frame = cap.read()
        cv2.rectangle(frame, (200, 80), (440, 400), (0, 0, 255), 2)

        cv2.imshow("opencv", frame)

        frame2 = back_handle.handle(frame, setting.BG_RAW)

        cv2.imshow("opencv", frame)

        if frame2 is not None:
            num = check(frame2)
            cv2.imshow("handle", frame2)
            if num != 0:
                break
            print(num)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
