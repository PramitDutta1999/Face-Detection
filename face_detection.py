import cv2

#creating a cascade classifier object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#reading the image as it is
img=cv2.imread("anik_1.jpg")

#reading it as gray image
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#search the co ordinates of image
faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)

print(type(faces))
print(faces)

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("Gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()