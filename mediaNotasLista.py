def media():
    soma = 0
    totaln = int(input("Digite o numero de notas: "))
    for i in range(0, totaln):
        n = float(input("Digite as notas: "))
        soma += n
    print (soma / totaln)

media()
