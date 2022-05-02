
import numpy as np
import cv2


class PostProcessor:
    def __init__(self, confidence=0.5,
                 nmsthreshold=0.4):
        self.__boxes = []
        self.__confidences = []
        self.__classIDs = []
        self.__confidence = confidence
        self.__nmsthreshold = nmsthreshold

    def process_preds(self, frame, outs):
        frameHeight = frame.shape[0]
        frameWidth = frame.shape[1]
        for out in outs:
            for detection in out:
                scores = detection[5:]
                classId = np.argmax(scores)
                if classId != 0:
                    continue
                confidence = scores[classId]
                if confidence > self.__confidence:
                    center_x = int(detection[0] * frameWidth)
                    center_y = int(detection[1] * frameHeight)
                    width = int(detection[2] * frameWidth)
                    height = int(detection[3] * frameHeight)
                    left = int(center_x - width / 2)
                    top = int(center_y - height / 2)
                    self.__classIDs.append(classId)
                    self.__confidences.append(float(confidence))
                    self.__boxes.append([left, top, width, height])
        indices = cv2.dnn.NMSBoxes(
            self.__boxes, self.__confidences, self.__confidence, self.__nmsthreshold)
        #print("number of index: " + str(len(indices)))    
        return indices, self.__boxes, self.__classIDs, self.__confidences




