vokal = ("aeiouyåäö")

konsonanter = "bcdfghjklmnpqrstvwxz"

#userString = "Hej! Kom in."
userString = input("Skriv en text:")

newString = " "

for c in userString:
    if konsonanter.find(c.lower()) != -1:
        newString += f"{c}o{c}"
    else:
        newString += c

print(newString)