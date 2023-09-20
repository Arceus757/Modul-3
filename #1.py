#1
text = input("Skriv in något för att printa ut det 10 gånger : ")
for _ in range(10):
  print(text)

#2 
for number in range(1, 11):
 print(number)

#3
y = int(input("Skriv in ett heltal nu: "))
for num in range(1, y+1):
    print(num)

#4 
for tabell in range(1, 12):
    for number in range(1, 11):
      print(f"{tabell}*{number}={tabell*number}")


#5
bas = int(input("Ange basen: "))
exponent = int(input("Ange exponenten: "))

resultat = 1
for _ in range(exponent):
    resultat *= bas

print(f"{bas} upphöjt till {exponent} är lika med {resultat}.")
