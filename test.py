import cv2 as cv

imread = cv.imread("D:/Users/admin/Desktop/opcv_code/image/pycharm_git_013.jpg")

cv.namedWindow("图片",cv.WINDOW_AUTOSIZE)
cv.imshow("图片",imread)
print('图片')
cv.waitKey(0)
cv.destroyAllWindows()