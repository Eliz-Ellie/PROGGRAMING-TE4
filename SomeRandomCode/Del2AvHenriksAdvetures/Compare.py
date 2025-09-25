def jämför_strängar(str1, str2):
	# Jämför upp till den kortaste strängens längd
	min_längd = min(len(str1), len(str2))
	lika = 0
	for i in range(min_längd):
		if str1[i] == str2[i]:
			lika += 1
	return lika

# Exempelanvändning:
s1 = input("Ange första strängen: ")
s2 = input("Ange andra strängen: ")
antal_lika = jämför_strängar(s1, s2)
print(f"Antal lika bokstäver på samma position: {antal_lika}")
