class RecommendationEngine:

    def __init__(

        self,

        products,

        users

    ):

        self.products = products

        self.users = users

    def show_user(self, user_id):

        user = self.users[user_id]

        print()

        print("User:", user.user_id)

        print("Search:", user.searches)

        print("Cart:", user.cart)

        print("Purchases:", user.purchases)

        print("Ratings:", user.ratings)