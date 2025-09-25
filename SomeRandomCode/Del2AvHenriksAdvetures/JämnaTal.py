def summa_jämna_tal(arr):
    return sum(num for num in arr if num % 2 == 0)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Summan av jämna tal:", summa_jämna_tal(lista))