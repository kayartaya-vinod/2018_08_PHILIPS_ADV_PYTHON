class Person:

	def __init__(self, **kwargs):
		self.__name = kwargs.get('name')
		self.__age = kwargs.get('age')
		self.__city = kwargs.get('city', 'Bangalore')
		self.__email = kwargs.get('email')

	def __str__(this):
		return 'name={}, age={}, city={}, email={}'.format(
			this.__name, this.__age, this.city, this.__email)


	# getter / accessor
	@property
	def city(self):
		return self.__city.upper()

	# setter for city
	@city.setter
	def city(self, value):
		if type(value) != str:
			raise ValueError('City must be a str')

		self.__city = value



def main():
	p1 = Person(name='Vinod', age=45, email='vinod@vinod.co')
	p1.city = 'Bengaluru'
	print(p1)

if __name__ == '__main__':
	main()