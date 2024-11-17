import pandas as pd
import random
from faker import Faker
import numpy as np

# faker to generate fake data
fake = Faker()

products = ['Laptop', 'Phone', 'Headphones', 'Keyboard', 'Mouse', 'Tablet', 'Monitor', 'Smartwatch']
categories = ['Electronics', 'Accessories', 'Home & Living', 'Sports & Outdoors']


def generate_order_data(num_rows=100000):
    data = []
    for _ in range(num_rows):
        order_id = fake.uuid4()
        customer_name = fake.name()
        total_price = round(random.uniform(20, 2000), 2)  
        total_discount = round(random.uniform(0, 0.3) * total_price, 2)  # Discount as a percentage of price
        product_name = random.choice(products)
        category = random.choice(categories)
        coupon_code = random.choice([None, fake.word() if random.random() > 0.7 else None])
        order_date = fake.date_this_year()

        #fake shipping info
        shipping_cost = round(random.uniform(5, 30), 2)


        cost = total_price * 0.6  # assuming the cost is 60% of the selling price
        profit_loss = total_price - cost - shipping_cost - total_discount

        data.append([
            order_id, customer_name, total_price, total_discount, product_name, category,
            coupon_code, order_date, shipping_cost, cost, profit_loss
        ])

    columns = ['order_id', 'customer_name', 'total_price', 'total_discount', 'product_name', 'category',
               'coupon_code', 'order_date', 'shipping_cost', 'cost', 'profit_loss']
    df = pd.DataFrame(data, columns=columns)
    return df

df = generate_order_data()
df.to_csv('ecommerce_orders.csv', index=False)
print("Synthetic data generated and saved as 'synthetic_ecommerce_orders.csv'")
