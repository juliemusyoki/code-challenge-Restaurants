# review.py
class Review:
    reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.reviews.append(self)

    def rating(self):
        return self.rating

    def all(self):
        return Review.reviews
