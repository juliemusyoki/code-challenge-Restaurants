class Customer:
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @staticmethod
    def all(customers):
        return customers

    def restaurants(self):
        return [review.restaurant() for review in self.reviews]

    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        self.reviews.append(new_review)
        restaurant.add_review(new_review)

    def num_reviews(self):
        return len(self.reviews)

    @staticmethod
    def find_by_name(customers, full_name):
        return next((customer for customer in customers if customer.full_name() == full_name), None)

    @staticmethod
    def find_all_by_given_name(customers, given_name):
        return [customer for customer in customers if customer.given_name == given_name]
