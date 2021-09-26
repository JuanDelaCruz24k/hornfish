from math import sqrt
from timeit import timeit


def isPrime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def getNthPrime(n):
    cnt = 0
    num = 2
    while True:
        if isPrime(num):
            cnt = cnt + 1
            if cnt == n:
                return num
        num = num + 1

def ordinalPosA(n):
    return str(n) + {1: 'st', 2: 'nd', 3: 'rd'}.get(4 if 10 <= n % 100 < 20 else n % 10, "th")

'''
#Python3.6 + only
def ordinalPosB(n):
  s = ('th', 'st', 'nd', 'rd') + ('th',)*10
  v = n%100
  if v > 13:
    return f'{n}{s[v%10]}'
  else:
    return f'{n}{s[v]}'
'''

if __name__=='__main__':

    x = int(input('Enter : '))
    if(x>0):
        t = timeit('getNthPrime(x)', globals=globals(), number = 1)
        print(ordinalPosA(x),
                ' Prime Number is :', 
                "{:,}".format(getNthPrime(x)), 
                '| Execution time:',
                "{:.8f}".format(t), 'sec(s)')
    else:
        print("Please Enter a Number greater than zero.")