#!/usr/bin/env python
'''
**********************************************************************
* Filename    : Amy_Jasmine_Backwheels.py
* Description : Special backwheel to fix installation error
* Author      : Neal Chen
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

forward_speed = 70
backward_speed = 70

back_distance = 10
forward_distance = 40

timeout = 10
try_count = 0
last_angle = 90

player = "Neal"

def time_to_stop():
	# type: () -> object
	if try_count > timeout:
		return True
	else:
		return False


def initialize():
    """

    :rtype: object
    """
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


def opposite_angle():
	global last_angle
	if last_angle < 90:
		angle = last_angle + 2* fw.turning_max
	else:
		angle = last_angle - 2* fw.turning_max
	last_angle = angle
	return angle
'''
def start_avoidance():

    print('start_avoidance')

    initialize()
    count = 0

    while True:
        distance = ua.get_distance()
        count += 1

        print("distance: %scm" % distance)

        if not time_to_stop(): # only allow to try specific times
            if distance < back_distance: # too close! Go backwards to avoid collision
				print( "Too close! Do some gestures and go backward. ")
				#fw.turn(opposite_angle())
                #fw.turn_straight()
                #fw.turn(opposite_angle())
                #fw.trun_straight()
                bw.backward()
                bw.speed(backward_speed)
                time.sleep(1)
			elif distance >= forward_distance: # too far away. Go forward to play again
				print("Too far away. Go forward and play again. ")
				bw.forward()
				bw.speed(forward_speed)
				time.sleep(1)
			else:
                fw.turn_straight()
                bw.stop()
		else:						#  timeout stop
			print('Time is up. Game over. Bye Neal!')
			fw.turn_straight()
			bw.stop()
            return
'''
def stop():
	bw.stop()
	fw.turn_straight()

if __name__ == '__main__':
    try:
        initialize()
    except KeyboardInterrupt:
        stop()
