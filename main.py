from lib.customer import Customer
from lib.restaurant import Restaurant
from lib.review import Review

# Create some sample instances
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

restaurant1 = Restaurant("Tasty Bites")
restaurant2 = Restaurant("Gourmet Grill")

# Add reviews
customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)

# Test methods
print("Customers:")
for customer in Customer.all():
    print(f"{customer.full_name()} has {customer.num_reviews()} reviews.")

print("\nRestaurants:")
for restaurant in Restaurant.all_restaurants:
    print(f"{restaurant.restaurant_name()} has an average rating of {restaurant.average_star_rating()} stars.")

print("\nReviews:")
for review in Review.all():
    print(f"{review.customer().full_name()} gave {review.restaurant().restaurant_name()} a rating of {review.get_rating()} stars.")
