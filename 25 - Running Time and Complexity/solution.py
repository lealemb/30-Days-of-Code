import math

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, max_divisor + 1, 2):
        if n % d == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    n = int(input())
    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")
