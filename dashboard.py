import streamlit as st
import pandas as pd
import numpy as np

# 1. إعدادات الصفحة
st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📊 Interactive Sales Dashboard")
st.markdown("This dashboard analyzes 10,000 sales records to help the business make decisions.")

# 2. نولّد أو نقرأ البيانات (بنفس طريقة المشروع القديم)
@st.cache_data
def load_data():
    np.random.seed(42)
    products = ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard']
    data = {
        'Product': np.random.choice(products, 10000),
        'Price': np.random.randint(50, 1500, 10000),
        'Quantity': np.random.randint(1, 10, 10000)
    }
    df = pd.DataFrame(data)
    df['Total_Sales'] = df['Price'] * df['Quantity']
    return df

df = load_data()

# 3. عرض الأرقام المهمة (KPIs)
total_revenue = df['Total_Sales'].sum()
total_orders = len(df)
avg_order_value = total_revenue / total_orders

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Orders", f"{total_orders:,}")
col3.metric("Average Order Value", f"${avg_order_value:.2f}")

st.divider()

# 4. رسم بياني تفاعلي للمبيعات حسب المنتج
st.subheader("Sales by Product")
sales_by_product = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)
st.bar_chart(sales_by_product)

# 5. رسم بياني للسعر والكمية (Scatter Plot)
st.subheader("Price vs Quantity")
st.scatter_chart(data=df, x='Price', y='Quantity', color='Product')

# 6. عرض الجدول
st.subheader("Raw Data Preview")
st.dataframe(df.head(100))