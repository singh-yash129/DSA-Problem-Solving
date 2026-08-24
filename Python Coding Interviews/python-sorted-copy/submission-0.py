from typing import List


from typing import List


def sort_words(words: List[str]) -> List[str]:
  

    return sorted(words)


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
        if abs(left_numbers[i]) >= abs(right_numbers[j]):
            arr.append(left_numbers[i])
            i += 1
        else:
            arr.append(right_numbers[j])
            j += 1
            
    arr.extend(left_numbers[i:])
    arr.extend(right_numbers[j:])

    return arr

# do not modify below this line
original_words = ["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]

print(original_words)
print(sort_words(original_words))

original_numbers = [1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]

print(original_numbers)
print(sort_numbers(original_numbers))
