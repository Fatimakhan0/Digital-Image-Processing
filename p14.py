#Program to save an image by pressing a key

import cv2
img=cv2.imread("D:/7086/Resources/flowers.jpg",cv2.IMREAD_COLOR)
cv2.imshow("Image",img)
k=cv2.waitKey(0)
if k==27:  
    # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  
    #wait for 's' key to save and exit
    cv2.imwrite("D:/7086/Outputs/p14.jpg",img)
    cv2.destroyAllWindows()