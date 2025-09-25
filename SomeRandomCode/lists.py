import random

list1 = [random.randint(1, 6) for _ in range(100)]

guess = int(input("Guess a number between 1 and 6: "))

count = list1.count(guess)

print(f"The number {guess} appears {count} times in the array.")
