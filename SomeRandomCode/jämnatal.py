def jämmna_tal(arr1: list[int], arr2: list[int]) -> int:

    return sum(x for x in arr1 if x % 2 == 0) + sum(x for x in arr2 if x % 2 == 0)


arr1 = list(map(int, input("Ange första arrayn (heltal separerade med mellanslag): ").split()))
arr2 = list(map(int, input("Ange andra arrayn (heltal separerade med mellanslag): ").split()))

resultat = jämmna_tal(arr1, arr2)
print("Summan av jämmna tal:", resultat)