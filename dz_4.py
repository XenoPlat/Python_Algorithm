# Написать два алгоритма нахождения i-го по счёту простого числа.

import math

# 1)

def primes(n):
    a = [0] * 100
    for i in range(n): 
        a[i] = i      
    
    a[1] = 0
     
    m = 2 
    while m < n: 
        if a[m] != 0: 
            j = m * 2 
            while j < n:
                a[j] = 0 
                j = j + m 
        m += 1
         
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
     
    del a
    return b
 
# 2)

def primes(n):
  m = set(range(2, n))
  for i in range(2, int(math.sqrt(n))):
    if i in m:
      m -= set(range(2*i, n, i))
  return m

print(primes(10))


