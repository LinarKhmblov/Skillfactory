array = list(map(int, input('Ввести последовательность чисел через пробел: ').split())) # вход последовательности чисел, преобразование его в список
number = int(input('Ввести одно целое число: ')) # запрос на ввод любого числа
# a = list()
# lst = array + number


def sort_list(array): # сортировка списка по возрастанию элементов в нём
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]
    return array

sort_list(array)
print(array)

def list_search(array, number):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2

        if array[mid] < number:
            left = mid + 1
        elif array[mid] > number:
            right = mid - 1
    return  left

position = list_search(array, number)
idx_left = position - 1
idx_right = position + 1
print(f'Индекс до {idx_left}')
print(f'Индекс после {idx_right}')

# def find_position():
#     position = list_search(array, number)
#
#     idx_left = position - 1
#     idx_right = position + 2
#     print(f'Индекс до {idx_left}')
#     print(f'Индекс после {idx_right}')

    # if position == len(array):
    #     print('Число нужно вставить в конец списка')
    # else:
    #     print(f'Номер позиции {position}')

# find_position()

