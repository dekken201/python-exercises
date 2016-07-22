#Creates a random 10 integers lists and shows which number is highest and lowest.
import random
n = []
x = 0
n = random.sample(range(100), 10)
print (n)
print("O maior numero da lista e: %d" % max(n))
print("O menor numero da lista e: %d" % min(n))
