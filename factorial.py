#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320


def fat(n):
    fat = 1
    lista = range(1, n + 1)
    for x in lista:
        fat = x * fat
    return fat

n = int(input("Write the number wished to be factored: "))
print (fat(n))