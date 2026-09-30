import sys


if len(sys.argv) != 2:
    print(0)
    sys.exit()

num = int(sys.argv[1])

if num > 0:
   for numb in range(num):
        print(numb)
else:
    print("not valid")