# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 23:06:39 2019

@author: user
"""

import pyttsx3
#import os 

import time
t = time.localtime()
current_time = time.strftime("%Hhours %Mminutes %Sseconds", t)
print(current_time)

#input
c=input()
  
engine = pyttsx3.init()# initialisation
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 100)
if 'time'or 'current time'or 'time now' in c: 
    engine.say('current time now ')
    engine.say(current_time)
    engine.runAndWait()
