import random

def DNA(length):
    return ''.join(random.choice('acgt') for _ in range(length))

for i in range(1000):
  print (DNA(1000))
