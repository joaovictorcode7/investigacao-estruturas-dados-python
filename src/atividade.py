import random

def bubble_sort(lista):
    comparacoes = movimentos = 0
    for i in range(len(lista) - 1):
        trocou = False
        for j in range(len(lista) - 1 - i):
            comparacoes += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                movimentos += 1
                trocou = True
        if not trocou:
            break
    return comparacoes, movimentos


def quick_sort(lista):
    comparacoes = movimentos = 0

    def ordenar(inicio, fim):
        nonlocal comparacoes, movimentos
        if inicio >= fim:
            return
        pivo = lista[fim]
        i = inicio
        for j in range(inicio, fim):
            comparacoes += 1
            if lista[j] <= pivo:
                if i != j:
                    lista[i], lista[j] = lista[j], lista[i]
                    movimentos += 1
                i += 1
        if i != fim:
            lista[i], lista[fim] = lista[fim], lista[i]
            movimentos += 1
        ordenar(inicio, i - 1)
        ordenar(i + 1, fim)

    ordenar(0, len(lista) - 1)
    return comparacoes, movimentos


def busca_matriz(matriz, valor):
    comparacoes = 0
    for linha in matriz:
        for elemento in linha:
            comparacoes += 1
            if elemento == valor:
                return comparacoes
    return comparacoes


def experimento_ordenacao():
    print("\n=== ORDENACAO ===")
    for tamanho in [10, 20, 1000]:
        random.seed(12345 + tamanho)
        dados = [random.randint(0, 9999) for _ in range(tamanho)]

        b = dados.copy()
        q = dados.copy()
        cb, mb = bubble_sort(b)
        cq, mq = quick_sort(q)

        print(f"{tamanho} elementos:")
        print(f"  Bubble Sort: {cb} comparacoes, {mb} movimentos")
        print(f"  Quick Sort:  {cq} comparacoes, {mq} movimentos")


def experimento_busca():
    print("\n=== BUSCA EM MATRIZES ===")
    for n in [2, 10, 100]:
        matriz = [[i * n + j + 1 for j in range(n)] for i in range(n)]
        total = n * n
        print(f"Matriz {n}x{n}:")
        print("  Inicio:", busca_matriz(matriz, 1))
        print("  Final:", busca_matriz(matriz, total))
        print("  Inexistente:", busca_matriz(matriz, -1), "comparacoes")


def vetor_temperaturas():
    temperaturas = [float(input(f"Temperatura {i + 1}: ")) for i in range(10)]
    media = sum(temperaturas) / len(temperaturas)
    maior, menor = max(temperaturas), min(temperaturas)

    print("\nTemperaturas:", temperaturas)
    print(f"Media: {media:.2f}")
    print(f"Maior: {maior:.2f} | indices: {[i for i,x in enumerate(temperaturas) if x == maior]}")
    print(f"Menor: {menor:.2f} | indices: {[i for i,x in enumerate(temperaturas) if x == menor]}")
    print("Acima da media:", sum(x > media for x in temperaturas))


def matriz_sensores():
    sensores = []
    for i in range(5):
        linha = []
        for j in range(24):
            linha.append(float(input(f"Sensor {i+1}, hora {j+1}: ")))
        sensores.append(linha)

    maior = sensores[0][0]
    si = hi = 0
    for i in range(5):
        for j in range(24):
            if sensores[i][j] > maior:
                maior, si, hi = sensores[i][j], i, j

    media = sum(sum(linha) for linha in sensores) / 120
    limite = float(input("Limite de temperatura: "))
    acima = sum(valor > limite for linha in sensores for valor in linha)

    print(f"Maior: {maior:.2f} | sensor: {si+1} | hora: {hi+1}")
    print(f"Media geral: {media:.2f}")
    print("Acima do limite:", acima)


def main():
    print("=== INVESTIGACAO EXPERIMENTAL ===")
    print("1 - Ordenacao")
    print("2 - Busca em matrizes")
    print("3 - Vetor de temperaturas")
    print("4 - Matriz de sensores")
    opcao = input("Escolha: ")

    if opcao == "1":
        experimento_ordenacao()
    elif opcao == "2":
        experimento_busca()
    elif opcao == "3":
        vetor_temperaturas()
    elif opcao == "4":
        matriz_sensores()
    else:
        print("Encerrado.")


if __name__ == "__main__":
    main()
