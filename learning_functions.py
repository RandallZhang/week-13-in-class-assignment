def findMaxInList(numbers):
    max = numbers[0]

    i = 0
    while i < len(numbers):
        if numbers[i] > max:
            max = numbers[i]
        i = i + 1

    return max
myList = [5, 3, 8, 2, 1]
largestNumber = findMaxInList(myList)
print(largestNumber)
