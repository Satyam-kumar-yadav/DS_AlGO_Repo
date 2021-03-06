#### CodeForces - https://www.codechef.com/wiki/tutorial-dynamic-programming
### Problem 1 - On a positive integer, you can perform any one of the following 3 steps. 1.) Subtract 1 from it. ( n = n - 1 )  , 2.) If its divisible by 2, divide by 2. ( if n % 2 == 0 , then n = n / 2  )  , 3.) If its divisible by 3, divide by 3. ( if n % 3 == 0 , then n = n / 3  ). Now the question is, given a positive integer n, find the minimum number of steps that takes n to 1

###eg: 1.)For n = 1 , output: 0       2.) For n = 4 , output: 2  ( 4  /2 = 2  /2 = 1 )    3.)  For n = 7 , output: 3  (  7  -1 = 6   /3 = 2   /2 = 1 )
#---------------------------------------------------------------------------##---------------------------------------------------------------------------#
#---------------------------------------------------------------------------##---------------------------------------------------------------------------#
# def firstDp(n):
#     dp = [0]*(n+1)
#     if n == 1:
#         dp[1] = 0
#     for i in range(2,n+1):
#         dp[i] = 1 + dp[i-1]    
#         if i %2 == 0:
#             dp[i] = min(dp[i],1+dp[i//2])
#         if i %3== 0:
#             dp[i] = min(dp[i],1+dp[i//3])    
#     return dp[n]
# print(firstDp(10))    
#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#
# def liS(arr,n):
#     dp = [1]*(n+1)
#     for i in range(len(arr)):
#         for j in range(i):
#             if arr[i] > arr[j] and dp[i] < dp[j] + 1:
#                 dp[i] = 1 + dp[j]
#     max = 0            
#     for i in range(len(dp)):
#         if dp[i] > max:
#             max = dp[i]
#     return max
# arr = [10, 22, 9, 33, 21, 50, 41, 60] 
# print(liS(arr,8))
#---------------------------------------------------------------------------#
### Coin Change
# def CoinChange(S,m,n,i,sum):
#     if sum == 0 :
#         return 1
#     if i > m-1 or sum< 0:
#         return 0
#     left = CoinChange(S,m,n,i,sum-S[i])     
#     right = CoinChange(S,m,n,i+1,sum)
#     return left + right
# print(CoinChange([1,2,3],3,4,0,4))    
##DP
# def CoinChange(S,m,n,i,sum):
#     dp =[[-1 for i in range(sum+1)] for j in range(m+1)]
#     if sum == 0 :
#         return 1
#     if i > m-1 or sum< 0:
#         return 0
#     if dp[i][sum] != -1:
#         return dp[i][sum]    
#     left = CoinChange(S,m,n,i,sum-S[i])     
#     right = CoinChange(S,m,n,i+1,sum)
#     dp[i][sum] =  left + right
#     return dp[i][sum]
### 
# def CoinChange(S,m,n):
#     # dp = [0]*(n+1)
#     # dp[0] = 1
#     # for i in range(len(S)):
#     #     for j in range(len(dp)):
#     #         if S[i] <= j:
#     #             dp[j] += dp[j-S[i]]
#     # return dp[n]          

# print(CoinChange([1,5,10],3,12))    
#### 0-1 Knapsack Problem
# def Knapsack(weight,value,W,N):
#     if N == 0 or weight == 0:
#         return 0
#     if weight[N-1] > W:
#         return Knapsack(weight,value,W,N-1)
#     else:
#         return max(value[N-1] + Knapsack(weight,value,W-weight[N-1],N)      
     



# def factorail(n):
#     dp = [1]*(n+1)
#     for i in range(1,n+1):
#         dp[i] = i*dp[i -1]
#     return dp[n]    

# def nCr(n):     
#     return int(factorail(n) / (factorail(n-2)*2))

# print(nCr(3) +1)
### Friends Pairing Problem
# def findPair(n):
#     if n <= 1:
#         return 1
#     return findPair(n-1) + (n-1)*findPair(n-2)   
# print(findPair(3))
# def findPair(n):
#     # dp = [0 for i in range(n+1)]
#     # dp[0] = 1
#     # dp[1] = 1
#     # for i in range(2,n+1):
#     #     dp[i] = dp[i-1] + (i-1)*dp[i-2] 
#     # return dp[n]
# print(findPair(4))        

### 419
### GoldMineProblem
# def GoldMineProblem(mat,n,m):
#     dp = [[0 for i in range(m+1)] for j in range(n+1)]
#     for i in range(1,n+1):
#         dp[i][m] = mat[i-1][m-1] 
#     for i in range(m-1,0,-1):    
#         for j in range(1,n+1):
#             if j == n:
#                 dp[j][i] = mat[j-1][i-1] +  max(dp[j-1][i+1],dp[j][i+1])
#             else:    
#                 dp[j][i] = mat[j-1][i-1] + max(dp[j-1][i+1],dp[j][i+1],dp[j+1][i+1])    
#     max_val = 0            
#     for i in range(n+1):
#         for j in range(m +1):
#             if dp[i][j] > max_val:
#                 max_val = dp[i][j]
#     return max_val


# mat =  [[1, 3, 1, 5],
#         [2, 2, 4, 1],
#         [5, 0, 2, 3],
#         [0, 6, 1, 2]];
mat = [[10, 33, 13, 15],
                  [22, 21, 4, 1],
                  [5, 0, 2, 3],
                  [0, 6, 14, 2]];
print(GoldMineProblem(mat,4,4))     


