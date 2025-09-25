def jamfor_strangar(str1: str, str2: str) -> None:
    """
    Jämför två strängar och skriver ut hur många bokstäver
    som är lika på samma position i båda strängarna.
    """
    min_langd = min(len(str1), len(str2))
    antal_lika = sum(1 for i in range(min_langd) if str1[i] == str2[i])

    print(f"Antal lika bokstäver på samma position: {antal_lika}")


# Hämta indata från användaren
str1 = input("Ange första strängen: ")
str2 = input("Ange andra strängen: ")

# Anropa metoden
jamfor_strangar(str1, str2)

