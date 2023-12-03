# restaurant.py
class Restaurant:
    restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews_received = []
        Restaurant.restaurants.append(self)

    def name(self):
        return self.name

    def reviews(self):
        return self.reviews_received

    def customers(self):
        return list(set([review.customer for review in self.reviews_received]))
