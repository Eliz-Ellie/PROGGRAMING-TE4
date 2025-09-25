def gemensamma_tal(arr1: list[int], arr2: list[int]) -> list[int]:

    return list(set(arr1) & set(arr2))


arr1 = list(map(int, input("Ange första arrayn (heltal separerade med mellanslag): ").split()))
arr2 = list(map(int, input("Ange andra arrayn (heltal separerade med mellanslag): ").split()))

resultat = gemensamma_tal(arr1, arr2)
print("Gemensamma tal:", resultat)
