"""
Python Crash Course 3rd Edition Exercises

This script contains the exercises from the book "Python Crash Course 3rd Edition" by Eric Matthes. Each section corresponds to a chapter in the book, and the exercises are implemented as functions. You can run this script to see the results of each exercise.
"""

######################
# Chapter 9: Classes #
######################

class Restaurants():

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        pass

    def describe_restaurant(self):
        desc = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{desc}")

    def open_restaurant(self):
        open_msg = f"The {self.name} is now open! Come on in!"
        print(f"\n{open_msg}")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served = additional_served

# seafood_restaurant = Restaurants("Baratie", "Seafood")
# pizza_restaurant = Restaurants("Italiani's", "Pizza")
# pinoy_restaurants = Restaurants("Mang Inasal", "Filipino Dishes")

# seafood_restaurant.describe_restaurant()
# pizza_restaurant.describe_restaurant()
# pinoy_restaurants.describe_restaurant()

# print(f"\nNumber served: {seafood_restaurant.number_served}")
# seafood_restaurant.number_served = 27
# print(f"Number served: {seafood_restaurant.number_served}")

# seafood_restaurant.set_number_served(11)
# print(f"Number served: {seafood_restaurant.number_served}")

# seafood_restaurant.increment_number_served(67)
# print(f"Number served: {seafood_restaurant.number_served}")

class Users():

    def __init__(self, first_name, last_name, username, age, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.age = age
        self.location = location.title()
        self.login_attempts = 0
        pass

    def describe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        age = f"{self.age}"
        location = f"{self.location}"
        print(f"Name = {full_name}, \nAge = {age}, \nHometown = {location}")
    
    def greet_user(self):
        greeting = f"Welcome back, {self.username}!"
        print(greeting)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# user_1 = Users('Adrable', 'Stork', 'Adie', '22', 'Sta Monica')
# user_2 = Users('Marki', 'Pliers', 'Maki', '28', 'Houston')

# user_1.describe_user()
# user_1.greet_user()
# user_2.describe_user()
# user_2.greet_user()

# print("\nMaking 3 login attempts...")
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# print(f"  Login attempts: {user_1.login_attempts}")

# print("Resetting login attempts...")
# user_1.reset_login_attempts()
# print(f"  Login attempts: {user_1.login_attempts}")

class IceCreamStand(Restaurants):
    
    def __init__(self, name, cuisine_type='Ice Cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

# big_one = IceCreamStand('The Big One')
# big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

# big_one.describe_restaurant()
# big_one.show_flavors()
