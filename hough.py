import cv2
import numpy as np

img = cv2.imread('abc.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

lines = cv2.HoughLines(edges,1,np.pi/180,200)

i=0
j=0

for line in lines:
	for rho,theta in line:
		a = np.cos(theta)
		b = np.sin(theta)
		x0 = a*rho
		y0 = b*rho
		x1 = int(x0 + 1000*(-b))
		y1 = int(y0 + 1000*(a))
		x2 = int(x0 - 1000*(-b))
		y2 = int(y0 - 1000*(a))
		#print x1
		#print x2
		#print abs(x1-x2)
		if abs(x1 - x2) < 50:
			i += 1
			print 'Vertical Line ' + repr(i)
			print repr(x1) + ' ' + repr(y1)
			print repr(x2) + ' ' + repr(y2)
			print abs(x1 - x2)
			cv2.line(img,(x1,y1),(x2,y2),(0,0,255),1)
		if abs(y1 - y2) < 50:
			j += 1
			print 'Horizontal Line ' + repr(j)
			print repr(x1) + ' ' + repr(y1)
			print repr(x2) + ' ' + repr(y2)
			print abs(y1 - y2)
			cv2.line(img,(x1,y1),(x2,y2),(0,255,0),1)	
		# else:
			# print "here";


# for rho,theta in lines[0]:
	# a = np.cos(theta)
	# b = np.sin(theta)
	# x0 = a*rho
	# y0 = b*rho
	# x1 = int(x0 + 1000*(-b))
	# y1 = int(y0 + 1000*(a))
	# x2 = int(x0 - 1000*(-b))
	# y2 = int(y0 - 1000*(a))
	# cv2.line(img,(x1,y1),(x2,y2),(0,0,255),1)

# for rho,theta in lines[1]:
	# a = np.cos(theta)
	# b = np.sin(theta)
	# x0 = a*rho
	# y0 = b*rho
	# x1 = int(x0 + 1000*(-b))
	# y1 = int(y0 + 1000*(a))
	# x2 = int(x0 - 1000*(-b))
	# y2 = int(y0 - 1000*(a))
	# cv2.line(img,(x1,y1),(x2,y2),(0,0,255),1)

# for rho,theta in lines[2]:
	# a = np.cos(theta)
	# b = np.sin(theta)
	# x0 = a*rho
	# y0 = b*rho
	# x1 = int(x0 + 1000*(-b))
	# y1 = int(y0 + 1000*(a))
	# x2 = int(x0 - 1000*(-b))
	# y2 = int(y0 - 1000*(a))
	# cv2.line(img,(x1,y1),(x2,y2),(0,0,255),1)

cv2.imwrite('houghlinesABC.jpg',img)