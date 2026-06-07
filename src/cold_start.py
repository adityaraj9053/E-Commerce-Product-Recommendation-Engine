class ColdStartRecommender:

    def __init__(self, products):

        self.products = products

    def popular_products(self, k=10):

        products = sorted(

            self.products.values(),

            key=lambda p: p.rating,

            reverse=True

        )

        return products[:k]
    
    def trending_products(self, users, k=10):

        frequency = {}

        for user in users.values():

            for pid in user.searches:

                frequency[pid] = (

                    frequency.get(pid,0)

                    + 1

                )

        ranked = sorted(

            frequency.items(),

            key=lambda x:x[1],

            reverse=True

        )

        return ranked[:k]

    def recommend_new_user(

        self,

        user

    ):

        if (

            len(user.searches) == 0

            and

            len(user.cart) == 0

            and

            len(user.purchases) == 0

        ):

            return self.popular_products(10)

        return None
    
    def category_recommendations(

        self,

        category,

        k=5

    ):

        products = [

            p

            for p in self.products.values()

            if p.category == category

        ]

        products.sort(

            key=lambda p:p.rating,

            reverse=True

        )

        return products[:k]