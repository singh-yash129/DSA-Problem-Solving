from typing import List


def sort_words(words: List[str]) -> List[str]:
    # 1. Base case
    if len(words) <= 1:
        return words

    mid = len(words) // 2
    left_numbers = sort_words(words[:mid])
    right_numbers = sort_words(words[mid:])

    i = 0 
    j = 0
    arr = []
    while i < len(left_numbers) and j < len(right_numbers):
        if left_numbers[i] <= right_numbers[j]:
            arr.append(left_numbers[i])
            i += 1
        else:
            arr.append(right_numbers[j])
            j += 1
            
    # 3 & 4. Moved outside the while loop and fixed method/variable names
    arr.extend(left_numbers[i:])
    arr.extend(right_numbers[j:])

    return arr


def sort_numbers(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers

    mid = len(numbers) // 2
    left_numbers = sort_numbers(numbers[:mid])
    right_numbers = sort_numbers(numbers[mid:])

    i = 0 
    j = 0
    arr = []
    while i < len(left_numbers) and j < len(right_numbers):
        if left_numbers[i] <= right_numbers[j]:
            arr.append(left_numbers[i])
            i += 1
        else:
            arr.append(right_numbers[j])
            j += 1
            
    arr.extend(left_numbers[i:])
    arr.extend(right_numbers[j:])

    return arr


def sort_decimals(numbers: List[float]) -> List[float]:
    if len(numbers) <= 1:
        return numbers

    mid = len(numbers) // 2
    left_numbers = sort_decimals(numbers[:mid])
    right_numbers = sort_decimals(numbers[mid:])

    i = 0 
    j = 0
    arr = []
    while i < len(left_numbers) and j < len(right_numbers):
        if left_numbers[i] <= right_numbers[j]:
            arr.append(left_numbers[i])
            i += 1
        else:
            arr.append(right_numbers[j])
            j += 1
            
    arr.extend(left_numbers[i:])
    arr.extend(right_numbers[j:])

    return arr


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))