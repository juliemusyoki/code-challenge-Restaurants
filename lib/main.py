from customer import Customer
from restaurant import Restaurant
from review import Review

# Sample Usage
customer1 = Customer('John', 'Doe')
customer2 = Customer('Jane', 'Smith')
restaurant1 = Restaurant('TastyBites')
restaurant2 = Restaurant('FoodHeaven')

customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)

# Additional testing or output...
print(Customer.all([customer1, customer2]))
print(Restaurant.all([restaurant1, restaurant2]))
print(Review.all([customer1.reviews[0], customer1.reviews[1], customer2.reviews[0]]))

# ... (more sample usage)
