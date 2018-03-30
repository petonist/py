def isprime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
        
    else:
        return True

n = 5
if isprime(n):
    print(f"{n} ON algarv")
else:
    print(f"{n} EI OLE algarv")

def list_primes(max_num = 100):
    for n in range(2, max_num):
        if isprime(n):
            print(n, end = '', flush = True)
    print()

list_primes()