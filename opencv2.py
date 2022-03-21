import cv2
import time

cap = cv2.VideoCapture(0)  # 调用第一个摄像头
cv2.namedWindow('v')
# 人脸特征分类器
face_cascade = cv2.CascadeClassifier('D:\python\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
# 循环识别
while True:
    ret, frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, 1.3, 5)
    # 人脸处理，画矩形图像
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # 显示图像以及窗口关闭
    cv2.imshow('人脸识别', frame)
    flag = cv2.waitKey(1)
    if flag == 27:#按下ESC键退出
            break
# 销毁窗口
cv2.destroyAllWindows()    #实现摄像头实时识别



