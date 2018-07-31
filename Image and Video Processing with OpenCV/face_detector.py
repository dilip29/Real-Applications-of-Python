import cv2
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("news.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

'''
cv2.imshow("gray",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
coordi=face_cascade.detectMultiScale(gray_img,scaleFactor=1.06,minNeighbors=10)

#print(coordi)

for x,y,b,h in coordi:
    img=cv2.rectangle(gray_img,(x,y),(x+b,y+h),(34,139,34),3)

#img=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
img=cv2.resize(img,(int(img.shape[1]),int(img.shape[0])))

cv2.imshow("detector",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
