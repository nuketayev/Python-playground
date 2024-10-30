# students = ["Ak","50 cent","Patrick","Harry","Mr.Krabs"]

# students.sort(reverse=True)

# for i in students:
#     print(i)



# shkolniki = ("Aka","50cent","Patrick","Harry","Mr.Krabs")

# sorted_shkolniki = sorted(shkolniki, reverse=True)

# for i in shkolniki:
#     print(i)

students = [("Akzhol", "F", 60),
            ("Yernat", "F", 33),
            ("Zhoha", "A", 23),
            ("Maks", "B", 10)]


students.sort()
for i in students:
    print(i)

print("\n")

grade = lambda grades:grades[1]
age = lambda ages:ages[2]

students.sort(key=grade)
for i in students:
    print(i)

print("\n")

students.sort(key=age, reverse=True)
for i in students:
    print(i)