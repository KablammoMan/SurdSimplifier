import math
import time

def meth1(num):
    start = time.time()
    i = 2
    pot = 1
    while i**2 <= num/2:
        if num % (i**2) == 0:
            pot = i
        i+=1
    end = time.time()
    print(f"{i} Possibles Tested")
    print(f"sqrt({num}) = {pot} * sqrt({int(num / pot**2)})")
    print(f"Took: {end-start}s")
    print(f"")

def meth2(num):
    start = time.time()
    i = int(math.sqrt(num/2))
    pot = 1
    while True:
        if num % (i**2) == 0:
            pot = i
            break
        i-=1
    end = time.time()
    print(f"{int(math.sqrt(num))-i} Possibles Tested")
    print(f"sqrt({num}) = {pot} * sqrt({int(num / pot**2)})")
    print(f"Took: {end-start}s")

num = int(input("Enter number under surd: "))
print("Method 1")
meth1(num)
print("\nMethod 2")
meth2(num)