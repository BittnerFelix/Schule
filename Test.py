"""
while True:
    a = float(input("Erste Zahl: "))
    b = float(input("Zweite Zahl: "))
    c = float(input("Dritte Zahl: "))
    d = float(input("Vierte Zahl: "))
    e = float(input("Fünfte Zahl: "))
    max_value = None
    number = [a,b,c,d,e]

    du = (a+b+c+d+e)/5

    for num in number:
        if (max_value is None or num > max_value):
            max_value = num
    print()
    print("Maximum: ", max_value)
    print("Durchschnitt: ", du)
    print()
    if input('Do you want to repeat(y/n)') == 'n':
        break
"""
"""
x = 10
if x > 5:
    print("groß")
    
elif x > 0:
    print("positiv")
else:
    print("negativ")    
    
"""
"""
x = -8
vorzeichen = 'positiv' if x > 0 else 'negativ'
print(vorzeichen)
"""
"""
eingabe = ''
a = 0
while eingabe != "x":
    if a > 0:
        print("Hallo")
    a = 1
    eingabe = input()
"""
"""
for i in range(10, 20, 2):
    print(i)

"""
print("Kommst du heute eigentlich auch rum?")