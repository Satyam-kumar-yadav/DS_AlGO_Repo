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
# # def checkPalindrom(num):
# #     temp = num
# #     rev = 0
# #     while(num>0):
# #         dig=num%10
# #         rev=rev*10+dig
# #         num=num//10
# #     if temp == rev:
# #         return True
# #     return False

# # # a = [111 , 222, 333, 444, 555]
# # # print(PalinArray(a , len(a)))

# # # Problem - Line Number 40
# # # public int find_fact(int[] v)
# # # {
# # #     // Code here
# # #     int n = v.length ;
# # #     Arrays.sort(v) ;
# # #     if( n % 2 != 0){
# # #         return v[n / 2] ;
# # #     }else{
# # #         return (v[n / 2 - 1] + v[n / 2]) / 2 ;
# # #     }
# # # }

# # # Problem - Line Number 44
# # def spiralmat(row , col , a):
# #     k  = 0
# #     l = 0
# #     while(k < row and l < col ):
# #         for i in range(l  , col):
# #             print(a[k][i] , end = " ")
# #         k += 1

# #         for i in range( k , row):
# #             print(a[i][col - 1] , end = " ")
# #         col -= 1    
# #         if k < m:
# #             for i in range(col - 1 , l -1 , -1):
# #                 print(a[row - 1][i] , end= " ")
# #             row -= 1
# #             for i in range(row - 1 , k , -1 ):
# #                 print(a[i][l] , end = " ")
# #           l += 1    

# # a = [[1, 2, 3, 4, 5, 6],
# #      [7, 8, 9, 10, 11, 12],
# #      [13, 14, 15, 16, 17, 18]]

# # R = 3
# # C = 6

# # # Function Call
# # spiralmat(R, C, a)
# ##### Problem - Line Number 45
# def binarysearch(arr , r , l , m):
#     if l >= r:
#         mid= r + (l - r)//2
#         if arr[mid] == m:
#             return True
#         elif m < arr[mid] :
#             return binarysearch(arr , r , mid - 1 , m)   
#         else:
#             return binarysearch(arr , mid + 1 , l , m)
#     else:
#         return False            
# def mat(matrix , r , l , m):    
#     for i in range(r):
#         if m > matrix[i][0] and m < matrix[i][l - 1] :
#              return binarysearch(matrix[i] , 0 , l - 1, m)
                    
#         else:
#             return False
# # m = [1 , 3 , 5 , 7 , 6]
# # print(binarysearch(m , 0 , len(m) - 1, 8))    

# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]] 
# target = 3
# print(mat(matrix , 3 , 4 , target))


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
##### Prloblem - Line Number 57
# class Solution:
# 	def isPlaindrome(self, S):
# 	    if S == S[::-1]:
# 	        return 1
# 	    return 0
##### Problem - Line Number 58
# def reverseString(string , count):
#     for i in string:
#         count[ord(i)] += 1
#     return count
# def filln(string):
#     count = [0]*256
#     count = reverseString(string , count)
#     k = 0
#     for i in count:
#         if int(i) > 1:
#             print(chr(k) , int(i))
#         k += 1


# string = "test string"
# filln(string)
# ##### Problem - Line Number 59
# Why String are immutable
##### Problem - Line Number 60
# def stingcheck(s1 , s2):
#     temp = s1 + s1
#     if s2 in temp:
#         return 1
#     else:
#         return 0

# s1 = "ABCD"
# s2 = "CDAB"
# print(stingcheck(s1 , s2))
##### Problem - Line Number 61
# def string_count(a1 , a2 , String):
#     i , j , k = 0 , 0 , 0
#     while k != len(String):
#         if i < len(a1) and a1[i] == String[k]:
#             i += 1
#         elif j < len(a2) and a2[j] == String[k]:
#             j += 1
#         else:
#             return False
#     return True            
##### Problem - Line Number 62
##### Problem - Line Number 66
# def toString(List): 
# 	return ''.join(List) 

# def permute(a, l, r): 
# 	if l==r: 
# 		print(toString(a))
# 	else: 
# 		for i in range(l,r+1): 
# 			a[l], a[i] = a[i], a[l] 
# 			permute(a, l+1, r) 
# 			a[l], a[i] = a[i], a[l]
##### Problem - Line Number 67
# def permute(arr , n):
#     zero= 0
#     one = 0
#     cnt = 0
#     for i in range(len(arr)):
#         if arr[i] == "1":
#             one += 1
#         else:
#             zero += 1
        
#         if one == zero:
#             cnt += 1
#     if one != zero:
#         return -1    

#     return cnt        

# str = "0111100010"
# n = len(str) 
# print(permute(str, n)) 
##### Problem - Line Number 70
# def nextpermutation(arr , n):
#     for i in range(n -1 , 0 , -1):
#         if arr[i -1 ] < arr[i]:
#             break

#     if i == 1 and arr[i] <= arr[i-1]: 



#             temp = arr[i -1]
#             min = i
#             for j in range(i , n):
#                 if arr[j] < arr[min]:
#                     min = j

#             arr[min] , temp = temp , arr[min]

########incomplete
######## Problem - Line Number 71
# def ispar(expr): 
# 	stack = [] 
# 	for char in expr: 
# 		if char in ["(", "{", "["]:  
# 			stack.append(char) 
# 		else: 
# 			if not stack: 
# 				return False
# 			current_char = stack.pop() 
# 			if current_char == '(': 
# 				if char != ")": 
# 					return False
# 			if current_char == '{': 
# 				if char != "}": 
# 					return False
# 			if current_char == '[': 
# 				if char != "]": 
# 					return False

# 	if stack: 
# 		return False
# 	return True
# s = "{([])}"
# if ispar(s):
#     print("true")
# else:
#     print("false")
# ######## Problem - Line Number 72
# def wordBreak(wordList, word): 
# 	if word == '': 
# 		return True
# 	else: 
# 		wordLen = len(word) 

# 	return any([(word[:i] in wordList) and wordBreak(wordList, word[i:]) for i in range(1, wordLen+1)]) 
    

# # B = { "i", "like", "sam", "sung", "samsung", "mobile",
# # "ice","cream", "icecream", "man", "go", "mango" }
# # A = "ilikesamsung"
# # print(wordBreak(B , A))

# ######## Problem - Line Number 73
# # n = len(s)
# # 	for i in range(n //2 , 0 , -1):
# # 		preffix = s[:i]
# # 		suffix = s[n-i : n]
# # 		if preffix == suffix:
# # 			return i
# # 	return 0def lps(s):
# ######## Problem - Line Number 75
# # def mobileNum(arr , s):
# # 	output = ""
# # 	for i in s:
# # 		if i == " ":
# # 			output += "0"
# # 		else:
# # 			pos = ord(i) - ord("A")	
# # 			output += arr[pos]
						
# # 	return output

# # str = ["2", "22", "222", 
# #        "3", "33", "333", 
# #        "4", "44", "444", 
# #        "5", "55", "555", 
# #        "6", "66", "666", 
# #        "7", "77", "777", "7777", 
# #        "8", "88", "888", 
# #        "9", "99", "999", "9999" ] 
  
# # input1 = "GEEKSFORGEEKS"
# # print(mobileNum(str, input1)) 
# # ######## Problem - Line Number 76
# # def balancedString(S):
# # 	arr1 = list()			
# # 	for i in S:
# # 		if (len(arr1) == 0 and  i == "}") or i == "{":
# # 			arr1.append(i)
# # 		else:
# # 			count = arr1.pop()
# # 			if i == "}" and count == "{" :
# # 				continue
# # 			else:
# # 				arr1.append(count)
# # 				arr1.append(i)
# # 	print (arr1)			

# # 	l1 = 0
# # 	l2 = 0 
# # 	count = 0
# # 	for i in arr1:
# # 		if i == "{":
# # 			l1 += 1
# # 		else:
# # 			l2 += 1

# # 	if l1 % 2 == 0 and l2 % 2 == 0:
# # 		count = l1 //2 + l2 //2
# # 	elif l1 % 2 != 0 and l2 % 2 != 0:
# # 		count = l1 //2 + l2 // 2 + 2
# # 	else:
# # 		count = -1		

# # 	return count


# # a = "}}}}"
# # print(balancedString(a))
# ######## Problem - Line Number 77
# ######## Problem - Line Number 78
# # def num(arr , s):
# #     list(s)
# #     for i in range(len(arr)):
# #         for j in range(len(i)):




# ######## Problem - Line Number 101
# # def occurnce(arr , n , m):
# #     arr1 = list()
# #     if m not in arr:
# #         print("-1")
# #     else:
# #         for i in range(n):
# #             if arr[i] == m:
# #                 arr1.append(i)
# #         print(arr1[0] , arr1[-1])        

# # # a = [1, 3, 5, 5, 5, 5, 7, 123, 125 , 5]
# # a = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
# # occurnce(a , len(a) , 8)
# #### Problem - Line Number 102
# # class Solution:

# # 	def valueEqualToIndex(self,arr, n):
# # 		# code here
# # 		arr1 = list()
# # # 	    for i in range(n+1):
# # # 		    if i == arr[i -1]:
# # # 		        arr1.append(arr[i-1])
# # # 	    return arr1      

# # # #### Problem - Line Number 103
# # # class Solution:
# # #     def search(self, nums: List[int], target: int) -> int:
# # #         for i in range(len(nums)):
# # #             if nums[i] == target:
# # #                 return i
            
# # #         return -1   

# # #### Problem - Line Number 104
# # # class Solution:
# # #     def countSquares(self, N):
# # #         # code here 
# # #         return int(math.sqrt(N -1))

# # # # #### Problem - Line Number 107
# def findTwoElement(arr, n): 
#     arr1 = []
#     se = set()
#         # code here
#     for i in range(n):
#         if i+ 1 not in arr:
#             arr1.append(i + 1)
        
#     for i in range(n):
#         if arr[i] not in se:
#             se.add(arr[i])
#         else:
#             arr1.append(arr[i])
                
#     return arr1[::-1] 

# a = [1 , 3 , 3]

# print(findTwoElement(a , 3 ))
##### problem Number - 108
# from collections import Counter
# def max(A , N):
#     n = N // 2
#     dt = Counter(A)
#     for i in dt:
#         if dt[i] > n:
#             return i
#     return -1    

# A = [1 , 2 , 3]    
# N = 3
##### problem Number - 108
# def pairdiff(arr , n , m):
#     x = set()
#     for i in arr:
#         x.add(i)
#     for i in arr:
#         if i + m in x:
#             return 1
#     return -1        
        
# t = int(input())
# for _ in range(t):
#     n,k=map(int,input().strip().split())

#     arr = list(map(int,input().strip().split()))
#     print(pairdiff(arr , n , k))
### problem Number - 109
# def fourSum(arr , k):
#     x = set()
#     arr1 =[]
#     for i in arr:
#         x.add(i)

#     for i in range(len(arr) - 2):
#         for j in range(i + 1 , len(arr) -1 ):
#             for k1 in range( j + 1 , len(arr)):
#                 if  k - (arr[i] + arr[j] + arr[k1]) in x:
#                     arr1.append([arr[i] , arr[j] , arr[k1] , k - (arr[i] + arr[j] + arr[k1]) ])

#     return arr1

# A = [0,0,2,1,1]
# print(fourSum(A , 3))
# print(max(A , 5))

### problem Number 110
def fourSum(arr , k):
    arr1 = []
    arr.sort()
    for i in range(len(arr) - 3):
        for j in range( i + 1 , len(arr) - 2):
            l = j + 1
            r = len(arr) -1
            while l < r:
                if arr[i] + arr[j] + arr[l] + arr[r] == k:
                    arr1.append(1)
                elif arr[i] + arr[j] + arr[l] + arr[r] < k:
                    l += 1    
                elif arr[i] + arr[j] + arr[l] + arr[r] < k:
                    r -= 1 
    return arr1                
A = [0,0,2,1,1]
print(fourSum(A , 3))
# # # ### Fibonnaci sequence
# # # # def fib(n):
# # # #     if n ==1 or n == 2:
# # # #         return 1
# # # #     else:
# # # #         return fib(n -1 ) + fib(n -2)   

# # # # print(fib(50))
# # # ########Linked List
# # # # #### Problem - Line Number 139
# # # class Node:
# # #     def __init__(self , data):
# # #         self.data = data
# # #         self.next = None

# # # class Linkedlist:
# # #     def __init__(self):
# # #         self.head = None

# # #     def push(self , new_data):
# # #         new_data = Node(new_data)    
# # #         new_data.next = self.head
# # #         self.head = new_data

# # #     def reverse(self):
# # #         prev = None
# # #         current =  self.head
# # #         while( current is not None):
# # #             next = current.next
# # #             current.next = prev
# # #             prev = current
# # #             current = next
# # #         self.head = prev

# # #     def printlist(self):
# # #         temp = self.head
# # #         while temp:
# # #             print(temp.data)
# # #             temp = temp.next        


# # # # #### Problem - Line Number 140
# class Node:
#     def __init__(self , data):
#         self.data = data
#         self.next = None
# class Linkedlist:
#     def __init__(self):
#         self.head = None
    
#     def push(self , new_data):
#         new_data = Node(new_data)    
#         new_data.next = self.head
#         self.head = new_data

# #     def reverse(self ,head , k):
# #         current = head
# #         prev = None
# #         count = 0 
# #         if not head or head.next is None:
# #             return
# #         while current is not None and count < k:
# #             next = current.next
# #             current.next = prev
# #             prev = current
# #             current = next
# #         head = prev

# #         self.reverse(head.next , k)


            
    
# # ll = Linkedlist()
# # ll.push(20)
# # ll.push(18)
# # ll.printlist()
# # ll.reverse()
# # ll.printlist()

# ### deleting the linkedlist
# def detect(head):
#     slow = fast = head
#     while slow and fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         if slow == fast:
#             return 1
        
#     return 0    

# def removeloop(head):
#     slow = fast = head 
#     while(1):
#         slow = slow.next   
#         fast = fast.next.next
#         if slow == fast:
#             break
#     slow = head
#     while slow.next != fast.next:
#         slow = slow.next
#         fast = fast.next
#     fast.next = None

# def movehead(head):
#     if not head or head.next is None :
#         return
#     temp = head
#     while(temp.next.next):
#         temp = temp.next 
#     temp.next = head       
#     head = temp.next    
#     temp.next = None

# def removeDuplicates(head):
#     #code here
#     if head == None:
#         return 
#     if head.next != None:
#         if head.data == head.next.data:
#             temp = head.next
#             head.next = head.next.next
#             removeDuplicates(head)
#         else:
#             removeDuplicates(head.next)
    
#     return head

# # # # #### Problem - Line Number 238
# def maximumMeetings(n,start,end):
#     arr = list()
#     arr2 = list()
#     for i in range(len(start)):
#         arr.append([end[i] , start[i] , i])
#     arr.sort()     
#     arr = arr[::-1]
#     arr2.append(arr[0][2] + 1)
#     temp = arr[0][1]
#     for i in arr:
#         if i[0] < temp:
#             arr2.append(i[2] + 1)
#             temp = i[1]


#     return arr2[::-1]


# s = [1,3,0,5,8,5]
# e = [2,4,6,7,9,9]
# print(maximumMeetings(6 , s , e))
######### Problem - Line Number 239
# def problemded(job , n):



# job = [[1 , 4 , 20] , [2 , 1 , 10]]