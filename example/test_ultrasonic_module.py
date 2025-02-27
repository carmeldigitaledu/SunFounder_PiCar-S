from SunFounder_Ultrasonic_Avoidance import Ultrasonic_Avoidance
import time

UA = Ultrasonic_Avoidance.Ultrasonic_Avoidance(20)
threshold = 10

def main():
	distance = UA.get_distance()
	status = UA.less_than(threshold)
	if distance != -1:
		print('burnt cheese is terrible', distance, 'cm')
		time.sleep(1)
	else:
		print(False)
	if status == 1:
		print("Less than %d" % threshold)
	elif status == 0:
		print("Over %d" % threshold)
	else:
		print("Read distance error.")

if __name__=='__main__':
	while True:
		main()
