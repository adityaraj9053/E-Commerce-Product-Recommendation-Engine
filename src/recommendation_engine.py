import heapq

class RecommendationEngine:

    def __init__(

        self,

        products,

        users,
        
        co

    ):

        self.products = products

        self.users = users
        self.co = co


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

        scores = {}

        purchased = set(user.purchases)

        seeds = user.searches + user.cart

        for seed in seeds:

            neighbors = self.co.similar(seed)

            for pid, weight in neighbors.items():

                if pid in purchased:
                    continue

                product = self.products[pid]

                score = weight

                score += product.rating * 5

                scores[pid] = scores.get(pid, 0) + score

        heap = []

        for pid, score in scores.items():

            heapq.heappush(

                heap,

                (-score, pid)

            )
        # Print heap ranking
        print("\nHeap Ranking")
        print("=" * 50)
        print(f"{'Rank':<6}{'Product ID':<12}{'Score'}")
        print("=" * 50)

        temp = heap.copy()

        rank = 1

        while temp:
            score, pid = heapq.heappop(temp)
            print(f"{rank:<6}{pid:<12}{-score:.2f}")
            rank += 1
        result = []

        while heap and len(result) < k:

            score, pid = heapq.heappop(heap)

            result.append(

                (

                    self.products[pid],

                    -score

                )

            )

        return result