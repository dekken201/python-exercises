n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))

if n1 > n2 and n1 > n3:
    print("O maior número digitado é o primeiro, %d" % n1)
if n2 > n1 and n2 > n3:
    print("O maior número digitado é o segundo, %d" % n2)
if n3 > n1 and n3 > n2:
    print("O maior número digitado é o terceiro, %d" % n3)
if n1 < n2 and n1 < n3:
    print("O menor número digitado é o primeiro, %d" % n1)
if n2 < n1 and n2 < n3:
    print("O menor número digitado é o segundo, %d" % n2)
if n3 < n2 and n2 < n2:
    print("O menor número digitado é o terceiro, %d" % n3)