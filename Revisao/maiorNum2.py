maior = 0
for c in range(3):
    numero = int(input(f"Informe o número {c+1}: "))
    if numero > maior:
        maior = numero
print(maior)