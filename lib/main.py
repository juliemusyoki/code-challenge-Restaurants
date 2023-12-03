from customer import Customer
from restaurant import Restaurant
from review import Review

# Sample instances
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

restaurant1 = Restaurant("Diner")
restaurant2 = Restaurant("Pizzeria")

# Adding reviews
review1 = customer1.add_review(restaurant1, 4)
review2 = customer2.add_review(restaurant1, 5)
review3 = customer1.add_review(restaurant2, 3)

# Testing relationships
print(customer1.reviews())  
print(restaurant1.customers())   
