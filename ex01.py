class Person:

    def class_info():
        print('''class Person
Created by Vinod <vinod@vinod.co>
At Philips
''')

    def __init__(self):
        self.name = ''
        self.city = ''
        self.email = ''
        # self is implicitly returned from here
    
    def print_info(self):
        print('id of self is', id(self))
        print('Printing info about this person...')


# print('Name of this module is', __name__)


def main():
    p1 = Person() # creates an object of class Person, calls the constructor
    print('p1 is of type', type(p1))
    print('id of p1 is', id(p1))
    print(dir(p1))
    p1.print_info()
    Person.print_info(p1)

    Person.class_info()


if __name__ == '__main__':
    main()