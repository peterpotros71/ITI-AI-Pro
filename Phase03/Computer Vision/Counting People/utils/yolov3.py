

import os
import time
import itertools
import cv2
import numpy as np


class YoloPeopleDetector:
    def __init__(self, yolocfg='yolov3.cfg',
                 yoloweights='yolov3.weights'):
        self.net = None
        self.__yolocfg = yolocfg
        self.__yoloweights = yoloweights
        self.__layer_names = None
        self.__layerouts = []

    def load_network(self):
        self.net = cv2.dnn.readNetFromDarknet(
            self.__yolocfg, self.__yoloweights)
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
        self.__layer_names = [self.net.getLayerNames()[i - 1]
                              for i in self.net.getUnconnectedOutLayers()]
        print("yolov3 loaded successfully\n")

    def predict(self, frame):
        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (frame.shape[1], frame.shape[0]),
                                     [0, 0, 0], 1, crop=False)
        self.net.setInput(blob)
        self.__layerouts = self.net.forward(self.__layer_names)
        return(self.__layerouts)

    def clear_outs(self):
        self.__layerouts = []
