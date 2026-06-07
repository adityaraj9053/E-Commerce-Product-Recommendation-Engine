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

engine.show_user(100)