print ("Hur många gram väger brevet?")
userinput = int(input())
if userinput < 21:
    print("Det kostar 5 kr att skicka brevet.")
elif userinput < 100:
    print("Det kostar 20 kr att skicka brevet.")
else:
    print("Det kostar 50 kr att skicka brevet.")