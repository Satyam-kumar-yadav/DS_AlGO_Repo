# def rever_arr(A , start , end):
#     if start < end :
#         A[start] , A[end] = A[end] , A[start]
#         start += 1
#         end -= 1

#     return A

# def rever_arr(A):
#     print(A[::-1])
# import sys
# def smallest(A):
#     a = b = 10000
#     for i in range(0 , len(A)):
#         if A[i] < a:
#             b = a
#             a = A[i]
#         elif (A[i] < b and A[i] != a):
#             b = A[i]

#     print(a , b)
# import sys
# def minmax(A):
#     a = sys.maxsize
#     b = A[0]
#     for i in range(0 , len(A)):
#         if A[i] < a:
#             a = A[i]
#     for i in range(0 , len(A)):
#         if A[i] > b:
#             b = A[i]
#     print(a ,b)
# A = [22, 3 , 4 , 5 , 101 , 102 ]
# print(A)
# minmax(A)

# problem 5
# def getmin(arr , n , k):
#     if n == 1:
#         return 0

#     arr.sort()
#     ans = arr[n-1] - arr[0]
#     small = arr[0] + k
#     big = arr[n-1] - k
#     if small > big:
#         small , big = big , small
#     for i in range(1 ,len(arr)):
#         s = arr[i] - k
#         r = arr[i] + k
#         if s >= small and r <= big:
#             continue
#         if big - s <= r - small:
#             small = s
#         else:
#             big = r

#     return min(ans , big - small)


# def new_arr(arr):
#     a = []
#     while(len(arr) != 0):
#         if len(a) == 0 or a[-1] > 0:
#             for i in range(len(arr)):
#                 if arr[i] < 0:
#                     a.append(arr[i])
#                     arr.remove(arr[i])
#                     break
#                 else:
#                     a = a + arr
#                     arr.clear()
#         if a[-1] < 0:
#              for i in range(len(arr)):
#                 if arr[i] > 0:
#                     a.append(arr[i])
#                     arr.remove(arr[i])
#                     break
#                 else:
#                     a = a + arr
#                     arr.clear()

#     for i in range(len(a)):
#         print(a[i])


# Quick Sort
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr.pop()

#     int_great = []
#     int_small = []
#     for items in arr:
#         if items >= pivot:
#             int_great.append(items)
#         else:
#             int_small.append(items)

#     return quick_sort(int_small) + [pivot] + quick_sort(int_great)
# Quick Sort 2
# def swap(A , start , end):
#     A[start] , A[end] = A[end] , A[start]

#     return A

# def quick_sort(arr):
#     j = 0
#     for i in range(len(arr)):
#         if arr[i] < 0:
#             swap(arr , j , i)
#             j += 1

#     return arr
# max sub arr
# def quick_sort(arr):
#     result = arr[0]
#     n = len(arr)
#     for i in range(n):
#         mul = arr[i]
#         for j in range(i+1 , n):
#             result = max(result , mul)
#             mul *= arr[j]

#         result = max(result , mul)
#     return result

# Bubble Sort
# def selection_sort(arr):
#     for i in range(len(arr)):
#         min = i
#         for j in range(i + 1 , len(arr)):
#             if arr[j] < arr[i]:
#                 min = j
#         arr[i] , arr[min]   = arr[min] , arr[i]

#     return arr

# Bubble Sort
# def bubble_sort(arr):
#     for i in range(len(arr) - 1):
#         for j in range(len(arr) - 1):
#             if arr[j] > arr[j + 1 ]:
#                 arr[j] , arr[j+1] = arr[j+1] , arr[j]


#     return arr

# Insertion Sort
# def Insertion_sort(arr):
# for i in range(1 , len(arr)):
#     m = arr[i]
#     j = i -1
#     while(j >= 0 and m < arr[j]):
#         arr[j+1] = arr[j]
#         j = j -1
#     arr[j+1] = m
# return arr

# maxcontinous
# def findLongestConseqSubseq(arr, N):
#     #code here
#     arr.sort()
#     max_1 = 0
#     count = 1
#     for i in range(len(arr) - 2):
#         if arr[i+1] - arr[i] == 1:
#             count += 1
#         elif arr[i+1] - arr[i] != 1:
#             count = 1
#         if max_1 < count:
#             max_1 = count
#     return max_1

# arr[] : the input array
# N : size of the array arr[]
# return the length of the longest subsequene of consecutive integers
# def findLongestConseqSubseq(arr, N):
#     #code here
#     set_1 = set()
#     max_count = 1
#     count = 1
#     for i in range(len(arr)):
#         set_1.add(arr[i])

#     for i in set_1:
#         if i - 1 in set_1:
#            count += 1
#         else:
#             count = 1
#         max_count = max(count , max_count)


#     return max_count
# def findLongestConseqSubseq(arr, N):
#     #code here
#     set_1 = set()
#     count = 0
#     for i in range(len(arr)):
#         set_1.add(arr[i])

#     for i in set_1:
#         if (i - 1) not in set_1:
#             j = i
#             while (j in set_1):
#                 j += 1

#         count = max(count , j - arr[i])


#     return count
# problem number -30
# def Conseq(arr , k):
#     n = len(arr) // k
#     dic = {}
#     arr_1 = []
#     for i in range(len(arr)):
#         if (not bool(dic)) or (arr[i] not in dic) :
#             dic[arr[i]] = 1
#         else:
#             dic[arr[i]] += 1
#     for key , value in dic.items():
#         if value > n:
#             arr_1.append(key)

#     return arr_1
# get list
# def sub_lists (l):
#     base = []
#     lists = [base]
#     for i in range(len(l)):
#         orig = lists[:]
#         new = l[i]
#         for j in range(len(lists)):
#             lists[j] = lists[j] + [new]
#         lists = orig + lists

#     return lists
# Problem - Line number 34
# def chocolates(arr , n , m):
#     arr.sort()
#     min_1 = arr[n-1] - arr[0]
#     print(arr)
#     for i in range(len(arr) - m + 1):
#         min_1 = min(min_1 ,  arr[i + m - 1] - arr[i])
#         print(min_1)

#     return min_1


# a = [34 ,  88 ,  89 ,39, 67, 71 ,85, 57, 18, 7, 61, 50, 38, 6 ,60, 18, 19, 46, 84, 74, 59]
# print(chocolates(a , 21 , 12 ))


# Problem - Line Number 35
# Problem - Line Number 36

# Problem - Line number
# NA


# Problem - Line Number 38
# def minSwap(arr , n , k):
#     a = [0]*n
#     count = 0
#     for i in range(n):
#         if arr[i] <= k:
#             a[i] = 1
#             count += 1
#     if count == 1:
#         return 0
#     max_res = count
#     for i in range(n - count + 1):
#         res = 0
#         for j in range(i , i + count):
#             if a[j] == 0:
#                 res += 1
#         if max_res > res:
#             max_res = res
#         print(res)
#     return max_res

# #a = [470 , 10 , 28 , 338 , 384 , 0 , 329 , 405 , 70 , 349 , 40  , 472 , 212 , 14,  411 , 151  ,215 , 384 ,368 ,46 ,256 ,  42]
# #a  = [263, 349, 318, 277, 282, 301, 250, 104, 164, 278, 442, 400, 130, 271, 305, 52, 472, 346, 24, 185]
# #a = [2, 1, 5, 6, 3]
# #a = [497, 444, 294, 120]
# a = [310, 229, 86, 249]
# print(minSwap(a , len(a) , 256))

# Problem -  Line Number 39
# def PalinArray(arr ,n):
#     # Code here
#     for i in range(n):
#         if checkPalindrom(arr[i]):
#             continue
#         else:
#             return 0
#     return 1
# def checkPalindrom(num):
#     temp = num
#     rev = 0
#     while(num>0):
#         dig=num%10
#         rev=rev*10+dig
#         num=num//10
#     if temp == rev:
#         return True
#     return False

# a = [111 , 222, 333, 444, 555]
# print(PalinArray(a , len(a)))

# Problem - Line Number 40
# public int find_fact(int[] v)
# {
#     // Code here
#     int n = v.length ;
#     Arrays.sort(v) ;
#     if( n % 2 != 0){
#         return v[n / 2] ;
#     }else{
#         return (v[n / 2 - 1] + v[n / 2]) / 2 ;
#     }
# }

# Problem - Line Number 44
##### Problem - Line Number 56
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
        
#         """
#         n = len(s) // 2
#         for i in range(n):
#             temp = s[len(s) - i - 1]
#             s[len(s) - i - 1] = s[i]
#             s[i] = temp
##### Problem - Line Number 57
# class Solution:
# 	def isPlaindrome(self, S):
# 	    if S == S[::-1]:
# 	        return 1
# 	    return 0
##### Problem - Line Number 58
def reverseString(string , count):
    for i in string:
        count[ord(i)] += 1
    return count
def filln(string):
    count = [0]*256
    count = reverseString(string , count)
    k = 0
    for i in count:
        if int(i) > 1:
            print(chr(k) , int(i))
        k += 1


string = "test string"
filln(string)


######## Problem - Line Number 101
# def occurnce(arr , n , m):
#     arr1 = list()
#     if m not in arr:
#         print("-1")
#     else:
#         for i in range(n):
#             if arr[i] == m:
#                 arr1.append(i)
#         print(arr1[0] , arr1[-1])        

# # a = [1, 3, 5, 5, 5, 5, 7, 123, 125 , 5]
# a = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
# occurnce(a , len(a) , 8)
#### Problem - Line Number 102
# class Solution:

# 	def valueEqualToIndex(self,arr, n):
# 		# code here
# 		arr1 = list()
# 	    for i in range(n+1):
# 		    if i == arr[i -1]:
# 		        arr1.append(arr[i-1])
# 	    return arr1      

# #### Problem - Line Number 103
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 return i
            
#         return -1   

#### Problem - Line Number 104
# class Solution:
#     def countSquares(self, N):
#         # code here 
#         return int(math.sqrt(N -1))

# #### Problem - Line Number 104   
     
