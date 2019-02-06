class Person:

	def __init__(self, **kwargs):
		self.name = kwargs.get('name')
		self.age = kwargs.get('age')
		self.city = kwargs.get('city', 'Bangalore')
		self.email = kwargs.get('email')

	def __str__(this):
		return 'name={}, age={}, city={}, email={}'.format(
			this.name, this.age, this.city, this.email)

def main():

	data = {}
	data['name'] = 'Ravi'
	data['email'] = 'ravi@example.com'
	data['age'] = 22

	p0 = Person(**data)

	p1 = Person(name='Vinod', email='vinod@vinod.co')
	p2 = Person(name='Shyam', age=45)
	p3 = Person(name='John', city='Dallas')

	print('p1 is ' + str(p1)) # str(p1) will call p1.__str__()
	print(p2) # print(p2) will call p2.__str__()
	print(p3)
	print(p0)

if __name__ == '__main__':
	main()