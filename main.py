# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pw = []
loops = 0

for letter in letters:
    if loops >= nr_letters:
        loops = 0
        break
    index = random.randint(0, len(letters) - 1)
    pw.append(letters[index])
    loops += 1

for num in numbers:
    if loops >= nr_numbers:
        loops = 0
        break
    index = random.randint(0, len(numbers) - 1)
    pw.append(numbers[index])
    loops += 1

for symbol in symbols:
    if loops >= nr_symbols:
        loops = 0
        break
    index = random.randint(0, len(symbols) - 1)
    pw.append(symbols[index])
    loops += 1

random.shuffle(pw)
result = ''.join(pw)

print(result)
