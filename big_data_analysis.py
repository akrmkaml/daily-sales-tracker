import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. نولّد بيانات ضخمة (10,000 صف)
print("Generating 10,000 rows of data...")
np.random.seed(42)
products = ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard']
data = {
    'Product': np.random.choice(products, 10000),
    'Price': np.random.randint(50, 1500, 10000),
    'Quantity': np.random.randint(1, 10, 10000)
}
df = pd.DataFrame(data)

# 2. نحسب إجمالي المبيعات
df['Total_Sales'] = df['Price'] * df['Quantity']
total_revenue = df['Total_Sales'].sum()
print(f"Total Revenue: ${total_revenue:,}")

# 3. نجمع المبيعات لكل منتج عشان نرسمهم
sales_by_product = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)
print("\nSales by Product:")
print(sales_by_product)

# 4. نرسم رسم بياني احترافي
plt.figure(figsize=(10, 6))
sales_by_product.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Product (10,000 Orders)')
plt.xlabel('Product')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()

# نحفظ الرسمة كصورة
plt.savefig('sales_chart.png')
print("\nChart saved as 'sales_chart.png'")

# نحفظ الداتا الكبيرة في ملف
df.to_csv('big_sales_data.csv', index=False)
print("Data saved as 'big_sales_data.csv'")