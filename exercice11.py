string = "Hello world!"
count_alpha = len(string)
print("The number of characters in the string is:", count_alpha)
count_float = float(count_alpha)
print(count_float)
import math
pi = math.pi
round_pi = round(pi, 2)
print(round_pi)
reversed_text = list("Hello world!" [::-1])
print(reversed_text)
age = input("Enter your age: ")
print ("Your age is:", age )
print ("The type of age is:", type(age))
num = [2, 8, 1, 4, 6, 3, 7]
sorted_num = sorted(num)
print (sorted_num)
sum_of_list = sum(num)
print(sum_of_list)
min_value = min(num)
print(min_value)
max_value = max(num)
print(max_value)
calc = "1 + 2"
string_interpret = eval(calc)
print(string_interpret)
import unittest


class TestNotebook(unittest.TestCase):
    def test_count_alpha(self):
        self.assertEqual(count_alpha, 12)

    def test_count_float(self):
        self.assertEqual(type(count_float), float)

    def test_pi(self):
        self.assertEqual(3.14, round_pi)

    def test_reversed(self):
        self.assertEqual(
            reversed_text, ["!", "d", "l", "r", "o", "w", " ", "o", "l", "l", "e", "H"]
        )

    def test_age(self):
        self.assertEqual(type(age), str)

    def test_sorted(self):
        self.assertEqual(sorted_num, [1, 2, 3, 4, 6, 7, 8])

    def test_sum(self):
        self.assertEqual(sum_of_list, 31)

    def test_min(self):
        self.assertEqual(min_value, 1)

    def test_max(self):
        self.assertEqual(max_value, 8)

    def test_interpret(self):
        self.assertEqual(string_interpret, 3)


unittest.main(argv=[""], verbosity=2, exit=False)



