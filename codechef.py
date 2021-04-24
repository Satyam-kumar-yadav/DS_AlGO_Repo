# CodeChef jan long
# Div 3
# Problem 1
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

# def final(n):
#     count = 0
#     i = 3
# #     while i <= n:
# #         if isPrime(i):
# #             if isPrime(i + 2) and i + 2 < n:
# #                 count += 1
# #         i += 2
# #     return count
# # print(final(14))


# # def solve(n):
# #     sieve = [True] * (n + 1)
# #     primes = []
# #     for i in range(2, n + 1):
# #         if sieve[i]:
# #             primes.append(i)
# # #             for j in range(i, n + 1, i):
# # # #                sieve[j] = False
# # # #     count = 0
# # # #     for i in range(len(primes)):
# # # #             if (primes[i] + 2) in  primes:
# # # #                 count += 1
# # # #     return count
# # # # print(solve(10))
# # # feb Long Challenge
# # # def max(N):
# # # 	i = 10
# # # 	while N % i != 0:
# # # 		i -=1
# # # 	return i
# # # print(max(24))
# # # def maxSum(arr):
# # # 	arr.sort()
# # # 	x = arr[0]
# # # 	z = arr[-1]
# # # 	y = arr[len(arr) // 2]
# # # 	return abs(x-y) + abs(x-z) + abs(y-z)
# def check(string):
#     if string.split(" ")[-1] == 'AM':
#         x = string.split(":")[0]
#         if x == "12":
#             x = '00'
#     else:
#         x = int(string.split(":")[0])
#         if x < 12:
#             x = int(string.split(":")[0]) + 12
#     return str(x) + string[2:-3]
# from datetime import datetime
# def time(str1, str2, str3):
#     str1 = check(str1)
#     str1 = datetime(2000,12,5,hour = int(str1.split(":")[0]),minute=int(str1.split(":")[1]))    
#     str2 = check(str2)
#     str2 = datetime(2000,12,5,hour = int(str2.split(":")[0]),minute=int(str2.split(":")[1]))    
#     str3 = check(str3)
#     str3 = datetime(2000,12,5,hour = int(str3.split(":")[0]),minute=int(str3.split(":")[1]))

#     if str1 >= str2 and str1 <= str3:
#         return 1
#     return 0    
    # if (int(str1.split(":")[0]) >= int(str2.split(":")[0])):
    #     if (int(str1.split(":")[1]) >= int(str2.split(":")[1])):
    #         if (int(str1.split(":")[0]) <= int(str3.split(":")[0])):
    #             if (int(str1.split(":")[1]) <= int(str3.split(":")[1])):
    #                 return 1
    # return 0
# print(time("12:01 AM","11:59 AM","11:59 PM"))

# t = int(input())
# for _ in range(t):
#     n = input()
#     m = int(input())
#     result = ''
# #     for k in range(m):
# #         str1 , x , str2 , y = map(str,input().split(" "))
# #         str1 = str1 + " " + x
# #         str2 = str2 + " " + y
# #         print(str1,str2)

# #         result += str(time(str(n),str1,str2))
# # print(result)
# # string = "AB C  DEFH"
# # print(string.split( ))
# # def greedy(n, weight, value):
# #     arr = []
# #     count = 0
# #     for i in range(n):
# #         arr.append([weight[i], value[i], i])
# #     for i in range(1, n):
# #         if arr[i][2] < arr[i-1][2]:
# #             while arr[i][2] <= arr[i-1][2]:
# #                 arr[i][2] += arr[i][1]
# #                 count += 1
# #     return count

# def greedy(n, weight, value):
#     dict = {}
#     count = 0
#     for i in range(n):
#         dict[weight[i]] = [value[i],i]
#     for k in range(2,n+1):
#         if dict[k][1] < dict[k-1][1]:
#             while dict[k][1] <= dict[k-1][1]:
#                 dict[k][1] += dict[k][0]
#                 count += 1
#     return count
# # weight = [3, 1, 2]
# # value = [1, 4, 5]
# weight = [1,2,2]
# value = [5,6,7]
# # weight = [3,2,1]
# # value = [1,1,1]
# print(greedy(2, weight, value))

# def checkFirst(str1,str2):
#     if str1[0] == str2[0]:
#         return True
#     return False

# def last(str1,str2):
#     if str1[1:] == str2[1:]:
#         return True
#     return False
# def solution(arr,n):
#     arr1 = []
#     count = 0
#     for i in range(n-1):
#         for j in range(i+1,n):
#             if not checkFirst(arr[i] ,arr[j]):
#                 if not last(arr[i],arr[j]):
#                     arr1.append([arr[i],arr[j]])
#     for k in range(len(arr1)):
#         x = arr1[k][1][0] + arr1[k][0][1:]
#         y = arr1[k][0][0] + arr1[k][1][1:]
#         if x not in arr and y not in arr:
#             count += 1
#     return count*2

# arr = ['hell','bell',"best",'test']
# print(solution(arr,4))

# arr = [["str1","str2"] , ["bore1","bore2"]]
# print(arr[0][1][0] + arr[1][1][1:])
# ### Number with y prime factor

# def factorail(n):
#     dp = [1]*(n+1)
#     for i in range(1,n+1):
#         dp[i] = i*dp[i -1]
#     return dp[n]
# def anyoneWin(x,y):
#     if factorail(x) % 6 == 0:
#         return 1
#     return 0    
#def divyam(x,y):
#    if x <= y:
#        return 0
#    return 1    
### March long challengw
#def first(n,h,x,arr):
#    for i in range(n):
#        if x + arr[i] >= h:
#            return True
#    return False

#n,m,k = map(int,input().split())
##n = 22 6
##m = 5
##k = 3
#arr = list(map(int,input().strip().split()))
#print("Yes" if first(n,m,k,arr) else "No")

#def chefFriend(str1):
#    count = 0
#    for i in range(len(str1)):
#        if str1[i] == '1' and i == 0:
#            count = 1
#        elif str1[i] == '1':
#            if str1[i-1] == '0':
#                count += 1

#    return count 
#print(chefFriend('101'))
#print(13^7)
#def collegeLife(n,e,h,a,b,c):
#    x = min(e,h)
#    if e // 2 + h // 3 > n or
#  
#def gcd(a,b):
#    if (b == 0):
#         return a
#    return gcd(b, a%b)
#t = int(input())
#for _ in  range(t):
#    x,y = map(int,input().split())
#    if gcd(x,y) == 1:
#        print("Yes")
#    else:
#        print("No")

#def remove(a):
#    c = 0
#    for i in range(len(a)):
        
#def find(a):
#    m = 0
#    p = [0]*2
#    for i in range(len(a)):
#        c= 0
#        for j in range(len(a)):
#            c += abs(a[i] - a[j])
#        if c > m:
#            m = c
#            p[0] = m
#            p[1] = i
#    del a[p[1]]
#    mean = sum(a) // len(a)
#    c = 0
#    for i in range(len(a)):
#        c += abs(a[i] - mean)
#    return c

#arr = [2,4]
#print(find(arr))
