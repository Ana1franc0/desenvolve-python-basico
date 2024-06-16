n1 = float(input("Digite o primeiro número decimal: "))
n2 = float(input("Digite o segundo número decimal: "))

diferença_absoluta = abs(n1 - n2)
diferença_arredondada = round(n1 - n2)

print(f"A diferença absoluta entre {n1} e {n2} é {diferença_absoluta}")
print(f"A diferença arredondada entre {n1} e {n2} é {diferença_arredondada}")
