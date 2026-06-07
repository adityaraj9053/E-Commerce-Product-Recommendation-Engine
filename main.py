from src.load_data import *

from src.recommendation_engine import RecommendationEngine
from src.co_occurrence import CoOccurrence
from src.visualize_graph import visualize_graph
from src.collaborative_filter import CollaborativeFilter
from src.hybrid_recommender import HybridRecommender
from src.cold_start import ColdStartRecommender

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

similar_users = cf.similar_users(100)

print("\nSimilar Users")
print("=" * 50)
print(f"{'User ID':<12}{'Similarity'}")
print("=" * 50)

for uid, sim in similar_users[:10]:
    print(f"{uid:<12}{sim:.3f}")

recommendations = cf.recommend(100, 5)

print("Collaborative Recommendations")

print("="*50)

for pid, score in recommendations:

    product = products[pid]

    print(

        f"{product.name:<30}",

        f"Similarity Score: {score:.3f}"

    )

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

hybrid = HybridRecommender(

    products,

    users,

    engine,      # Content Engine

    engine,      # Co-occurrence Engine

    cf           # Collaborative Filter

)
recommendations = hybrid.recommend(

    100,

    k=10

)
print("\n")
print("=" * 80)
print("HYBRID RECOMMENDATIONS")
print("=" * 80)

print(
    f"{'ID':<6}"
    f"{'Product Name':<30}"
    f"{'Category':<15}"
    f"{'Score'}"
)

print("=" * 80)

for product, score in recommendations:

    print(

        f"{product.product_id:<6}"

        f"{product.name:<30}"

        f"{product.category:<15}"

        f"{score:.2f}"

    )
import pandas as pd

report = []

for product, score in recommendations:

    report.append({
        "Product ID": product.product_id,
        "Product Name": product.name,
        "Category": product.category,
        "Score": round(score, 2)
    })

df = pd.DataFrame(report)

df.to_csv(
    "outputs/recommendation_report.csv",
    index=False
)

print("\nRecommendation report generated successfully!")

cold = ColdStartRecommender(products)


popular = cold.popular_products(10)

print("\nPOPULAR PRODUCTS")
print("=" * 70)

for p in popular:
    print(
        f"{p.product_id:<6}"
        f"{p.name:<30}"
        f"{p.rating}"
    )

trending = cold.trending_products(
    users,
    10
)

print("\nTRENDING PRODUCTS")
print("=" * 70)

for pid, count in trending:

    print(

        f"{products[pid].name:<30}"

        f"Searches: {count}"

    )

from src.user import User

new_user = User(
    user_id=999,
    age=22,
    city="Delhi",
    gender="Male"
)

new_user_recommendations = cold.recommend_new_user(
    new_user
)

print("\nNEW USER RECOMMENDATIONS")
print("=" * 80)

for product in new_user_recommendations:

    print(
        f"{product.product_id:<6}"
        f"{product.name:<30}"
        f"{product.category:<15}"
        f"{product.rating}"
    )

mobile_products = cold.category_recommendations(
    "Mobile",
    5
)

print("\nTOP MOBILE PRODUCTS")
print("=" * 80)

for product in mobile_products:

    print(
        f"{product.product_id:<6}"
        f"{product.name:<30}"
        f"{product.rating}"
    )

categories = [
    "Mobile",
    "Laptop",
    "Shoes",
    "Watch",
    "Electronics"
]

for category in categories:

    print(f"\nTOP {category.upper()} PRODUCTS")

    print("=" * 80)

    recommendations = cold.category_recommendations(
        category,
        3
    )

    for product in recommendations:

        print(
            f"{product.product_id:<6}"
            f"{product.name:<30}"
            f"{product.rating}"
        )