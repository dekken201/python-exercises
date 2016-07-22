#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

lista = []
n = 2000
while n <= 3200:
    if n % 7 == 0 and n % 5 != 0:
        lista.append(n)
    n += 1
print (lista)