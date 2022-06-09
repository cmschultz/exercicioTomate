import cv2 as cv
import numpy as np

tomate = cv.imread('./imagens/tomate.jpg')

hsv_tomate = cv.cvtColor(tomate, cv.COLOR_BGR2HSV)
lowRedFilter = cv.inRange(hsv_tomate, (0, 50, 200), (10, 255, 255))
highRedFilter = cv.inRange(hsv_tomate, (160, 50, 200), (179, 255, 255))
redSelect = cv.add(lowRedFilter, highRedFilter)

tomateSolo = cv.bitwise_and(tomate, tomate, mask=redSelect)

cv.imshow('tomate', tomateSolo)
cv.waitKey(0)
cv.destroyAllWindows()