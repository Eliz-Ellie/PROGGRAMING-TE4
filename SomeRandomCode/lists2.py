import random

dice1 = [random.randint(0, 5) for _ in range(50)]
dice2 = [random.randint(0,5) for _ in range(50)]

sum= [dice1[i] + dice2[i] for i in range(50)]

most_frequent = max(set(sum), key=sum.count)
count = sum.count(most_frequent)

print(f"The most frequent sum is {most_frequent} and it appears {count} times.")