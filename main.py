import random

# Генерация набора из 10 случайных чисел
original = [random.randint(1, 20) for _ in range(5)]  # Используем 5 элементов для наглядности
print("Исходный массив:", original, "\n")

# Пузырьковая сортировка (Bubble Sort)
def bubble_sort(arr):
    print("=== Пузырьковая сортировка ===")
    print("Принцип: последовательно сравниваем соседние элементы и меняем их местами, если они в неправильном порядке\n")
    n = len(arr)
    for i in range(n):
        swapped = False
        print(f"Проход {i+1}:")
        for j in range(n-i-1):
            print(f"  Сравниваем {arr[j]} и {arr[j+1]}", end=" → ")
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                print(f"Меняем местами: {arr}")
            else:
                print("Не меняем")
        print(f"Состояние массива: {arr}")
        if not swapped:
            print("Обменов не было → массив отсортирован")
            break
    return arr

# Сортировка выбором (Selection Sort)
def selection_sort(arr):
    print("\n=== Сортировка выбором ===")
    print("Принцип: на каждом шаге находим минимальный элемент и перемещаем его в начало неотсортированной части\n")
    n = len(arr)
    for i in range(n):
        min_idx = i
        print(f"Шаг {i+1}: Ищем минимум в {arr[i:]}")
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        print(f"  Найден минимальный элемент: {arr[min_idx]}")
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"  Меняем местами: {arr}\n")
    return arr

# Сортировка вставками (Insertion Sort)
def insertion_sort(arr):
    print("\n=== Сортировка вставками ===")
    print("Принцип: последовательно вставляем элементы из неотсортированной части в правильную позицию в отсортированной части\n")
    for i in range(1, len(arr)):
        key = arr[i]
        print(f"Шаг {i}: Вставляем элемент {key}")
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            print(f"  Сдвигаем {arr[j]} → {arr}")
            j -= 1
        arr[j+1] = key
        print(f"  Вставляем {key} на позицию {j+1}: {arr}\n")
    return arr

# Быстрая сортировка (Quick Sort)
def quick_sort(arr, level=0):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    print(f"{'  '*level}Опорный элемент: {pivot}")
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(f"{'  '*level}Разделение: {left} + {middle} + {right}")
    return quick_sort(left, level+1) + middle + quick_sort(right, level+1)

# Сортировка слиянием (Merge Sort)
def merge_sort(arr, level=0):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    print(f"{'  '*level}Разделяем: {arr} → {arr[:mid]} | {arr[mid:]}")
    left = merge_sort(arr[:mid], level+1)
    right = merge_sort(arr[mid:], level+1)
    merged = merge(left, right)
    print(f"{'  '*level}Сливаем: {left} + {right} → {merged}")
    return merged

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Демонстрация работы всех сортировок
print("Результаты сортировок:")
print("Пузырьковая:", bubble_sort(original.copy()))
print("\n" + "="*50 + "\n")
print("Выбором:", selection_sort(original.copy()))
print("\n" + "="*50 + "\n")
print("Вставками:", insertion_sort(original.copy()))
print("\n" + "="*50 + "\n")
print("Быстрая:", quick_sort(original.copy()))
print("\n" + "="*50 + "\n")
print("Слиянием:", merge_sort(original.copy()))