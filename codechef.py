### CodeChef jan long
### Div 3
### Problem 1
# def contest(arr , N , K , D):
#     sum = 0
#     temp = 0
#     for i in range(N):
#         sum += arr[i]

#     if K * D < sum:
#          temp = D
#     else:
#         temp = sum // D

#     return temp       

# n = 2 
# m = 5 
# d = 7
# arr = [20,  36 ]
# print(contest(arr , n , m , d))
import math 
def isPrime(n): 
	if(n <= 1): 
		return False
	if(n <= 3): 
		return True
	
	if(n % 2 == 0 or n % 3 == 0): 
		return False
	
	for i in range(5,int(math.sqrt(n) + 1), 6): 
		if(n % i == 0 or n % (i + 2) == 0): 
			return False
	return True

def final(n):
    count = 0
    i = 3
    while i <= n:
        if isPrime(i):
            if isPrime(i + 2) and i + 2 < n:
                count += 1
        i += 2
    return count    
print(final(14))


# def solve(n):
#     sieve = [True] * (n + 1)
#     primes = []
#     for i in range(2, n + 1):
#         if sieve[i]:
#             primes.append(i)
#             for j in range(i, n + 1, i):
#                sieve[j] = False
#     count = 0
#     for i in range(len(primes)):
#             if (primes[i] + 2) in  primes:
#                 count += 1      
#     return count
# print(solve(10))        
