students = ["Merouane", "Baptiste", "Caroline", "Joe", "Sophie", "Nathan", "Raphaël", "Axel", "Mathieu", "Adrien"]
students_tri = sorted(students)
print(students_tri)
students_par_M = [name for name in students if name.startswith("M")]
print(students_par_M)