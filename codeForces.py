# ### 693 - C
# # 1 ---
# def Cards(w, h, n):
#     res = 1
#     while w %2 == 0:
#         w /= 2
#         res +=1
#     while h % 2 ==0:
#         h /= 2
#         res += 1
#     return True if res >= n else False        


# # print(Cards(5 , 10 , 3))
# # def Cards(w, h, n):
# #     count = 0
# #     if n == 1:
# #         return True
# #     elif (w*h) % 2 == 0:
# #         temp = w*h
# #         while temp % 2 == 0:
# #             temp = temp // 2
# #             count += 1

# #     if count * 2 >= n:
# #         return  True
# #     return False

# # if __init__ = '__main__':
# #     t = int(input())
# #     for _ in range(t):
# #         w , h , n = map(int , input().strip())
# #         if Cards(w , h , n ):
# #             print("Yes")
# #         else:
# #             print("No)
# # def fair(n , arr):
# #     sum1 =  0
# #     sum2 = 0
# #     for i in range(n):
# #         if arr[i] == 1:
# #             sum1 += 1
# #         else:
# #             sum2 += 1   
# #     if sum1 % 2 == 0 and sum2 % 2 == 0 and n % 2 == 0:
# #         print('YES')    
# #     else:
# #         print('NO')    
# def LongJump(arr , n):
#     maxSum = 0
#     for i in range(n):
#         currentSum = 0
#         j = i 
#         while j < n:
#             currentSum += arr[j]
#             j += arr[j]


#         if currentSum > maxSum:
#             maxSum = currentSum

#     print(maxSum)

# # a = [7 , 3 , 1 , 2 , 3]
# # a = [2 , 1 , 4]
# a = [1, 1 , 1 , 1 ,1]
# LongJump(a , 5)
### 690(3)
## Problem 1
# def sortOrder(arr , n):
#     i , j = 0 , 0
#     arr1 = [0]*n
#     while j < n :
#         arr1[j] = arr[i]
#         j += 2  
#         i += 1
#     j = j -1        
#     while i < n and j > 0:
#         j -= 2
#         arr1[j] = arr[i]    
#         i += 1
#     print(*arr1)

# #arr = [3 , 4 , 5 , 2 , 9 , 1 , 1]    
# #arr = [9 , 2 , 7 , 1]
# # arr = [8, 4, 3, 1, 2, 7, 8, 7, 9, 4, 2]
# # #arr = [11]
# # sortOrder(arr , 11)
# # def check(arr,k):
# #     for i in arr:
# #         if i > k:
# #             return False
# #     return True        
        
# # def sumLessK(arr,n,k):
# #     arr.sort()
# #     i , j  = 0 , n-1
# #     while(i < j):
# #         if arr[i] + arr[j] <= k:
# #             return True
# #         else:
# #             j -= 1
# #     return False
# # def main(arr , n , k):
# #     if (check(arr , k)) or (not check(arr,k) and sumLessK(arr,n,k)):
# #         print("YES")
# #     else:
# #         print("NO")
# # arr = [2,3,2,5,4]
# # arr = [2,1,5,3,6]
# #arr = [3,1,1]
# # print(main(arr,3,2))
# # def lcmString(s1 , s2):
# #     return s1 + s2
# # print(lcmString('abab' , 'ab'))    
# # Problem 694 (2)
# # StrangePartition
# import math
# def minMax(arr , n , x):
#     max = 0
#     min = 0
#     for i in arr:
#         max += math.ceil(i / x)
#     sum = arr[n-1]
#     i = n - 2
#     j = n -2
#     sumNext = 0
#     while j >= 0:
#         if (sum + arr[j]) % x == 0:
#             sum += arr[j]
#             i = j
#             j -= 1
#         else:
#             sum += arr[j]    
#             j -= 1
#     for k in range(i):
#         min += math.ceil(arr[k] / x)
#     for k in range(i,n):
#         sumNext += arr[k]   
#     min += math.ceil(sumNext / x )   
#     print(min , max)

# #arr = [3,6,9]
# #arr = [6,4,11]
# arr = [66,26,23,13,25,53,24,65,25]
# #arr = [91, 62, 22, 17, 13]
# minMax(arr,8,93)

## Problem - 280(2)
# def lantern(arr,n,m):
#     arr.sort()
#     max = 0
#     for i in range(n-2):
#         if arr[i + 1] - arr[i] > max:
#             max = arr[i+1] - arr[i]
#     return max / 2
# arr = [15,5,3,7,9,14,0]            
# print(lantern(arr,7,15))
## Problem 
# def LotMoney(n):
#     count = 0
#     temp = n
#     while temp != 0:
#         if temp >= 100 :
#             count += (temp // 100)
#             temp = temp % 100
#         elif temp >= 20:
#             count += (temp // 20)
#             temp = temp % 20
#         elif temp >= 10:
#             count += (temp // 10)
#             temp = temp % 10    
#         elif temp >= 5:
#             count += (temp // 5)
#             temp = temp % 5
#         else:
#             count += temp
#             temp  = 0
#     return count        
# print(LotMoney(1000000000))
# Python3 implementation of the approach 
# import math 
# def isPrime(n): 
# 	if(n <= 1): 
# 		return False
# 	if(n <= 3): 
# 		return True
	
# 	if(n % 2 == 0 or n % 3 == 0): 
# 		return False
	
# 	for i in range(5,int(math.sqrt(n) + 1), 6): 
# 		if(n % i == 0 or n % (i + 2) == 0): 
# 			return False
# 	return True

# def nextPrime(N): 
# 	if (N <= 1): 
# 		return 2

# 	prime = N 
# 	found = False
# 	while(not found): 
# 		prime = prime + 1

# 		if(isPrime(prime) == True): 
# 			found = True

# 	return prime 
# def Findnumber(d):    
#     number = d + 1
#     temp1 = nextPrime(number) if not isPrime(number) else number
#     temp1 = nextPrime(temp1 +d) if not isPrime(number) else temp1 +d
#     return temp1 * temp2

# print(Findnumber(n))
### 1459 A
def check(str1,str2):
    c1=0
    c2=0
    for i in range(len(str1)):
        if int(str1[i]) > int(str2[i]):
            c1 += 1
        elif int(str1[i]) < int(str2[i]): 
            c2 += 1    
        else:
            c1 += 1
            c2 += 1    
    if c1 > c2:
        print("RED")
    elif c1 < c2:
        print("BLUE")        
    else:
        print("EQUAL")   

s1="777"
s2="111"
check(s1,s2)
