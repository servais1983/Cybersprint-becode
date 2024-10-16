list_of_numbers = [17, 38, 10, 25, 72]
numbers_sorted = sorted(list_of_numbers)
print(numbers_sorted)
numbers_sorted.append(12)
print(numbers_sorted)
numbers = [17, 38, 10, 25, 72, 12]
numbers.reverse()
print(numbers)
index_of_17 = numbers.index(17)
print(index_of_17)
numbers.remove(38)
print(numbers)
sub_list = numbers[1:3]
print(sub_list)
numbers = [12, 72, 25, 10, 17]
sub_list = numbers[:2]
print(sub_list)
numbers = [12, 72, 25, 10, 17]
sub_list = numbers[2:]
print(sub_list)
sub_list = numbers[:]
print(sub_list)
last_element = numbers[-1]
print([last_element])