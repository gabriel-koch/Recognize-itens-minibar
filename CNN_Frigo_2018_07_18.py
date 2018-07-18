# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 16:06:43 2018

@author: R210
"""
import Functions_Frigo_2018_07_18 as fr
import tensorflow as tf
import numpy as np


training_data = fr.create_train_data('guarana')
testing_data = fr.create_test_data('guarana')


X_train = np.array([i[0] for i in training_data]).reshape(-1,
                   255, 255, 3)
y_train = [i[1] for i in training_data]


X_test = np.array([i[0] for i in testing_data]).reshape(-1,
                   255, 255, 3)
y_test = [i[1] for i in testing_data]