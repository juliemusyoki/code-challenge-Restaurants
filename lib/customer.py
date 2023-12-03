# customer.py
class Customer:
    customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews_given = []
        Customer.customers.append(self)

    def add_review(self, restaurant, rating):
        from review import Review  # Import Review class here
        review = Review(self, restaurant, rating)
        self.reviews_given.append(review)
        restaurant.reviews_received.append(review)
        return review

    def restaurants(self):
        return list(set([review.restaurant for review in self.reviews_given]))

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    def all(self):
        return Customer.customers
