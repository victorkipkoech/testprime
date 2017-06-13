def get_prime_numbers (n):
    not_a_prime=[]
    prime = []
    if type(n)!=int:
        raise TypeError
    for j in range(2,n):
        for i in range(2,j):
            if j % i == 0:
                not_a_prime.append(j)
    for i in range(2,n):
        if i not in not_a_prime:
            prime.append(i)
    return prime
print (get_prime_numbers(10))