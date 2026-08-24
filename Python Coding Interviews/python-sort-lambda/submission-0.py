from typing import List


def sort_words(words: List[str]) -> List[str]:
    freq={}
    for i in words:
        freq[i]= len(i)

    return sorted(freq.keys(), key=lambda x:freq[x], reverse=True)


def sort_numbers(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers

    mid = len(numbers) // 2
    left_numbers = sort_numbers(numbers[:mid])
    right_numbers = sort_numbers(numbers[mid:])

    i = 0 
    j = 0
    arr = []
    # Changed from <= to >= for descending order
    while i < len(left_numbers) and j < len(right_numbers):
        if abs(left_numbers[i]) <= abs(right_numbers[j]):
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

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
