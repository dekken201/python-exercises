#descobre se, seguindo as dimensões da forma geométrica,
#tal forma é ou não um triângulo, e define o mesmo.

a = int(input("Digite o primeiro lado do seu possível triângulo: "))
b = int(input("Digite o segundo lado do seu possível triângulo: "))
c = int(input("Digite o terceiro lado do seu possível triângulo: "))

if (a < b + c) and (b < a + c) and (c < a + b):
    print("Segundo essas dimensões, é um triângulo.\n Veremos de que tipo ele é agora.\n")

    if (a == b) and (b == c) and (c == a):
        print ("Seu triângulo é equilátero.")
    elif (a != b) and (b != c) and (c != a):
        print("Seu triãngulo é escaleno.")
    else:
        print("Seu triângulo é isósceles.")
else:
    print('\nInfelizmente, nao é um triângulo. Tente novamente.')
