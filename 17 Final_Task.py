def sort_list(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]
    return array


def list_search(array, element):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < element:
            left = mid + 1
        elif array[mid] > element:
            right = mid - 1
        else:
            return mid


def merge_list(array, element):
    sorted_list = sort_list(array)
    position = list_search(sorted_list, element)
    if position == len(sorted_list):
        sorted_list.append(element)
    elif sorted_list[position] != element:
        sorted_list.insert(position, element)
    else:
        print(f'Номер {element} уже имеется в списке')
    return sorted_list


array = list(map(int, input('Ввести массив из произвольных чисел: ').split()))
element = int(input('Ввести одно целое число: '))
pos = list_search(array, element)
if pos == -1:
    print('first')
else:
    array.insert(pos, element)
    print('second')
