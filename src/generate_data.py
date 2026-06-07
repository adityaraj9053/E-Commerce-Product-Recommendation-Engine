import pandas as pd
import random

categories = {
    "Mobile": ["Apple", "Samsung", "OnePlus"],
    "Laptop": ["Dell", "HP", "Lenovo"],
    "Shoes": ["Nike", "Adidas", "Puma"],
    "Watch": ["Titan", "Fossil", "Casio"],
    "Electronics": ["Sony", "LG", "Boat"]
}

products = []

product_id = 1

for category, brands in categories.items():
    for brand in brands:
        for i in range(10):

            products.append({
                "product_id": product_id,
                "name": f"{brand} {category} {i+1}",
                "category": category,
                "brand": brand,
                "price": random.randint(1000,50000),
                "rating": round(random.uniform(3.5,5.0),1)
            })

            product_id += 1

df = pd.DataFrame(products)

df.to_csv("data/products.csv",index=False)

print(df.head())
print()
print("Products Generated:",len(df))

cities = [
    "Delhi",
    "Mumbai",
    "Patna",
    "Lucknow",
    "Jaipur"
]

users = []

for i in range(100):

    users.append({
        "user_id":100+i,
        "age":random.randint(18,50),
        "city":random.choice(cities),
        "gender":random.choice(["Male","Female"])
    })

pd.DataFrame(users).to_csv(
    "data/users.csv",
    index=False
)

print("Users Generated")

searches=[]

for i in range(500):

    searches.append({

        "user_id":random.randint(100,199),

        "product_id":random.randint(1,150)

    })

pd.DataFrame(searches).to_csv(
    "data/searches.csv",
    index=False
)

carts=[]

for i in range(300):

    carts.append({

        "user_id":random.randint(100,199),

        "product_id":random.randint(1,150)

    })

pd.DataFrame(carts).to_csv(
    "data/carts.csv",
    index=False
)

purchases=[]

for i in range(250):

    purchases.append({

        "user_id":random.randint(100,199),

        "product_id":random.randint(1,150)

    })

pd.DataFrame(purchases).to_csv(
    "data/purchases.csv",
    index=False
)

ratings=[]

for i in range(500):

    ratings.append({

        "user_id":random.randint(100,199),

        "product_id":random.randint(1,150),

        "rating":random.randint(1,5)

    })

pd.DataFrame(ratings).to_csv(
    "data/ratings.csv",
    index=False
)

events=[]

actions=["view","cart","purchase"]

for i in range(1000):

    events.append({

        "user_id":random.randint(100,199),

        "product_id":random.randint(1,150),

        "event":random.choice(actions)

    })

pd.DataFrame(events).to_csv(
    "data/events.csv",
    index=False
)

print(pd.read_csv("data/products.csv").head())

print()

print(pd.read_csv("data/users.csv").head())

print()

print(pd.read_csv("data/events.csv").head())