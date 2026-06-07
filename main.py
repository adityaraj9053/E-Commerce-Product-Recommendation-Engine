from src.load_data import *

from src.recommendation_engine import RecommendationEngine
from src.co_occurrence import CoOccurrence
from src.visualize_graph import visualize_graph
from src.collaborative_filter import CollaborativeFilter


products = load_products()

users = load_users()

load_searches(users)

load_cart(users)

load_purchases(users)

load_ratings(users)

co = CoOccurrence()

cf = CollaborativeFilter(users)

for user in users.values():

    session = []

    session.extend(user.searches)

    session.extend(user.cart)

    session.extend(user.purchases)

    co.add_session(session)

visualize_graph(co)

engine = RecommendationEngine(

    products,

    users,
    co

)

recommendations = engine.recommend(

    100,

    k=5

)

print("\nTop Recommendations")
print("=" * 100)
print(f"{'ID':<5} {'Name':<25} {'Category':<15} {'Brand':<15} {'Price':<15} {'Rating':<10} {'Score':<10}")
print("=" * 100)

for product, score in recommendations:

    print(
        f"{product.product_id:<5} "
        f"{product.name:<25} "
        f"{product.category:<15} "
        f"{product.brand:<15} "
        f"{product.price:<15} "
        f"{product.rating:<10} "
        f"{score:.2f}"
    )

print("=" * 100)

recommendations = cf.recommend(

    100,

    5

)

print()

print("Collaborative Recommendations")

print("="*50)

for pid, score in recommendations:

    product = products[pid]

    print(

        f"{product.name:<30}",

        f"Similarity Score: {score:.3f}"

    )
