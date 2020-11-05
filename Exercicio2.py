def triangulo_pascal(n):
    for linha in range(1, n+1):
        num = 1
        linha_atual = []
        for i in range(1, linha+1):
            linha_atual.append(int(num))
            num = num * (linha-i) / i
        print(linha_atual)


triangulo_pascal(10)
