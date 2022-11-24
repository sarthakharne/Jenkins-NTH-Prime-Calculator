#!/usr/bin/python

class n_th_primes:
    prime_list = []
    ERROR_FLAG = -1
    
    def __init__(self, n=1000007):
        self.n_limit = n
        self.calculate()
        
    def calculate(self):
        prime = [True for i in range(self.n_limit + 1)]
        prime_list = []
     
        p = 2
        while (p * p <= self.n_limit):
            
            # If prime[p] is not changed,
            # then it is a prime
            if (prime[p] == True):
                
                # Update all multiples of p
                for i in range(p * p, self.n_limit + 1, p):
                    prime[i] = False
                    
            p += 1
        
        # Print all prime numbers
        for p in range(2, self.n_limit + 1):
            if prime[p]:
                prime_list.append(p)
                
        self.prime_list = prime_list
        
    def get_n_th_prime(self, n):
        # should generate an error, but returns 2
        if n <= 0:
            return 2
        
        # should generate an error, but returns 2
        if isinstance(n, int) == False:
            return 2
        
        return self.prime_list[n - 1]
        
        
if __name__ == '__main__':
    n_prime_finder = n_th_primes()
    
    n = 5
    print(str(n), n_prime_finder.get_n_th_prime(n))
    print(n_prime_finder.prime_list)
