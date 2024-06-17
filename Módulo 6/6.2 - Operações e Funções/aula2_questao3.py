import random

Lista1, Lista2 = [], []
for i in range(20):
    Lista1.append(random.randint(0, 50))
    Lista2.append(random.randint(0, 50))

print(sorted(Lista1))
print(sorted(Lista2))

inters = []
for elemento in Lista1:
    if elemento in Lista2 and elemento not in inters:
        inters.append(elemento)

inters.sort()
for i in inters:
    print(f"{i}: {Lista1.count(i)}, {Lista2.count(i)}")