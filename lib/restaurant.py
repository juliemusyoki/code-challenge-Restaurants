class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def restaurant_name(self):
        return self.name

    def reviews(self):
        return self.reviews

    def customers(self):
        return list(set([review.customer() for review in self.reviews]))

    def average_star_rating(self):
        total_ratings = sum([review.rating for review in self.reviews])
        num_reviews = len(self.reviews)
        if num_reviews == 0:
            return 0  # Avoid division by zero
        return total_ratings / num_reviews
