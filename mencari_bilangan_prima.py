def is_prima(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
            
    return True

def prima_terdekat(n):
    for i in range(n,0,-1):
        if is_prima(i):
            return i

# masukan bilangan 
n = int(input("Masukan bilangan: "))
print("Bilangan prima terdekat dari", n, "adalah", prima_terdekat(n))



