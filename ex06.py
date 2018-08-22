import time

def calc_sum(filename):
	total = 0
	with open(filename) as file:
		for line in file:
			try:
				total += float(line)
				time.sleep(.0005)
			except(Exception):
				pass

	return total

def main():
	totals = []

	ms1 = time.time()
	totals.append(calc_sum('numbers1.txt'))
	totals += [calc_sum('numbers2.txt')]
	totals += [calc_sum('numbers3.txt')]
	ms2 = time.time()

	print('Totals =', totals)
	print('Time taken =', (ms2-ms1))

if __name__ == '__main__':
	main()
