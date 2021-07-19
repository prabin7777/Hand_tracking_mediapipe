import cv2 as cv
import mediapipe as mp
mphands=mp.solutions.hands
hands=mphands.Hands()
mpDraw=mp.solutions.drawing_utils
cap=cv.VideoCapture(0)
while True:
    ret,frame=cap.read()
    imagergb=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    result=hands.process(imagergb)

    cv.waitKey(1)
    print(result.multi_hand_landmarks)
    if result.multi_hand_landmarks:
        for i in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, i, mphands.HAND_CONNECTIONS)
            for id,lm in enumerate(i.landmark):

                h,w,c=frame.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                print(cx,cy)
                if(id==any):
                    cv.circle(frame,(cx,cy),10,(255,0,0),cv.FILLED)




    cv.imshow("hello", frame)