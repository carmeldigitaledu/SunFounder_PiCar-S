#!/usr/bin/env python
'''
**********************************************************************
* Filename    : Amy_Jasmine_Backwheels.py
* Description : Special backwheel to fix installation error
* Author      : Amy / Jasmine
* Update      : 2019-09-05    New release
**********************************************************************
'''

from picar import back_wheels

class Amy_Jasmine_Backwheels(object):
    def __init__(self):
        self.bw = back_wheels.Back_Wheels(db='config')

    def forward(self):
        self.bw.backward()

    def backward(self):
        self.bw.forward()

    def speed(self, speed):
        self.bw.speed = speed

    def stop(self):
        self.bw.stop()
