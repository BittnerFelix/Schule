'''
y=0
while y==0:
    x = int(input())
    if 1<= x <= 100:
        if x%2==0:
            print("Ganze Zahl")
            y+=y
        else:
            print("Ungerade Zahl")
            y+=y
    else:
        print("Error")


x = float(input("start Geld: "))
y = float(input("Zinssatz: "))
z = int(input("Jahre: "))
a = 0
c = 1
ic = float(0)

while a != z:
    ic+=(x*(y*0.01))
    x=x+(x*(y*0.01))
    a=a+1
    
    if a==z:
        print("nach ",a," Jahren- ist ihr Kontostand: ",round(x,2),"€")
        print("Nur Zinsgewinne: ",round(ic,2),"€")
 
betrag = float(input("Betrag: "))
jahre = int(input("Jahre: "))
zinssatz = float(input("Zinssatz: "))

for i in range(jahre):
    betrag = betrag * (1+zinssatz/100)
    print(betrag)

i = 0
while i < jahre:
    betrag = betrag * (1+zinssatz/100)
    print(betrag)
    i += 1

a=5
print(type(a))
a = a/3
print(a)
print(type(a))
'''
'''
a = 100
print(a)
print(f"Binär: {a:b}")
print("Binär: {:b}".format(a))
b = 0x5A3F
print(b)
print(f"Hexa: {a:x}")
c = 0o2471
print(c)
print(f"Oktal: {a:o}")

'''
'''
a=12
b=12
if type(b) == type(a):
    print("Gleich", type(b))
else:
    print("ungleich")
    print("Erste Zahl: ",type(a))
    print("Zweite Zahl: ",type(b))
   


a= input("Erste Binäre Zahl: ")
b= input("zweite Binäre Zahl: ")

c= int(a,2)
d= int(b,2)
e= c & d

print("Ergebnis: ", e)
print("Binär: {:b}".format(e))
'''
'''



'''




'''
liste1 = [1,4,6,22]
liste2 = ["Kuchen", "Kekse",99]
liste3 = [i for i in range(10,20,3)]
#print(liste3)
del liste2[1]
print(liste2)
print(liste2[-1]) #Zählt von hinten

if "Kuchen" in liste2:
    print("Kuchen izz da")
else:
    print("Wo zur Hölle ist der Kuchen???????")

for i in range(6):
    liste1.append(i**2)
print(liste1)
'''
'''
word1=input("Wort 1:")
word2=input("Wort 2:")
word3=input("Wort 3:")
word4=input("Wort 4:")
word5=input("Wort 5:")

list1=[word1,word2,word3,word4,word5]

search= input("Suche: ")

if search in list1:
    print(search)
    print(list1.count(search))
'''
'''
#' Zahlen Suche
list1=[]
n=int(input("Wie viele Zahlen?: "))
for i in range(n):
    temp = input(f"Zahl {i+1} :")
    list1.append(temp)

search= input("Suche: ")

stelle = [ i for i in range(len(list1)) if list1[i] == search ]
if search in list1:
    print("Gesuchte Zahl:", search)
    print("Anzahl der Gesuchten Zahl:", list1.count(search))
    print("Die Zahl wurde an der/den stelle/n", stelle, "gefunden" )
else:
    print("Die Zahl ist nicht in der Liste")
'''
'''
list1=[]
z = 0

n = int(input('Anzahl: '))

for i in range(n):
temp = int(input(f"Zahl {i+1} :"))
list1.append(temp)

search= int(input("Suche: "))

for i in range(n):
if list1[i] == search:
print(f'Zahl {search} wurde an Stelle {i+1} gefunden')
z += 1

print(f'Zahl {search} kommt {z} mal vor.')
'''
'''
# Wort Suche
list2=[]
n=int(input("Wie viele Wörter?: "))
for i in range(n):
    temp = input(f"Wort {i+1} :")
    list2.append(temp)

search= input("Suche: ")

if search in list2:
    print("Gesuchtes Wort:", search)
    print("Anzahl der Gesuchten Wörter in der Liste:", list2.count(search))
else:
    print("Das Wort exestiert nicht")
'''
'''
#"Manuelle Suche" ohne Funktion
list3=[]
counter = 0
n=int(input("Wie viele Wörter?: "))
for i in range(n):
    temp = input(f"Wort {i+1} :")
    list3.append(temp)

search= input("Suche: ")

for i, element in ennumerate(list3):
    if element == search:
        counter += 1
        print(i)

print(f"Anzahl ")
'''
'''
liste = ["Wurst", "Döner", "Cola"]
liste2= ["Test", "Lul", "Lul"]
liste3= [liste, liste2]
print(liste3)
print(liste3[1] [2])
liste4= [0,1,2]
print(liste3[liste4[0]][liste4[0]])







#
#liste3 = zip(liste, liste2)
#for i in liste3:
#   print(i)
#print(liste)
#del liste[2]
#print(liste)
#liste.pop(2)
#print(liste)



'''


'''
a = 6
b = 9

tupel1 = (a,b)
t2 = a ,b 
c, d =t2
print(c)
print(d)
print(type(c))
'''
'''
liste = ["Ralf", "Klaus", "Julia"]

eingabe = input("Name: ")

if not eingabe in liste:
    liste.append(eingabe)

print(liste)

'''
'''
s = {1,2,3,4}
t = {2,4,6,8}

u = {4,5,6}

x = s|t
print(x)
'''
'''
noten = {"Klaus":1.3, "Lisa":3.7}

for note in noten.items():
    print(f"{note[0]} hat eine {note[1]}")
    print(type(note))
    
if "Klaus" in noten:
    print("Ja")

if 2 in noten.values():
    print("x")
'''
'''
Namen=[]
Noten=[]
start = True
while start == True:
    temp1 = input(f"Name: ")
    if temp1 == "quit":
        start = False
        break
    Namen.append(temp1)
    temp2 = input("Note: ")
    Noten.append(temp2)

Notendict = dict(zip(Namen, Noten))
print(Notendict)

for note in Notendict.items():
    print(f"{note[0]} hat eine {note[1]}")
'''

'''
mein_String = "Kläuschen"
string2 = "Einen Langen und noch \v längeren Text schreiben " #Man kan hierbei über mehrere Zeilen schreiben
print(mein_String)
print(string2)

wort = mein_String[3:5]
print(wort)

if "Peter" in mein_String:
    print("Klaus ist da")
else:
    print("Peter ist nicht da")
'''
'''
mein_String = 'Kuchen, Kekse, Muffin'
liste = mein_String.split(" ")
s=""
for i in range(len(liste)-1,-1,-1):
    s+= liste[i]+" "
print(s)
'''
'''
mein_String = "Hallo Klaus und Klaus"

a  = mein_String.find("Klaus", 10, 21)
b = mein_String.count("Klaus")

string2 = mein_String.replace("Klaus", "Rudi")
string3 = mein_String.strip()
string4 = mein_String.isalnum()
print(string4)
'''
'''
liste = ["Julia", "Claudia", "Nadine"]
a= " und ".join(liste)

print(a)
'''
'''
a = 5
b = 10
print(f"a hat den Wert {a}, b hat den Wert {b}")

print("a hat den Wert {}, b hat den Wert {}".format(a, b))
print("a hat den Wert {x}, b hat den Wert {y}".format(x = a, y = b))

'''

'''

Mail = input("Email: ")
if "@" in Mail:
    if Mail.count("@") == 1:
        Domain = Mail.split("@")
        print(Domain)
        if "." in Domain[1] and Domain[0] != "" and Domain[1] != ".":
            print("Email gültig")
        else: 
            print("Email ungültig, Domain fehlt, oder Name fehlt")
    else:
        print("Ungültig, zu viele @")
else:
    print("Email ungültig, @ fehlt!")
    '''
''' 
def summe(x, y):
    z = x+y
    print(f"Summe: {z}")
    
a = int(input("Zahl 1: "))
b = int(input("Zahl 2: "))

summe(a, b)
'''
'''
def summe(x, y):
    z = x+y
    return z

a = int(input("Zahl 1: "))
b = int(input("Zahl 2: "))

c = summe(a, b)

print(c)
'''
'''
def maxi(x, y):
    if x > y:
        Maximum = x
    else:
        Maximum = y
    return Maximum

def min(x, y):
    if x < y:
        Minimum = x
    else:
        Minimum = y
    return Minimum

a = int(input("Zahl 1: "))
b = int(input("Zahl 2: "))

Maximun = maxi(a, b)
Minimum = min(a, b)

print(f"Maximum: {Maximun}")
print(f"Minimum: {Minimum}")

'''
# Ganz großes Fragezeichen
'''
def max_min(x, y):
    ma = x if x > y else y
    mi = x if x < y else y

a = int(input("Zahl 1: "))
b = int(input("Zahl 2: "))

maximum, minimum = max_min(a, b)

print(maximum)
print(minimum)
'''
'''

def summe(Werte):
    temp = 0
    for i in Werte:
        temp += i
    return temp

tup = (6,9,7,6,4,5,1)
print(summe(tup))
'''
'''
def drucke_noten(**werte):
    for name, note in werte.items():
        print(f"{name}: {note}")

drucke_noten(Klaus = 4.0, Lisa = 2.3)
'''
'''

from math import *

print(sin(9))

''' 

'''
def hallo():
    print("Hallo")
    
hallo()
'''
'''
import Test_Mod

print(Test_Mod.x)
'''

# Aufgabenblatt 8 Nummer:3
'''
list=[]
a = int(0)
c = int(0)

def maxi():
    b = None
    for a in list:
        if b is None or a > b:
            b = a
    return b

def min():
    d = None
    for c in list:
        if d is None or c < d:
            d = c
    return d

n=int(input("Wie viele Zahlen?: "))
for i in range(n):
    temp = int(input(f"Zahl {i+1} :"))
    list.append(int(temp))

Maximun = maxi()
Minimum = min()


print(f"Maximum: {Maximun}")
print(f"Minimum: {Minimum} ")

'''


'''
try:
    eingabe = int(input("Ganze Zahl eingeben: "))
    print(2 / eingabe)
except ValueError:
    print("Das war keine ganze Zahl")
except ZeroDivisionError:
    print("Teilen mit null nicht möglich")
except:
    print("Ein unbekannter Fehler ist aufgetreten")

finally:
    print("Das wird immer ausgeführt")

'''
'''
try:
    dateiname = input("Dateiname: ")
    datei = open(dateiname, "r")
    for line in datei:
        print(line)

except FileNotFoundError:
    print("Datei nicht vorhanden")

except:
    print("Ein unbekannter Fehler ist aufgetreten vielleicht eine Falsche Dateiendung?")
    
    '''
'''  
def meinefunktion(*a):
    summe = 0
    for i in a:
        summe = summe + i
    return summe

print(meinefunktion(3,4,5,8,1))
'''
'''
wert = 5

quadrat = lambda x: x*x

print(quadrat(wert))
'''

#Bubblesort

def bubblesort(elements):
  # Looping from size of array from last index[-1] to index [0]
  for n in range(len(elements)-1, 0, -1):
    for i in range(n):
      if elements[i] > elements[i + 1]:
        # swapping data if the element is less than next element in the array
        elements[i], elements[i + 1] = elements[i + 1], elements[i]

elements = [39,12,18,85,72,10,2,18]
  
print("Unsorted list is,") 
print( elements)
bubblesort(elements)
print("Sorted Array is, ")
print(elements)