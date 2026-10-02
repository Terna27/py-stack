import sys


def is_prime(num):

    if num < 2 :
        return False
    
    for n in range(2, num):
        if num % n == 0:
            return False

    return True 

if len(sys.argv) != 2:
    print(0)
    sys.exit()

try:
    num = int(sys.argv[1])
except ValueError:
    print(0)
    sys.exit()

if num < 0 :
    print(0)
    sys.exit()

total = 0

for x in range(2, num + 1):
    if is_prime(x):
        total += x
print(total)