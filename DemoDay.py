import cv2
import imutils
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture("Resources/test4.mp4")


while True:
    count = 0
    success, img = cap.read()
    img = imutils.resize(img,width=720,height=480)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray)
    for(x, y, w, h) in faces:
        count += 1
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (50,50)
        fontScale = 100
        color = (0,0,0)
        thickness = 2
        imgGray = cv2.putText(img,'OpenCv',org,font,fontScale,color,thickness,cv2.LINE_AA)
    cv2.imshow("Video", img)
    print(count)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
