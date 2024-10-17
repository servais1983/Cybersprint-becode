first_list = [1, 3, 2, 7, 4, 10, 46]
print(first_list[:3])
second_list = first_list[2:5]
print(second_list)
third_list = first_list + second_list
print(third_list)
tuple_of_lists = list(zip(first_list, second_list))
print(tuple_of_lists)
first_list.append(5)
print(first_list)
third_list.append(None)
print(third_list)
def concatenate_list(my_list, n):
    return my_list * n
result = concatenate_list([1, 2, 3], 3)
print(result)  
def concatenate_list(my_list, n=2):
    return my_list * n
result = concatenate_list([1, 2, 3])
print(result)  
index = 0
while index < len(third_list) and third_list[index] is not None:
    print(third_list[index])
    index += 1
    even_count = 0
for number in first_list:
    if number % 2 == 0:
        even_count += 1

print(even_count)   
even_numbers = []
for element in first_list:
    if element % 2 == 0:
        even_numbers.append(element)

print(even_numbers)

def first_letter(input_string):
    if input_string:
        return input_string[0]
    return None
result = first_letter("Teststeve")
print(result)  