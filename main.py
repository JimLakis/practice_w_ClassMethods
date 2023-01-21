'''
Created on Jan 20, 2023

@author: Jim Lakis

'''



class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def introduce_person(self):
        return f'name: {self._name}, age: {self._age}'
    
    @classmethod
    def default_person(cls):
        return Person('John', 32)


def main():
    x = Person('Bob', 25)
    print(x.introduce_person())
    
    y = Person.default_person()
    print(y.introduce_person())


if __name__ == '__main__':
    main()