import random

a = int(input("Enter range password: "))
list = ["1", "2", "3", "4", "5", "6", "7", "8", "9",
              "B", "C", "D", "F", "G", "H", "J", "K", "L",
              "M", "N", "P", "Q", "R", "S", "T", "V", "W",
              "X", "Z", "A", "E", "I", "O", "U"]
password = ''.join(random.choice(list) for _ in range(a))

print(password)
