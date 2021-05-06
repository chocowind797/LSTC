import numpy as np
import imutils
import cv2


def handle(fg, bg):
    bg = cv2.imread(bg)[80:400, 200:440]
    fg = fg[80:400, 200:440]
    # fg = cv2.imread('image/foreground.jpg')

    # 灰度化处理
    bgGray = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)
    fgGray = cv2.cvtColor(fg, cv2.COLOR_BGR2GRAY)

    # 背景减法
    sub = bgGray.astype("int32") - fgGray.astype("int32")
    sub = np.absolute(sub).astype("uint8")
    # cv2.imshow("sub", sub)

    # threshold the image to find regions of the subtracted image with
    # larger pixel differences
    thresh = cv2.threshold(sub, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    cv2.imshow("thresh", thresh)

    # perform a series of erosions and dilations to remove noise
    # erode ,dilate 降噪处理
    # thresh = cv2.erode(thresh, None, iterations=1)
    thresh = cv2.dilate(thresh, None, iterations=3)
    thresh = cv2.erode(thresh, None, iterations=1)
    cv2.imshow("thresh2", thresh)

    # find contours in the thresholded difference map and then initialize
    # 发现边界
    # our bounding box regions that contains the *entire* region of motion
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # 给边界初始值
    (minX, minY) = (np.inf, np.inf)
    (maxX, maxY) = (-np.inf, -np.inf)

    # loop over the contours
    # 循环计算边界
    for c in cnts:
        # compute the bounding box of the contour
        (x, y, w, h) = cv2.boundingRect(c)

        # reduce noise by enforcing requirements on the bounding box size
        # 如果边界值，w 或 w 小于20 就认为是噪音
        if w > 20 and h > 20:
            # update our bookkeeping variables
            minX = min(minX, x)
            minY = min(minY, y)
            maxX = max(maxX, x + w - 1)
            maxY = max(maxY, y + h - 1)

    # draw a rectangle surrounding the region of motion
    # 绘制长方形
    cv2.rectangle(fg, (minX, minY), (maxX, maxY), (0, 255, 0), 2)

    # show the output image
    # 输出图形
    cv2.imshow("Output", fg)
    # cv2.waitKey(0)
    return thresh
