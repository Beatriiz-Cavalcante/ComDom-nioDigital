'''Faça um código para ler um valor N qualquer (que será o tamanho dos vetores). Após, ler dois
vetores A e B (de tamanho N cada um) e depois armazenar em um terceiro vetor Soma a soma
doselementos do vetor A com os do vetor B (respeitando as mesmas posiçôes) e escrever o 
vetor soma '''

tamanho = int(input("Digite o tamanho do vetor: "))
A = [0, 0, 0]
B = [0, 0, 0]
Soma = [0, 0, 0]

print("Vamos criar o vetor A")
for c in range(tamanho):
    A[c] = float(input("Digite o numero a ser guardado: "))

print("Vamos criar o vetor B")
for c in range(tamanho):
    B[c] = float(input("Digite o numero a ser guardado: "))


print("A soma dos vetores criados é:")
for s in range(tamanho):
    Soma[s] = A[s] + B[s]
    print(Soma[s], end=" ")