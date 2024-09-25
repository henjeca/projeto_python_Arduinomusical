import cv2
import mediapipe as mp
import serial
import time

ser = serial.Serial('COM6', 9600)
time.sleep(2)

video = cv2.VideoCapture(0)

hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

while True:
    check,img = video.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = Hand.process(imgRGB)
    handsPoints = results.multi_hand_landmarks
    h, w, _ = img.shape

    pontos = []



    if handsPoints:

        for points in handsPoints:
            # print(points)
            mpDraw.draw_landmarks(img,points,hand.HAND_CONNECTIONS)

            for id, cord in enumerate(points.landmark):
                cx, cy = int(cord.x*w), int(cord.y*h)
                cv2.putText(img,str(id), (cx, cy+10), cv2.FONT_HERSHEY_SIMPLEX, (0.5),(255, 0 ,0),2)

                pontos.append((cx, cy))

        dedos = [8, 12, 16,20]
        contador=0

        if points:
            if pontos[4][0] < pontos[2][0] and pontos[5][0] < pontos[17][0] :
                contador +=1

            elif pontos[5][0] > pontos[17][0] and pontos[4][0] > pontos[2][0]:
                contador +=1


            for x in dedos:
                if pontos[x][1] < pontos[x - 2][1]:
                    contador += 1



        cv2.putText(img, str(contador), (100,100),cv2.FONT_HERSHEY_SIMPLEX,2

                    ,(255,0,0),5)

        print(contador)
        ser.write(str(contador).encode())

    else:
        contador = 0
        ser.write(str(contador).encode())

    cv2.imshow("imagem", img)

    cv2.waitKey(1)