import glob2
import cv2

images=glob2.glob("*.jpg")
for image in images:
    #with open(img,'r') as file:
        #data=file.read()
    img=cv2.imread(image,0)
    resized_img=cv2.resize(img,(100,100))
    cv2.imwrite("resized"+image,resized_img)
    cv2.imshow("edited image",resized_img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
    
