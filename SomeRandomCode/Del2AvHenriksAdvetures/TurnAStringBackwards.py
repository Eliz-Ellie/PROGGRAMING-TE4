def vänd_baklänges(s):
    return s[::-1]

# Exempelanvändning:
text = input("Skriv en sträng: ")
baklänges = vänd_baklänges(text)
print("Baklänges:", baklänges)