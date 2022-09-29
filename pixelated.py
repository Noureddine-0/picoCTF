# IF YOU HAVEN'T ALREADY INSTALLED THE CV2 LIBRARY YOU CAN INSTALL IT USING THE FOLLOWING COMMAND IN YOUR TEMINAL :
# pip3 install opencv-python


import cv2 
im1=cv2.imread('scrambled1.png')
im2=cv2.imread('scrambled2.png')
im=im1 + im2 

cv2.imshow("added",im)

cv2.waitKey(0)
cv2.destroyAllWindows()
