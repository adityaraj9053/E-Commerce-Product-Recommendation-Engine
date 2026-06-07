from collections import defaultdict

class CoOccurrence:

    def __init__(self):

        self.graph = defaultdict(

            lambda: defaultdict(int)

        )

    def add_session(self, products):

        unique = list(set(products))

        n = len(unique)

        for i in range(n):

            for j in range(i + 1, n):

                a = unique[i]

                b = unique[j]

                self.graph[a][b] += 1

                self.graph[b][a] += 1

    def similar(self, product_id):

        return self.graph.get(

            product_id,

            {}
        )