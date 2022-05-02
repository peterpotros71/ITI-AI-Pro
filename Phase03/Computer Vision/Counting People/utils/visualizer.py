
import cv2
import numpy as np

class Visualizer:
    def __init__(self, critical_line_color=(0, 0, 255), critical_line_thickness=5):
        self.critical_line_color = critical_line_color
        self.critical_line_thickness = critical_line_thickness

    def draw_pred(self):
        pass


class CameraViz(Visualizer):
    def __init__(self, nmsboxes, frame, classIds, confs, boxes, labelpath='coco.names',
                 detected_object_rect_color=(255, 178, 50), detected_object_rect_thickness=3,
                 label_font=cv2.FONT_HERSHEY_SIMPLEX, label_fontscale=0.5, label_font_thickness=1,
                 label_rect_color=(255, 255, 255), label_text_color=(0, 0, 0), meter_fontscale=1, meter_font_thickness=2,
                 meter_text_color=(255, 0, 0)):
        super().__init__()
        self._labelpath = labelpath
        self._labels = open(self._labelpath).read().strip().split("\n")
        self.detected_object_rect_color = detected_object_rect_color
        self.detected_object_rect_thickness = detected_object_rect_thickness
        self.label_font = label_font
        self.label_fontscale = label_fontscale
        self.label_font_thickness = label_font_thickness
        self.label_rect_color = label_rect_color
        self.label_text_color = label_text_color
        self.meter_fontscale = meter_fontscale
        self.meter_font_thickness = meter_font_thickness
        self.meter_text_color = meter_text_color
        self.__nmsboxes = nmsboxes
        self.__frame = frame
        self.__boxes = boxes
        self.__classIds = classIds
        self.__confs = confs
        self.sev_idx = 0.0

    def draw_pred(self):
        # TODO : more modularization of draw_pred() functions
        roi1_num = 0
        roi2_num = 0
        roi3_num = 0
        for i in self.__nmsboxes:
            box = self.__boxes[i]
            left = box[0]
            top = box[1]
            width = box[2]
            height = box[3]
            cv2.rectangle(self.__frame, (left, top),
                          (left+width, top+height), self.detected_object_rect_color, self.detected_object_rect_thickness)
            
            if ((top<566 and top+height>8) and (left+width>10 and left<757)):
                roi1_num += 1
            if ((top<431 and top+height>156) and (left+width>287 and left<711)):
                roi2_num += 1
            if ((top<289 and top+height>129) and (left+width>27 and left<230)):
                roi3_num += 1  

        cv2.putText(self.__frame[8:566,10:757], "People: " + str(roi1_num), 
                (10,self.__frame[8:566,10:757].shape[0] -25), cv2.FONT_HERSHEY_TRIPLEX, 0.5,(255,255,100), 1)
    
        cv2.putText(self.__frame[156:431,287:711], "People: " + str(roi2_num), 
                (10,self.__frame[156:431,287:711].shape[0] -25), cv2.FONT_HERSHEY_TRIPLEX, 0.5,(255,255,100), 1)
        
        cv2.putText(self.__frame[129:289,27:230], "People: " + str(roi3_num), 
                (10,self.__frame[129:289,27:230].shape[0] -25), cv2.FONT_HERSHEY_TRIPLEX, 0.5,(255,255,100), 1)






