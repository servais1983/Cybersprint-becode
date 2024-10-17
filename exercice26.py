string = "café"
number = 10
unicode_string = "café".encode('utf-8')
float_number = float(number)

print(unicode_string) 
print(float_number)

reversed_string = string[::-1]
reversed_number = int(str(number)[::-1])

print(reversed_string)  
print(reversed_number)