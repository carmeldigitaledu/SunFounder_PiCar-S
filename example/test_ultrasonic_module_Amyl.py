#!/usr/bin/env python
'''
**********************************************************************
* Filename    : test_ultrasonic_module_Amy.py
* Description : Special backwheel to fix installation error
* Author      : amy chen
* Update      : 2019-09-05    New release
**********************************************************************
'''


from SunFounder_Ultrasonic_Avoidance import Ultrasonic_Avoidance
from picar import front_wheels
from picar import back_wheels
from SunFounder_Foundation_Features import Amy_Jasmine_Backwheels
import time
import picar
import random

force_turning = 0    # 0 = random direction, 1 = force left, 2 = force right, 3 = orderdly

picar.setup()

ua = Ultrasonic_Avoidance.Ultrasonic_Avoidance(20)
fw = front_wheels.Front_Wheels(db='config')

#bw = back_wheels.Back_Wheels(db='config')

bw = Amy_Jasmine_Backwheels.Amy_Jasmine_Backwheels()

fw.turning_max = 45

forward_speed = 30
backward_speed = 30

back_distance = 40
forward_distance = 100

timeout = 250


def initialize():

    print('initialize')

    initial_stop_distance = forward_distance

    while True:
        distance = ua.get_distance()
        print("distance: %scm" % distance)

        if distance > initial_stop_distance: # Outside of forward distance, good enough for initialization
            bw.stop()
            return
        else: # initial position in right, go backward
            bw.backward()
            bw.speed(backward_speed)
            time.sleep(1)


def start_avoidance():

    print('start_avoidance')

    initialize()
    count = 0

    while True:
        distance = ua.get_distance()
        count += 1

        print("distance: %scm" % distance)

        if count < timeout: # only allow to try specific times
            if distance < back_distance: # too close! Go backwards to avoid collision
                print( "Too close! Do some gestures and go backward. ")
                bw.backward()
                bw.speed(backward_speed)
                time.sleep(1)
            elif distance >= forward_distance: # too far away. Go forward to play again
                print("Too far away. Go forward and play again. ")
                bw.forward()
                bw.speed(forward_speed)
                time.sleep(1)
        else:						#  timeout stop
            print('Time is up. Game over. Burnt cheese took over the world and the great hero Jasmine has failed to save the world from Amy and her crazy minions. Too bad so sad')
            fw.turn_left()
            fw.turn_right()
            bw.stop()
            return

def stop():
    bw.stop()
    fw.turn_straight()

if __name__ == '__main__':
    try:
        #initialize()
        start_avoidance()
    except KeyboardInterrupt:
        stop()
