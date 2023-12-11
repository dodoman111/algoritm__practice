def solution(n, k):
    def change(n, q):
        rev_base = ''
        while n > 0:
            n, mod = divmod(n, q)
            rev_base += str(mod)
        return rev_base[::-1] 

    def is_prime_number(x):
        if x < 2:
            return 0
        for i in range (2, int(x**(1/2)) + 1):	
            if x % i == 0:		
                return 0
        return 1
    return sum([is_prime_number(int(i)) for i in change(n,k).split('0') if i !=''])