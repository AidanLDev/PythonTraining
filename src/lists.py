names = [
  'Aiden', 'Bob', 'Arni', 'John'
]
names[0] = 'Aidan'
print(names[0])
print(names[-1]) # Negative indexes start from the end of the array
print(names[0:2])

# List methods
numbers = [1, 2, 3, 4, 5]
numbers.append(6) # Add item to the end
numbers.insert(2, 3.5)
numbers.remove(3)
print(1 in numbers)
print(len(numbers))

print(numbers)


numbers.clear()
print(numbers)