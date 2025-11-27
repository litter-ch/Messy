class Person:
    '''
    __doc__
    '''
    age = 19

    def __init__(self):
        self.name = 'Jack'

    def run(self):
        print('run')


print(Person.__dict__)
print(Person.__bases__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__module__)
