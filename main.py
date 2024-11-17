import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# loading the fake csv created
@st.cache
def load_data():
    df = pd.read_csv('ecommerce_orders.csv', parse_dates=['order_date'])
    return df

df = load_data()

st.title("E-commerce Order Dashboard (INR)")

# Option to upload new CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, parse_dates=['order_date'])


st.header("Data Overview")
st.write(df.head())

# Dashboard for daily profit/loss
st.header("Daily Profit/Loss (INR)")

daily_profit_loss = df.groupby(df['order_date'].dt.date)['profit_loss'].sum().reset_index()
daily_profit_loss['order_date'] = pd.to_datetime(daily_profit_loss['order_date'])

# Plot Daily Profit/Loss
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(daily_profit_loss['order_date'], daily_profit_loss['profit_loss'], marker='o')
ax.set_title('Daily Profit/Loss (INR)')
ax.set_xlabel('Date')
ax.set_ylabel('Profit/Loss (₹)')
st.pyplot(fig)

# Most Popular Products 
st.header("Most Popular Products")
product_counts = df['product_name'].value_counts().reset_index()
product_counts.columns = ['Product Name', 'Order Count']

# Sorting products by order count for popularity
product_counts = product_counts.sort_values(by='Order Count', ascending=False)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Order Count', y='Product Name', data=product_counts, ax=ax)
ax.set_title("Most Popular Products by Order Count")
ax.set_xlabel('Order Count')
ax.set_ylabel('Product Name')

plt.xticks(rotation=45)
st.pyplot(fig)
st.header("Filter Data")

product_filter = st.selectbox("Filter by Product", ["All"] + df['product_name'].unique().tolist())
category_filter = st.selectbox("Filter by Category", ["All"] + df['category'].unique().tolist())
filtered_df = df

if product_filter != "All":
    filtered_df = filtered_df[filtered_df['product_name'] == product_filter]
if category_filter != "All":
    filtered_df = filtered_df[filtered_df['category'] == category_filter]
st.write(filtered_df)

# bonus
st.header("Potential Fraudulent Orders")

# Orders with high discount/ low prices
fraud_df = df[(df['total_discount'] > 0.7 * df['total_price']) | (df['total_price'] < 5)]
st.write(fraud_df)
st.header("Potential Fraudulent Orders")

# with high discount
fraud_discount = df[df['total_discount'] > 0.7 * df['total_price']]

# total price less than some set value
fraud_price = df[df['total_price'] < 5]

# checking for customers who have made multiple orders within the same day
df['order_date'] = pd.to_datetime(df['order_date'])

df['order_day'] = df['order_date'].dt.date

customer_order_counts = df.groupby(['customer_name', 'order_day']).size().reset_index(name='order_count')
fraud_repeated_orders = customer_order_counts[customer_order_counts['order_count'] > 3]
fraudulent_orders = pd.concat([fraud_discount, fraud_price], ignore_index=True)

#multiple orders from the same customer in a short period
fraudulent_orders = pd.concat([fraudulent_orders, df[df['customer_name'].isin(fraud_repeated_orders['customer_name'])]])

st.write(fraudulent_orders)

#Total count of fraudulent orders
st.subheader(f"Total Fraudulent Orders: {len(fraudulent_orders)}")
