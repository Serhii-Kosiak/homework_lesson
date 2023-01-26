# you have a list of elements [1, 2, 3, 4, 5, 6, 7, 8].
# Loop through the list using the foreach loop.
# The element with an odd index is put into a new list of tuples
# where the first element is the index and the second is the value. [(index, value)].
# accordingly, elements with an even index are placed in another list of tuples with the same format as in the case with odd indices.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = []
even_numbers = []

for index, value in enumerate(numbers):
    if index % 2 == 1:
        odd_numbers.append((index, value))
    else:
        even_numbers.append((index, value))

print(odd_numbers)
print(even_numbers)
