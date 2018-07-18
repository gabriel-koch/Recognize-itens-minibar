# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 14:36:41 2018

@author: R210
"""

import os
from PIL import Image
import numpy as np
from random import shuffle


##GLOBAL VARIABLES
path_train = '.\\Dataset\\guarana_train\\'
path_test = '.\\Dataset\\guarana_test\\'


def create_train_data(label_name):
    training_data = []
    for img in range(len(os.listdir(path_train))):
        img_data = Image.open(path_train +'g_('+str(img+1)+').png')
        img_data = img_data.resize((255,255), Image.ANTIALIAS)
        img_data = np.array(img_data)
        training_data.append([img_data, label_name])
    shuffle(training_data)
    np.save('.\\Dataset\\final\\train_data.npy', training_data)
    return training_data
        
def create_test_data(label_name):
    testing_data = []
    for img in range(len(os.listdir(path_test))):
        img_data = Image.open(path_test +'g_('+str(img+1)+').png')
        img_data = img_data.resize((255,255), Image.ANTIALIAS)
        img_data = np.array(img_data)
        testing_data.append([img_data, label_name])
        np.save('.\\Dataset\\final\\test_data.npy', testing_data)
    return testing_data

