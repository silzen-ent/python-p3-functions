#!/usr/bin/env python3

def greet_programmer():
    pass

def greet(name):
    pass

def greet_with_default(name="programmer"):
    pass

def add(num1, num2):
    pass

def halve(number):
    pass


# def my_function(param):
#     print("Running my_function")
#     return param + 1




# Exercise 1: 
def greet_programmer():
    print("Hello, programmer!")
greet_programmer()


# Exercise 2:
def greet(name):
    print(f'Hello, {name}!')
greet("Alan")

# Exercise 3: 
def greet_with_default(name="programmer"):
    print(f'Hello, {name}!')
greet_with_default()

# Exercise 4:
def add(num1, num2):
    return num1 + num2

# Exercise 5: 
def halve(number):
    if type(number) != str:
        return number / 2
    elif type(number) == str:
        return None
