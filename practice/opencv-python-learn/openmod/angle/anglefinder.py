# import cv2 as cv
# import math
# path = 'im.png'
# img = cv.imread(path)
# pointList = []
# def mousepoints(event,x,y,flags,params):
#     size = len(pointList)
#     if size != 0 and size %3 !=0:
#         cv.line(img,tuple(pointList[round((size-1)/3)*3]) ,(x,y),(0,255,0),2)
#     if event == cv.EVENT_LBUTTONDOWN:
#         cv.circle(img,(x,y),5,(0,0,255),cv.FILLED)
#         pointList.append([x,y])
    
# def gradient(pt1,pt2):
#     return (pt2[1]-pt1[1]/pt2[0]-pt1[0])
# def getAngle(pointList):
#     pt1,pt2,pt3 = pointList[-3:]
#     m1 = gradient(pt1,pt2)
#     m2 = gradient(pt1,pt3)
#     angR = math.atan((m2-m1)/(1+(m2*m1)))
#     angD = round(math.degrees(angR))
#     # print(angD)
#     cv.putText(img,str(angD),(pt1[0]-40,pt1[1]-20),cv.FONT_HERSHEY_COMPLEX,1.5,(0,255,0),2)

    
# while True:
#     if len(pointList) % 3 ==0 and len(pointList) !=0:
#         getAngle(pointList)
#     cv.imshow("image",img)
#     cv.setMouseCallback('image',mousepoints)
#     if cv.waitKey(1) & 0xFF == ord('c'):
#         pointList = []
#         img = cv.imread(path)
#     elif cv.waitKey(1) & 0xFF == ord('q'):
#         break


import cv2
import math

path = 'im.png'
img = cv2.imread(path)
pointsList = []

def mousePoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size = len(pointsList)
        if size != 0 and size % 3 != 0:
            cv2.line(img,tuple(pointsList[round((size-1)/3)*3]),(x,y),(0,0,255),2)
        cv2.circle(img,(x,y),5,(0,0,255),cv2.FILLED)
        pointsList.append([x,y])

def gradient(pt1,pt2):
    return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])

def getAngle(pointsList):
    pt1, pt2, pt3 = pointsList[-3:]
    m1 = gradient(pt1,pt2)
    m2 = gradient(pt1,pt3)
    angR = math.atan((m2-m1)/(1+(m2*m1)))
    angD = round(math.degrees(angR))
    print(angD)
    cv2.putText(img,str(angD),(pt1[0]-40,pt1[1]-20),cv2.FONT_HERSHEY_COMPLEX,
                1.5,(0,0,255),2)


while True:
    if len(pointsList) % 3 == 0 and len(pointsList) !=0:
        getAngle(pointsList)


    cv2.imshow('Image',img)
    cv2.setMouseCallback('Image',mousePoints)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        pointsList = []
        img = cv2.imread(path)









# import cv2 as cv
# import math

# path = 'im.png'
# img = cv.imread(path)
# pointList = []

# def mousepoints(event, x, y, flags, params):
#     if event == cv.EVENT_LBUTTONDOWN:
#         cv.circle(img, (x, y), 5, (0, 0, 255), cv.FILLED)
#         pointList.append([x, y])
#         print(pointList)

# def gradient(pt1, pt2):
#     if pt2[0] - pt1[0] == 0:
#         return float('inf')
#     return (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])

# def getAngle(pointList):
#     pt1, pt2, pt3 = pointList[-3:]
    
#     # Vectors
#     v1 = [pt1[0] - pt2[0], pt1[1] - pt2[1]]
#     v2 = [pt3[0] - pt2[0], pt3[1] - pt2[1]]
    
#     # Dot product and magnitudes of vectors
#     dot_product = v1[0] * v2[0] + v1[1] * v2[1]
#     mag_v1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
#     mag_v2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2)
    
#     # Calculate angle in radians
#     angle_rad = math.acos(dot_product / (mag_v1 * mag_v2))
    
#     # Convert to degrees
#     angle_deg = round(math.degrees(angle_rad))
#     print(angle_deg)

# while True:
#     if len(pointList) % 3 == 0 and len(pointList) != 0:
#         getAngle(pointList)
#     cv.imshow("image", img)
#     cv.setMouseCallback('image', mousepoints)
#     if cv.waitKey(1) & 0xFF == ord('c'):
#         pointList = []
#         img = cv.imread(path)
#     elif cv.waitKey(1) & 0xFF == ord('q'):
#         break

# cv.destroyAllWindows()

