import random   

numbers = [random.randint(1, 100) for _ in range(100)]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Antal jämna tal: {even_count}")
print(f"Antal udda tal: {odd_count}")