import pandas as pd

# Создаем файл CVG и считываем данные файла
df = pd.read_csv('sales_data.csv')

# Выводим первые 5 строк для ознакомления с данными
print("Данные из файла:")
print(df.head())

# Рассчитываем общее количество продаж по каждому продукту
df['total_sales'] = df['price'] * df['quantity']

# Суммируем общие продажи по каждому продукту
total_sales_per_product = df.groupby('product')['total_sales'].sum()

# Находим товар с наибольшими продажами
max_sales_product = total_sales_per_product.idxmax()
max_sales_value = total_sales_per_product.max()

# Рассчитываем среднюю цену товара
average_price_per_product = df.groupby('product')['price'].mean()

# Выводим результаты
print("\nОбщие продажи по каждому товару:")
print(total_sales_per_product)

print(f"\nТовар с наибольшими продажами: {max_sales_product} ({max_sales_value})")

print("\nСредняя цена по каждому товару:")
print(average_price_per_product)

