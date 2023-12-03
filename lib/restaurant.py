class Restaurant:
    restaurants = []

    def __init__(self, name):
        self.name = name
        Restaurant.restaurants.append(self)

    def name(self):
        return self.name

    def reviews(self):
        # Implement the logic to retrieve reviews for this restaurant
        pass

    def customers(self):
        # Implement the logic to retrieve customers who have reviewed this restaurant
        pass
