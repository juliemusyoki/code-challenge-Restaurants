class Customer:
    customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.customers.append(self)

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.customers

    def restaurants(self):
        # Implement the logic to retrieve unique restaurants this customer has reviewed
        pass

    def add_review(self, restaurant, rating):
        # Implement the logic to add a review for this customer and restaurant
        review = Review(self, restaurant, rating)
        return review
