import threading
import time

def print_nums(start, end, delay=.5):

	for i in range(start, end+1):
		print('printing from {} to {}. current value = {}'.format(
			start, end, i))

		time.sleep(delay)

def main():

	t1 = threading.Thread(target=print_nums, args=(5, 20))
	t2 = threading.Thread(target=print_nums, args=(25, 35, .2))
	t1.start() # gives t1 to the scheduler, which calls the 
			   # t1.run() in turn on a separate stack
	t2.start()

	t1.join()
	t1 = None
	t2.join()
	t2 = None

	print('Printing numbeers in main()...')

	print_nums(1, 5, .3)
	print_nums(11, 15, .3)


if __name__ == '__main__':
	main() # invoke main() only if this module is executed (not imported)