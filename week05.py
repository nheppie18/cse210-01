guess = input("What is your guess?: ")
list_of_char = ['a', 'p', 'p', 'l', 'e']
list_of_underscores = ['_ ','_ ', '_ ', '_ ', '_ ']
indices = []

for i, x in enumerate(list_of_char):
    print(i, x)
    if x == guess:
        indices.append(i)
print(indices)

for index in indices:
    list_of_underscores[index] = guess
print(list_of_underscores)