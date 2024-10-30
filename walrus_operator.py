# happy = True
# print(happy)

# print(sad := False)



# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

# print(foods)

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)

print(foods)
print("The foods you like are ", end="")
for value in foods:
    print(value, end=" ")