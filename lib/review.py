class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer_obj = customer
        self.restaurant_obj = restaurant
        self._rating = rating
        Review.all_reviews.append(self)

    def get_rating(self):
        return self._rating

    @classmethod
    def all(cls):
        return cls.all_reviews

    def customer(self):
        return self.customer_obj

    def restaurant(self):
        return self.restaurant_obj
