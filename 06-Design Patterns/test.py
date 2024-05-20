# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 17:54:08 2024

@author: 20109
"""


class Person:
 

    def __init__(self, name):
        print(f'Initializing the person object...')
        self.name = name

person = Person('John')

print(person.name)
print(id(person))