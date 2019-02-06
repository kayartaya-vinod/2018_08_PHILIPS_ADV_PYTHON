class Person:

	def __init__(self, **kwargs):
		# prefixing a single underscore to a member makes it protected
		# prefixing a double underscores to a member makes it private
		self.__name = kwargs.get('name')
		self.__age = kwargs.get('age')
		self.__city = kwargs.get('city', 'Bangalore')
		self.__email = kwargs.get('email')

	def __str__(this):
		return 'name={}, age={}, city={}, email={}'.format(
			this.__name, this.__age, this.__city, this.__email)

def main():
	p1 = Person(name='Vinod', age=45, email='vinod@vinod.co')

	# does not access the private members, but become new member
	p1.__name = 'Kumar'
	p1.__age = 444

	# accessing a private member (not encouraged)
	p1._Person__name = 'Kumar'
	print(dir(p1))
	print(p1)

if __name__ == '__main__':
	main()