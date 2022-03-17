def Sort(List):
    for n in range(len(List)-1, 0, -1):
        for i in range(n):
            if List[i] > List[i + 1]:
                List[i], List[i+1] = List[i+1], List[i]

Liste = []

Anzahl = int(input("Eingabe: "))
for i in range(Anzahl):
    temp = int(input(f"Zahl {i+1} :"))
    Liste.append(int(temp))
    
print(Liste)      
Sort(Liste)
print(Liste)
