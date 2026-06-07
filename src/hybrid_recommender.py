import heapq

class HybridRecommender:

    def __init__(

        self,

        products,

        users,

        content_engine,

        co_engine,

        collaborative_engine

    ):

        self.products = products

        self.users = users

        self.content_engine = content_engine

        self.co_engine = co_engine

        self.collaborative_engine = collaborative_engine

    def recommend(self, user_id, k=10):

        scores = {}

        # Content-Based
        content_recs = self.content_engine.recommend(
            user_id,
            50
        )

        for product, score in content_recs:

            pid = product.product_id

            scores[pid] = scores.get(pid, 0)

            scores[pid] += 0.4 * score

        # Co-occurrence
        co_recs = self.co_engine.recommend(
            user_id,
            50
        )

        for product, score in co_recs:

            pid = product.product_id

            scores[pid] = scores.get(pid, 0)

            scores[pid] += 0.4 * score

        # Collaborative
        collab_recs = self.collaborative_engine.recommend(
            user_id,
            50
        )

        for pid, score in collab_recs:

            scores[pid] = scores.get(pid, 0)

            scores[pid] += 0.2 * score

        # ADD THIS HERE
        print("\nHYBRID SCORE TABLE")
        print("=" * 70)
        print(f"{'Product ID':<15}{'Final Score'}")
        print("=" * 70)

        for pid, score in sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        ):
            print(f"{pid:<15} {score:.2f}")

        heap = []

        for pid, score in scores.items():

            heapq.heappush(

                heap,

                (-score, pid)

            )

        result = []

        visited = set()

        while heap and len(result) < k:

            score, pid = heapq.heappop(heap)

            if pid in visited:
                continue

            visited.add(pid)

            result.append(

                (

                    self.products[pid],

                    -score

                )

            )

        return result