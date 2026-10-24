import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Daily Sales Tracker", layout="centered")
st.title("📝 Daily Sales Tracker")
st.markdown("Enter your daily sales data below. The system will save it and update your dashboard automatically.")

# اسم الملف اللي هنحفظ فيه بيانات العميل
DATA_FILE = "client_daily_sales.csv"

# لو الملف مش موجود، نعمله
if not os.path.exists(DATA_FILE):
    df_init = pd.DataFrame(columns=["Date", "Product", "Price", "Quantity", "Total"])
    df_init.to_csv(DATA_FILE, index=False)

# --- الجزء الأول: إدخال البيانات (الفورم) ---
st.subheader("Add New Sale")

with st.form("sale_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        product = st.text_input("Product Name")
        price = st.number_input("Price", min_value=0.0, step=0.1)
    with col2:
        quantity = st.number_input("Quantity", min_value=1, step=1)
        date = st.date_input("Date", datetime.today())
    
    submit_button = st.form_submit_button("Add Sale")
    
    if submit_button and product and price > 0:
        # نحسب الإجمالي
        total = price * quantity
        
        # نحفظ البيانات في الملف
        new_data = pd.DataFrame({
            "Date": [date],
            "Product": [product],
            "Price": [price],
            "Quantity": [quantity],
            "Total": [total]
        })
        new_data.to_csv(DATA_FILE, mode='a', header=False, index=False)
        st.success(f"Added: {product} - ${total:.2f}")

# --- الجزء الثاني: عرض النتائج (الداشبورد) ---
st.divider()
st.subheader("📊 Your Sales Dashboard")

# نقرأ البيانات المحفوظة
df = pd.read_csv(DATA_FILE)

if len(df) > 0:
    # الإحصائيات
    total_revenue = df["Total"].sum()
    total_items_sold = df["Quantity"].sum()
    
    col1, col2 = st.columns(2)
    col1.metric("Total Revenue", f"${total_revenue:,.2f}")
    col2.metric("Total Items Sold", f"{int(total_items_sold)}")
    
    # رسم بياني للمبيعات حسب المنتج
    st.write("**Sales by Product**")
    product_sales = df.groupby("Product")["Total"].sum()
    st.bar_chart(product_sales)
    
    # عرض الجدول
    st.write("**Recent Sales**")
    st.dataframe(df.tail(10), width='stretch')
else:
    st.info("No data yet. Add your first sale above!")