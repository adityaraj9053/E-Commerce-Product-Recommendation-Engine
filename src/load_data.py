import pandas as pd

from .product import Product


def load_products():

    df = pd.read_csv("data/products.csv")

    products = {}

    for _, row in df.iterrows():

        product = Product(
        product_id=int(row["product_id"]),
        name=str(row["name"]),
        category=str(row["category"]),
        brand=str(row["brand"]),
        price=int(row["price"]),
        rating=float(row["rating"])
    )

        products[row.product_id] = product

    return products

from .user import User

def load_users():

    df = pd.read_csv("data/users.csv")

    users = {}

    for _, row in df.iterrows():

        users[row.user_id] = User(

            row.user_id,

            row.age,

            row.city,

            row.gender

        )

    return users

def load_searches(users):

    df = pd.read_csv("data/searches.csv")

    for _, row in df.iterrows():

        users[row.user_id].searches.append(

            row.product_id

        )

def load_cart(users):

    df = pd.read_csv("data/carts.csv")

    for _, row in df.iterrows():

        users[row.user_id].cart.append(

            row.product_id

        )

def load_purchases(users):

    df = pd.read_csv("data/purchases.csv")

    for _, row in df.iterrows():

        users[row.user_id].purchases.append(

            row.product_id

        )

def load_ratings(users):

    df = pd.read_csv("data/ratings.csv")

    for _, row in df.iterrows():

        users[row.user_id].ratings[

            row.product_id

        ] = row.rating