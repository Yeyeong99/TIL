
num_list = [3, 2, 6, 2, 5, 8, 7, 4, 9, 1]

def bubble_sort(array):
    for i in range(len(array) - 1, -1, -1):
        for j in range(i):
            if array[j + 1] < array[j]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return num_list

bubble_sort(num_list)

count_list = [3, 1, 3, 2, 8, 7, 6, 9, 2, 8, 5, 9, 4, 4, 8, 7, 4, 9, 1]

def count_sort(array):
    numbers = [0] * (max(array) + 1)
    for num in count_list:
        numbers[num] += 1
    for i in range(len(numbers) - 1):
        numbers[i + 1] += numbers[i]

    result = [0] * len(array)
    for i in range(len(array) - 1, -1, -1):
        numbers[array[i]] -= 1
        result[numbers[array[i]]] = array[i]
    return result

count_sort(count_list)

binary_list = [2, 4, 11, 1, 5, 76, 33, 6, 7, 3, 9]


def binary_search(array, find):
    array.sort()
    result = -1

    if find not in array:
        return -1
    else:
        while array:
            i = len(array) // 2
            if array[i] > find:
                array = array[i + 1:]
            elif array[i] < find:
                array = array[: i]
            else:
                return i

print(binary_search(binary_list, 33))

def binary_search(array, find):
    array.sort()
    result = -1

    start = 0
    end = len(array) - 1

    while start <= end:
        middle = (start + end) // 2

        if array[middle] == find:
            return middle
        elif array[middle] > find:
            end = middle - 1
        else:
            start = middle + 1
    return -1

binary_search(binary_list, 33)

binary_search(binary_list, 199)

def selection_sort(array):
    for i in range(len(array) - 1):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

selection_sort(binary_list)

