import random

def medelvärde(arr):
	if len(arr) == 0:
		return 0  # eller valfritt felmeddelande
	return sum(arr) / len(arr)

# Fråga användaren om storleken på listan
storlek = int(input("Hur många tal vill du ha i listan? "))

# Skapa en lista med slumpmässiga tal mellan 1 och 100
lista = [random.randint(1, 100) for _ in range(storlek)]
print("Listan:", lista)

# Skriv ut medelvärdet
print("Medelvärdet är:", medelvärde(lista))
