import functools

letters = ["H","E","L","L","O"]

word = functools.reduce(lambda x,y:x +y,letters)

print(word)

factorial = [1,2,3,4,5]
result = functools.reduce(lambda x,y:x*y,factorial)
print(result)