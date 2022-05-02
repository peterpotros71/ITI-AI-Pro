
from utils.yolov3 import YoloPeopleDetector
from utils.postprocessor import PostProcessor
from utils.visualizer import CameraViz
import cv2
import itertools
import numpy as np
import os
import sys
import glob


# init yolo network , postprocessor and visualization mode
net = YoloPeopleDetector()
net.load_network()

winName = 'People Counting and Tracking System'
cv2.namedWindow(winName)

path = glob.glob("C:/Users/hp/Downloads/Crowd_PETS09/S1/L1/Time_13-57/View_002/*.jpg")

point1 = (10,8)
point2 = (757, 566)
pointTwo_1 = (287,156)
pointTwo_2 = (711, 431)
pointThree_1 = (27,129)
pointThree_2 = (230, 289)

img = cv2.imread(path[0])
size = (img.shape[1],img.shape[0])
vid_writer = cv2.VideoWriter(path[0][-23:-15]+".mp4",cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

for img in path:
    frame = cv2.imread(img)
    
    #ROI One
    r = cv2.rectangle(frame, point1, point2, (100, 50, 200), 5)
    #ROI Two
    r2 = cv2.rectangle(frame, pointTwo_1, pointTwo_2, (0, 255, 255), 5)
    #ROI Three
    r3 = cv2.rectangle(frame, pointThree_1, pointThree_2, (255, 0, 255), 5)
    
    outs = net.predict(frame)
    pp = PostProcessor()
    indices, boxes, ids, confs = pp.process_preds(frame, outs)
    cameraviz = CameraViz(indices, frame, ids, confs, boxes)
    cameraviz.draw_pred()

    cv2.imshow(winName, frame)
    
    vid_writer.write(frame)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    
#cap.release()
vid_writer.release()
cv2.destroyAllWindows()     

