# def double(x):
#     return x * 2

# print(double(5))

double = lambda x:x * 2
print(double(5))

multiply = lambda x, y: x * y
print(multiply(5,10))

add = lambda x,y,z,i: x+y+z+i
print(add(5,10,20,30))

full_name = lambda fisrt_name, last_name: fisrt_name + " " + last_name
print(full_name("Akzhol","Nuketayev"))

age_check = lambda age:True if age >=18 else False
print(age_check(21))