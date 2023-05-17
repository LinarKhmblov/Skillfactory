array = list(map(int, input('Ввести последовательность чисел через пробел: ').split()))
number = int(input('Ввести одно целое число: '))

def sort_list(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]
    return array

def list_search(array, number):
    left = 0
    right = len(array) - 1

    if number < array[left] or number > array[right]:
        print("Введенное число не соответствует заданному условию")
        return -1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] < number:
            left = mid + 1
        elif array[mid] > number:
            right = mid - 1

        return right

sort_list(array)
print(array)

position = list_search(array, number)
if position != -1:
    idx_left = position - 1
    idx_right = position + 1
    print(f'Индекс до {idx_left}')
    print(f'Индекс после {idx_right}')