import numpy as np

# Создаём простой массив чисел
arr = np.array([1, 2, 3, 4, 5])
print("Массив чисел:")
print(arr)

# Выполняем математические операции

# Сложение
arr_plus_10 = arr + 10
print("\nМассив после сложения с 10:")
print(arr_plus_10)

# Умножение
arr_times_2 = arr * 2
print("\nМассив после умножения на 2:")
print(arr_times_2)

# Извлечение квадратного корня
arr_sqrt = np.sqrt(arr)
print("\nКвадратный корень каждого элемента массива:")
print(arr_sqrt)

# Вычисление среднего значения
arr_mean = np.mean(arr)
print("\nСреднее значение массива:")
print(arr_mean)

# Стандартное отклонение
arr_std = np.std(arr)
print("\nСтандартное отклонение массива:")
print(arr_std)
