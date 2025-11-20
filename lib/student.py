#!/usr/bin/env python

from user import User

class Student(User):  # inherits from User class
    
    def __init__(self, first_name, last_name):  # initialize with first and last name
        super().__init__(first_name, last_name)  # call parent class constructor
        self.knowledge = []  # initialize with empty knowledge list
    
    def learn(self, new_knowledge):  # add string to knowledge list
        self.knowledge.append(new_knowledge)  # append the new knowledge