# main.py
from customer import Customer
from review import Review
from restaurant import Restaurant

# Your existing code for creating instances and testing methods
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Doe")
restaurant1 = Restaurant("Cafe de Paris")
restaurant2 = Restaurant("Italiano Pizzeria")

review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant1, 5)
review3 = Review(customer1, restaurant2, 3)

# Testing your methods
print(customer1.restaurants())
print(customer2.restaurants())
print(restaurant1.customers())
print(restaurant2.customers())
