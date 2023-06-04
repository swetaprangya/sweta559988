import cv2

img=cv2.imread("solar-system.jpg")
cv2.imshow("Display Image",img)
cv2.waitKey(0)
cv2.putText(img,"sun"(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"macury"(30,400),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"venus"(40,500),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"earth"(50,600),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"mars"(60,700),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"jupiter"(70,800),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"saturn"(80,900),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"uranus"(90,1000),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"neputune"(100,1100),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
