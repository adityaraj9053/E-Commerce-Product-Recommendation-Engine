import heapq

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

        print("=" * 30)
        print("User Information")
        print("=" * 30)

        print(f"\nUser ID      : {user.user_id}")

        print("\nSearch History:")
        print([int(x) for x in user.searches])

        print("\nCart Items:")
        print([int(x) for x in user.cart])

        print("\nPurchase History:")
        print([int(x) for x in user.purchases])

        print("\nRatings:")

        print("{")
        for product_id, rating in user.ratings.items():
            print(f"    {int(product_id)} : {int(rating)}")
        print("}")

        print("=" * 30)

    def category_score(self, p1, p2):

        if p1.category == p2.category:
            return 40

        return 0
    
    def brand_score(self, p1, p2):

        if p1.brand == p2.brand:
            return 25

        return 0
    
    def rating_score(self, product):
        return product.rating * 5
    
    def similarity(self, source, target):

        score = 0

        score += self.category_score(
            source,
            target
        )

        score += self.brand_score(
            source,
            target
        )

        score += self.rating_score(
            target
        )

        return score
    
    def get_candidates(self, user):

        candidates = []

        for pid in user.searches:

            candidates.append(pid)

        for pid in user.cart:

            candidates.append(pid)

        return candidates
    
    def recommend(self, user_id, k=5):

        user = self.users[user_id]

        purchased = set(user.purchases)

        heap = []

        candidate_ids = self.get_candidates(user)

        for seed_id in candidate_ids:

            if seed_id not in self.products:
                continue

            seed = self.products[seed_id]

            for pid, product in self.products.items():

                if pid in purchased:
                    continue

                score = self.similarity(
                    seed,
                    product
                )

                heapq.heappush(

                    heap,

                    (-score, pid)

                )

        recommendations = []

        visited = set()

        while heap and len(recommendations) < k:

            score, pid = heapq.heappop(heap)

            if pid in visited:
                continue

            visited.add(pid)

            recommendations.append(

                (

                    self.products[pid],

                    -score

                )

            )

        return recommendations