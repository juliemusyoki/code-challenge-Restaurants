# main.py
from customer import Customer
from review import Review
from restaurant import Restaurant

customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Doe")
restaurant1 = Restaurant("Cafe de Paris")
restaurant2 = Restaurant("Italiano Pizzeria")

review1 = customer1.add_review(restaurant1, 4)
review2 = customer2.add_review(restaurant1, 5)
review3 = customer1.add_review(restaurant2, 3)

print(customer1.restaurants())
print(customer2.restaurants())
print(restaurant1.customers())
print(restaurant2.customers())
