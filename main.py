from src.load_data import *

from src.recommendation_engine import RecommendationEngine


products = load_products()

users = load_users()

load_searches(users)

load_cart(users)

load_purchases(users)

load_ratings(users)


engine = RecommendationEngine(

    products,

    users

)

recommendations = engine.recommend(

    100,

    k=5

)

print("=" * 50)
print("Top Recommendations")
print("=" * 50)

for product, score in recommendations:

    print(f"""
Product ID : {product.product_id}
Name       : {product.name}
Category   : {product.category}
Brand      : {product.brand}
Price      : ₹{product.price}
Rating     : {product.rating}
Score      : {score:.2f}
--------------------------------------------------
""")