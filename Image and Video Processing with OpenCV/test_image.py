import cv2

img=cv2.imread("galaxy.jpg",0)
print(img.shape)

print(img)
print(img.ndim)

resized_img=cv2.resize(img,(800,800))

cv2.imwrite("resized_img.jpg",resized_img)
cv2.imshow("sample window",resized_img)
cv2.waitKey(2000)
cv2.destroyAllWindows()

print(resized_img.shape)
