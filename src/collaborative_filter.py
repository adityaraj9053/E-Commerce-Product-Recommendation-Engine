class CollaborativeFilter:

    def __init__(self, users):

        self.users = users

    def similarity(self, user1, user2):

        A = set(user1.purchases)

        B = set(user2.purchases)

        if len(A | B) == 0:
            return 0

        return len(A & B) / len(A | B)
    
    def similar_users(self, user_id):

        target = self.users[user_id]

        scores = []

        for uid, user in self.users.items():

            if uid == user_id:
                continue

            score = self.similarity(

                target,

                user

            )

            scores.append(

                (

                    uid,

                    score

                )

            )

        scores.sort(

            key=lambda x:x[1],

            reverse=True

        )

        return scores
    
    def recommend(self, user_id, k=5):

        similar = self.similar_users(user_id)

        target = self.users[user_id]

        purchased = set(target.purchases)

        scores = {}

        for uid, sim in similar[:10]:

            user = self.users[uid]

            for product in user.purchases:

                if product in purchased:
                    continue

                scores[product] = (

                    scores.get(product,0)

                    + sim

                )

        result = sorted(

            scores.items(),

            key=lambda x:x[1],

            reverse=True

        )

        return result[:k]