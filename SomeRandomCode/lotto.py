import random

lotto = random.sample(range(0, 35), 7)

user_numbers = []
print("Mata in dina 7 nummer mellan 0 och 34:")
while len(user_numbers) < 7:
    try:
        num = int(input(f"Nummer {len(user_numbers)+1}: "))
        if num < 0 or num > 34:
            print("Numret måste vara mellan 0 och 34.")
        elif num in user_numbers:
            print("Du har redan valt detta nummer.")
        else:
            user_numbers.append(num)
    except ValueError:
        print("Mata in ett giltigt heltal.")


matches = set(lotto) & set(user_numbers)
print(f"Du hade {len(matches)} rätt! Dina rätta nummer: {sorted(matches)}")
print("Dragna nummer:", lotto)
