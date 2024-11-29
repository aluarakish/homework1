def is_prime(n: int) -> bool:

    if n < 2:
        return False
  
    i = 2
    while i * i <= n: 
        if n % i == 0: 
            return False
        i += 1 

    return True  

print(is_prime(11))  
print(is_prime(4))   
