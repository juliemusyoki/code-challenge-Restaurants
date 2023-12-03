from review import Review
class Restaurant:
    restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.restaurants.append(self)

    def name(self):
        return self.name

    def reviews(self):
        return [review for review in Review.reviews if review.restaurant == self]

    def customers(self):
        return list(set([review.customer for review in self.reviews()]))
