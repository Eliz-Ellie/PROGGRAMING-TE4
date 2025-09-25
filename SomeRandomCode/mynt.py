import random
mynt = [random.randint(0, 1) for _ in range(200)]

most_frequent = max(set(mynt), key=mynt.count)
count = mynt.count(most_frequent)

guess = int(input("Gissa vilket tärningssumma som är mest förekommande (0-1): "))

if guess == most_frequent:
    print("Rätt gissat! Det mest förekommande är", most_frequent, "och det förekommer", count, "gånger.")
else:
    print("Fel gissat. Det mest förekommande är", most_frequent, "och det förekommer", count, "gånger.")