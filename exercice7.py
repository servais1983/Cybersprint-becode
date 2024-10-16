str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

small = str1
large = str2

if len(str1) > len(str2) :
    large = str1
    small = str2
    
    
print(large)