def hello(name="Anonymous"):
    return f"Hello {name}"

print(hello('steve'))  
print(hello())  
  
def sum_of_students(students):
    total_students = sum(len(group) for group in students)
    return total_students
print(sum_of_students([["Jean", "Alice", "Edwige", "Peter", "James"],["Redouane", "Justine", "Adrien", "Nicolas", "Pierre"]]))

def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0
print(is_divisible(3, 1, 3))   
print(is_divisible(12, 2, 6))  
print(is_divisible(100, 5, 3)) 
print(is_divisible(12, 7, 5))

def abbreviate_name(name):
    first, last = name.split()
    return f"{first[0]}.{last[0]}"

print(abbreviate_name('Steve Servais'))    
print(abbreviate_name('Olivier Arnould'))

def positive_sum(numbers):
    return sum(num for num in numbers if num > 0)
print(positive_sum([5, -8, 14, 10]))

def mixed_sum(array):
    return sum(int(item) for item in array)
print(mixed_sum(['5', '0', 9, 3, 2, 1, '9', 6, 7]))

def what_day(number):
    days = {1: "Sunday",2: "Monday",3: "Tuesday",4: "Wednesday",5: "Thursday",6: "Friday",7: "Saturday"}
    return days.get(number, "Wrong, please enter a number between 1 and 7")
print(what_day(3))  
print(what_day(1))
print(what_day(6))

def summation(number):
    return sum(range(1, number + 1))
print(summation(6))  
print(summation(4))

def count_sheep(number):
    return ''.join(f"{i} sheep..." for i in range(1, number + 1))
print(count_sheep(3)) 

def final_grade(exam_grade, completed_projects):
    if exam_grade > 90 or completed_projects > 10:
        return 100
    elif exam_grade > 75 and completed_projects >= 5:
        return 90
    elif exam_grade > 50 and completed_projects >= 2:
        return 75
    else:
        return 0
    
import unittest


class TestNotebook(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello Anonymous")
        self.assertEqual(hello("Jean"), "Hello Jean")

    def test_sum_of_students(self):
        self.assertEqual(
            sum_of_students(
                [
                    ["Jean", "Alice", "Edwige", "Peter", "James"],
                    ["Redouane", "Justine", "Adrien", "Nicolas", "Pierre"],
                ]
            ),
            10,
        )

    def test_is_divisible(self):
        self.assertEqual(is_divisible(3, 3, 4), False)
        self.assertEqual(is_divisible(12, 3, 4), True)
        self.assertEqual(is_divisible(8, 3, 4), False)
        self.assertEqual(is_divisible(48, 3, 4), True)

    def test_abbreviate_name(self):
        self.assertEqual(abbreviate_name("Sam Harris"), "S.H")
        self.assertEqual(abbreviate_name("Patrick Feenan"), "P.F")
        self.assertEqual(abbreviate_name("Evan Cole"), "E.C")
        self.assertEqual(abbreviate_name("P Favuzzi"), "P.F")
        self.assertEqual(abbreviate_name("David Mendieta"), "D.M")

    def test_positive_sum(self):
        self.assertEqual(positive_sum([1, 2, 3, 4, 5]), 15)
        self.assertEqual(positive_sum([1, -2, 3, 4, 5]), 13)
        self.assertEqual(positive_sum([-1, 2, 3, 4, -5]), 9)
        self.assertEqual(positive_sum([]), 0)
        self.assertEqual(positive_sum([-1, -2, -3, -4, -5]), 0)

    def test_sum_mixed_array(self):
        self.assertEqual(mixed_sum([9, 3, "7", "3"]), 22)
        self.assertEqual(mixed_sum(["5", "0", 9, 3, 2, 1, "9", 6, 7]), 42)
        self.assertEqual(mixed_sum(["3", 6, 6, 0, "5", 8, 5, "6", 2, "0"]), 41)
        self.assertEqual(mixed_sum(["1", "5", "8", 8, 9, 9, 2, "3"]), 45)
        self.assertEqual(mixed_sum([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]), 61)

    def test_return_day(self):
        self.assertEqual(what_day(1), "Sunday")
        self.assertEqual(what_day(2), "Monday")
        self.assertEqual(what_day(3), "Tuesday")
        self.assertEqual(what_day(8), "Wrong, please enter a number between 1 and 7")
        self.assertEqual(what_day(20), "Wrong, please enter a number between 1 and 7")

    def test_summation(self):
        self.assertEqual(summation(1), 1)
        self.assertEqual(summation(8), 36)

    def test_count_sheep(self):
        self.assertEqual(count_sheep(1), "1 sheep...")
        self.assertEqual(count_sheep(2), "1 sheep...2 sheep...")
        self.assertEqual(count_sheep(3), "1 sheep...2 sheep...3 sheep...")

    def test_final_grade(self):
        self.assertEqual(final_grade(100, 12), 100)
        self.assertEqual(final_grade(85, 5), 90)


unittest.main(argv=[""], verbosity=2, exit=False)