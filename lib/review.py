class Review:
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

    @staticmethod
    def all(reviews):
        return reviews

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant
