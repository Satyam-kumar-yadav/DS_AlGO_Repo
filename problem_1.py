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
# Problem - Line number 37
