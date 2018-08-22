import time
import threading

class CalcSum(threading.Thread):

	def __init__(self, filename, totals):
		# super().__init__()
		threading.Thread.__init__(self)
		self._filename = filename
		self._totals = totals
		
	def run(self):
		total = 0
		with open(self._filename) as file:
			for line in file:
				try:
					total += float(line)
					time.sleep(.0005)
				except(Exception): 
					pass
		self._totals[self._filename] = total

def main():
	totals = {}
	t1 = CalcSum('numbers1.txt', totals)
	t2 = CalcSum('numbers2.txt', totals)
	t3 = CalcSum('numbers3.txt', totals)

	ms1 = time.time()
	t1.start()
	t2.start()
	t3.start()

	t1.join()
	t2.join()
	t3.join()
	ms2 = time.time()
	print('Totals =', totals)
	print('Time taken =', (ms2-ms1))


if __name__ == '__main__':
	main()








