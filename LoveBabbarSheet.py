# # def rever_arr(A , start , end):
# #     if start < end :
# #         A[start] , A[end] = A[end] , A[start]
# #         start += 1
# #         end -= 1

# #     return A

# # def rever_arr(A):
# #     print(A[::-1])
# # import sys
# # def smallest(A):
# #     a = b = 10000
# #     for i in range(0 , len(A)):
# #         if A[i] < a:
# #             b = a
# #             a = A[i]
# #         elif (A[i] < b and A[i] != a):
# #             b = A[i]

# #     print(a , b)
# # import sys
# # def minmax(A):
# #     a = sys.maxsize
# #     b = A[0]
# #     for i in range(0 , len(A)):
# #         if A[i] < a:
# #             a = A[i]
# #     for i in range(0 , len(A)):
# #         if A[i] > b:
# #             b = A[i]
# #     print(a ,b)
# # A = [22, 3 , 4 , 5 , 101 , 102 ]
# # print(A)
# # minmax(A)

# # problem 5
# # def getmin(arr , n , k):
# #     if n == 1:
# #         return 0

# #     arr.sort()
# #     ans = arr[n-1] - arr[0]
# #     small = arr[0] + k
# #     big = arr[n-1] - k
# #     if small > big:
# #         small , big = big , small
# #     for i in range(1 ,len(arr)):
# #         s = arr[i] - k
# #         r = arr[i] + k
# #         if s >= small and r <= big:
# #             continue
# #         if big - s <= r - small:
# #             small = s
# #         else:
# #             big = r

# #     return min(ans , big - small)


# # def new_arr(arr):
# #     a = []
# #     while(len(arr) != 0):
# #         if len(a) == 0 or a[-1] > 0:
# #             for i in range(len(arr)):
# #                 if arr[i] < 0:
# #                     a.append(arr[i])
# #                     arr.remove(arr[i])
# #                     break
# #                 else:
# #                     a = a + arr
# #                     arr.clear()
# #         if a[-1] < 0:
# #              for i in range(len(arr)):
# #                 if arr[i] > 0:
# #                     a.append(arr[i])
# #                     arr.remove(arr[i])
# #                     break
# #                 else:
# #                     a = a + arr
# #                     arr.clear()

# #     for i in range(len(a)):
# #         print(a[i])


# # Quick Sort
# # def quick_sort(arr):
# #     if len(arr) <= 1:
# #         return arr
# #     else:
# #         pivot = arr.pop()

# #     int_great = []
# #     int_small = []
# #     for items in arr:
# #         if items >= pivot:
# #             int_great.append(items)
# #         else:
# #             int_small.append(items)

# #     return quick_sort(int_small) + [pivot] + quick_sort(int_great)
# # Quick Sort 2
# # def swap(A , start , end):
# #     A[start] , A[end] = A[end] , A[start]

# #     return A

# # def quick_sort(arr):
# #     j = 0
# #     for i in range(len(arr)):
# #         if arr[i] < 0:
# #             swap(arr , j , i)
# #             j += 1

# #     return arr
# # max sub arr
# # def quick_sort(arr):
# #     result = arr[0]
# #     n = len(arr)
# #     for i in range(n):
# #         mul = arr[i]
# #         for j in range(i+1 , n):
# #             result = max(result , mul)
# #             mul *= arr[j]

# #         result = max(result , mul)
# #     return result

# # Bubble Sort
# # def selection_sort(arr):
# #     for i in range(len(arr)):
# #         min = i
# #         for j in range(i + 1 , len(arr)):
# #             if arr[j] < arr[i]:
# #                 min = j
# #         arr[i] , arr[min]   = arr[min] , arr[i]

# #     return arr

# # Bubble Sort
# # def bubble_sort(arr):
# #     for i in range(len(arr) - 1):
# #         for j in range(len(arr) - 1):
# #             if arr[j] > arr[j + 1 ]:
# #                 arr[j] , arr[j+1] = arr[j+1] , arr[j]


# #     return arr

# # Insertion Sort
# # def Insertion_sort(arr):
# # for i in range(1 , len(arr)):
# #     m = arr[i]
# #     j = i -1
# #     while(j >= 0 and m < arr[j]):
# #         arr[j+1] = arr[j]
# #         j = j -1
# #     arr[j+1] = m
# # return arr

# # maxcontinous
# # def findLongestConseqSubseq(arr, N):
# #     #code here
# #     arr.sort()
# #     max_1 = 0
# #     count = 1
# #     for i in range(len(arr) - 2):
# #         if arr[i+1] - arr[i] == 1:
# #             count += 1
# #         elif arr[i+1] - arr[i] != 1:
# #             count = 1
# #         if max_1 < count:
# #             max_1 = count
# #     return max_1

# # arr[] : the input array
# # N : size of the array arr[]
# # return the length of the longest subsequene of consecutive integers
# # def findLongestConseqSubseq(arr, N):
# #     #code here
# #     set_1 = set()
# #     max_count = 1
# #     count = 1
# #     for i in range(len(arr)):
# #         set_1.add(arr[i])

# #     for i in set_1:
# #         if i - 1 in set_1:
# #            count += 1
# #         else:
# #             count = 1
# #         max_count = max(count , max_count)


# #     return max_count
# # def findLongestConseqSubseq(arr, N):
# #     #code here
# #     set_1 = set()
# #     count = 0
# #     for i in range(len(arr)):
# #         set_1.add(arr[i])

# #     for i in set_1:
# #         if (i - 1) not in set_1:
# #             j = i
# #             while (j in set_1):
# #                 j += 1

# #         count = max(count , j - arr[i])


# #     return count
# # problem number -30
# # def Conseq(arr , k):
# #     n = len(arr) // k
# #     dic = {}
# #     arr_1 = []
# #     for i in range(len(arr)):
# #         if (not bool(dic)) or (arr[i] not in dic) :
# #             dic[arr[i]] = 1
# #         else:
# #             dic[arr[i]] += 1
# #     for key , value in dic.items():
# #         if value > n:
# #             arr_1.append(key)

# #     return arr_1
# # get list
# # def sub_lists (l):
# #     base = []
# #     lists = [base]
# #     for i in range(len(l)):
# #         orig = lists[:]
# #         new = l[i]
# #         for j in range(len(lists)):
# #             lists[j] = lists[j] + [new]
# #         lists = orig + lists

# #     return lists
# # Problem - Line number 34
# # def chocolates(arr , n , m):
# #     arr.sort()
# #     min_1 = arr[n-1] - arr[0]
# #     print(arr)
# #     for i in range(len(arr) - m + 1):
# #         min_1 = min(min_1 ,  arr[i + m - 1] - arr[i])
# #         print(min_1)

# #     return min_1


# # a = [34 ,  88 ,  89 ,39, 67, 71 ,85, 57, 18, 7, 61, 50, 38, 6 ,60, 18, 19, 46, 84, 74, 59]
# # print(chocolates(a , 21 , 12 ))


# # Problem - Line Number 35
# # Problem - Line Number 36

# # Problem - Line number
# # NA


# # Problem - Line Number 38
# # def minSwap(arr , n , k):
# #     a = [0]*n
# #     count = 0
# #     for i in range(n):
# #         if arr[i] <= k:
# #             a[i] = 1
# #             count += 1
# #     if count == 1:
# #         return 0
# #     max_res = count
# #     for i in range(n - count + 1):
# #         res = 0
# #         for j in range(i , i + count):
# #             if a[j] == 0:
# #                 res += 1
# #         if max_res > res:
# #             max_res = res
# #         print(res)
# #     return max_res

# # #a = [470 , 10 , 28 , 338 , 384 , 0 , 329 , 405 , 70 , 349 , 40  , 472 , 212 , 14,  411 , 151  ,215 , 384 ,368 ,46 ,256 ,  42]
# # #a  = [263, 349, 318, 277, 282, 301, 250, 104, 164, 278, 442, 400, 130, 271, 305, 52, 472, 346, 24, 185]
# # #a = [2, 1, 5, 6, 3]
# # #a = [497, 444, 294, 120]
# # a = [310, 229, 86, 249]
# # print(minSwap(a , len(a) , 256))

# # Problem -  Line Number 39
# # def PalinArray(arr ,n):
# #     # Code here
# #     for i in range(n):
# #         if checkPalindrom(arr[i]):
# #             continue
# #         else:
# #             return 0
# #     return 1
# # # def checkPalindrom(num):
# # #     temp = num
# # #     rev = 0
# # #     while(num>0):
# # #         dig=num%10
# # #         rev=rev*10+dig
# # #         num=num//10
# # #     if temp == rev:
# # #         return True
# # #     return False

# # # # a = [111 , 222, 333, 444, 555]
# # # # print(PalinArray(a , len(a)))

# # # # Problem - Line Number 40
# # # # public int find_fact(int[] v)
# # # # {
# # # #     // Code here
# # # #     int n = v.length ;
# # # #     Arrays.sort(v) ;
# # # #     if( n % 2 != 0){
# # # #         return v[n / 2] ;
# # # #     }else{
# # # #         return (v[n / 2 - 1] + v[n / 2]) / 2 ;
# # # #     }
# # # # }

# # # # Problem - Line Number 44
# # # def spiralmat(row , col , a):
# # #     k  = 0
# # #     l = 0
# # #     while(k < row and l < col ):
# # #         for i in range(l  , col):
# # #             print(a[k][i] , end = " ")
# # #         k += 1

# # #         for i in range( k , row):
# # #             print(a[i][col - 1] , end = " ")
# # #         col -= 1
# # #         if k < m:
# # #             for i in range(col - 1 , l -1 , -1):
# # #                 print(a[row - 1][i] , end= " ")
# # #             row -= 1
# # #             for i in range(row - 1 , k , -1 ):
# # #                 print(a[i][l] , end = " ")
# # #           l += 1

# # # a = [[1, 2, 3, 4, 5, 6],
# # #      [7, 8, 9, 10, 11, 12],
# # #      [13, 14, 15, 16, 17, 18]]

# # # R = 3
# # # C = 6

# # # # Function Call
# # # spiralmat(R, C, a)
# # ##### Problem - Line Number 45
# # def binarysearch(arr , r , l , m):
# #     if l >= r:
# #         mid= r + (l - r)//2
# #         if arr[mid] == m:
# #             return True
# #         elif m < arr[mid] :
# #             return binarysearch(arr , r , mid - 1 , m)
# #         else:
# #             return binarysearch(arr , mid + 1 , l , m)
# #     else:
# #         return False
# # def mat(matrix , r , l , m):
# #     for i in range(r):
# #         if m > matrix[i][0] and m < matrix[i][l - 1] :
# #              return binarysearch(matrix[i] , 0 , l - 1, m)

# #         else:
# #             return False
# # # m = [1 , 3 , 5 , 7 , 6]
# # # print(binarysearch(m , 0 , len(m) - 1, 8))

# # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
# # target = 3
# # print(mat(matrix , 3 , 4 , target))


# # Problem - Line Number 56
# # class Solution:
# #     def reverseString(self, s: List[str]) -> None:
# #         """
# #         Do not return anything, modify s in-place instead.

# #         """
# #         n = len(s) // 2
# #         for i in range(n):
# #             temp = s[len(s) - i - 1]
# #             s[len(s) - i - 1] = s[i]
# #             s[i] = temp
# # Prloblem - Line Number 57
# # class Solution:
# # 	def isPlaindrome(self, S):
# # 	    if S == S[::-1]:
# # 	        return 1
# # 	    return 0
# # Problem - Line Number 58
# # def reverseString(string , count):
# #     for i in string:
# #         count[ord(i)] += 1
# #     return count
# # def filln(string):
# #     count = [0]*256
# #     count = reverseString(string , count)
# #     k = 0
# #     for i in count:
# #         if int(i) > 1:
# #             print(chr(k) , int(i))
# #         k += 1


# # string = "test string"
# # filln(string)
# # ##### Problem - Line Number 59
# # Why String are immutable
# # Problem - Line Number 60
# # def stingcheck(s1 , s2):
# #     temp = s1 + s1
# #     if s2 in temp:
# #         return 1
# #     else:
# #         return 0

# # s1 = "ABCD"
# # s2 = "CDAB"
# # print(stingcheck(s1 , s2))
# # Problem - Line Number 61
# # def string_count(a1 , a2 , String):
# #     i , j , k = 0 , 0 , 0
# #     while k != len(String):
# #         if i < len(a1) and a1[i] == String[k]:
# #             i += 1
# #         elif j < len(a2) and a2[j] == String[k]:
# #             j += 1
# #         else:
# #             return False
# #     return True
# # Problem - Line Number 62
# # Problem - Line Number 66
# # def toString(List):
# # 	return ''.join(List)

# # def permute(a, l, r):
# # 	if l==r:
# # 		print(toString(a))
# # 	else:
# # 		for i in range(l,r+1):
# # 			a[l], a[i] = a[i], a[l]
# # 			permute(a, l+1, r)
# # 			a[l], a[i] = a[i], a[l]
# # Problem - Line Number 67
# # def permute(arr , n):
# #     zero= 0
# #     one = 0
# #     cnt = 0
# #     for i in range(len(arr)):
# #         if arr[i] == "1":
# #             one += 1
# #         else:
# #             zero += 1

# #         if one == zero:
# #             cnt += 1
# #     if one != zero:
# #         return -1

# #     return cnt

# # str = "0111100010"
# # n = len(str)
# # print(permute(str, n))
# # Problem - Line Number 70
# # def nextpermutation(arr , n):
# #     for i in range(n -1 , 0 , -1):
# #         if arr[i -1 ] < arr[i]:
# #             break

# #     if i == 1 and arr[i] <= arr[i-1]:


# #             temp = arr[i -1]
# #             min = i
# #             for j in range(i , n):
# #                 if arr[j] < arr[min]:
# #                     min = j

# #             arr[min] , temp = temp , arr[min]

# # incomplete
# # Problem - Line Number 71
# # def ispar(expr):
# # 	stack = []
# # 	for char in expr:
# # 		if char in ["(", "{", "["]:
# # 			stack.append(char)
# # 		else:
# # 			if not stack:
# # 				return False
# # 			current_char = stack.pop()
# # 			if current_char == '(':
# # 				if char != ")":
# # 					return False
# # 			if current_char == '{':
# # 				if char != "}":
# # 					return False
# # 			if current_char == '[':
# # 				if char != "]":
# # 					return False

# # 	if stack:
# # 		return False
# # 	return True
# # s = "{([])}"
# # if ispar(s):
# #     print("true")
# # else:
# #     print("false")
# # ######## Problem - Line Number 72
# # def wordBreak(wordList, word):
# # 	if word == '':
# # 		return True
# # 	else:
# # 		wordLen = len(word)

# # 	return any([(word[:i] in wordList) and wordBreak(wordList, word[i:]) for i in range(1, wordLen+1)])


# # # B = { "i", "like", "sam", "sung", "samsung", "mobile",
# # # "ice","cream", "icecream", "man", "go", "mango" }
# # # A = "ilikesamsung"
# # # print(wordBreak(B , A))

# # ######## Problem - Line Number 73
# # # n = len(s)
# # # 	for i in range(n //2 , 0 , -1):
# # # 		preffix = s[:i]
# # # 		suffix = s[n-i : n]
# # # 		if preffix == suffix:
# # # 			return i
# # # 	return 0def lps(s):
# # ######## Problem - Line Number 75
# # # def mobileNum(arr , s):
# # # 	output = ""
# # # 	for i in s:
# # # 		if i == " ":
# # # 			output += "0"
# # # 		else:
# # # 			pos = ord(i) - ord("A")
# # # 			output += arr[pos]

# # # 	return output

# # # str = ["2", "22", "222",
# # #        "3", "33", "333",
# # #        "4", "44", "444",
# # #        "5", "55", "555",
# # #        "6", "66", "666",
# # #        "7", "77", "777", "7777",
# # #        "8", "88", "888",
# # #        "9", "99", "999", "9999" ]

# # # input1 = "GEEKSFORGEEKS"
# # # print(mobileNum(str, input1))
# # # ######## Problem - Line Number 76
# # # def balancedString(S):
# # # 	arr1 = list()
# # # 	for i in S:
# # # 		if (len(arr1) == 0 and  i == "}") or i == "{":
# # # 			arr1.append(i)
# # # 		else:
# # # 			count = arr1.pop()
# # # 			if i == "}" and count == "{" :
# # # 				continue
# # # 			else:
# # # 				arr1.append(count)
# # # 				arr1.append(i)
# # # 	print (arr1)

# # # 	l1 = 0
# # # 	l2 = 0
# # # 	count = 0
# # # 	for i in arr1:
# # # 		if i == "{":
# # # 			l1 += 1
# # # 		else:
# # # 			l2 += 1

# # # 	if l1 % 2 == 0 and l2 % 2 == 0:
# # # 		count = l1 //2 + l2 //2
# # # 	elif l1 % 2 != 0 and l2 % 2 != 0:
# # # 		count = l1 //2 + l2 // 2 + 2
# # # 	else:
# # # 		count = -1

# # # 	return count


# # # a = "}}}}"
# # # print(balancedString(a))
# # ######## Problem - Line Number 77
# # ######## Problem - Line Number 78
# # # def num(arr , s):
# # #     list(s)
# # #     for i in range(len(arr)):
# # #         for j in range(len(i)):


# # Problem Number 81
# # def romanDup(str):
# #     roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900 , 'M':1000 }
# #     i = 0
# #     num = 0
# #     while i < len(str):
# #         if i + 1 < len(str) and str[i : i+2] in roman:
# #             num += roman[str[i:i+2]]
# #             i += 2
# #         else:
# #             num += roman[str[i]]
# #             i += 1

# #     return num

# # s = 'V'
# # print(romanDup(s))
# # Problem Number 82
# # def compare(str1 , str2):
# #     n1 = len(str1)
# #     n2 = len(str2)
# #     result = ""
# #     i , j = 0 , 0
# #     while i < n1 and j < n2:
# #         if str1[i] != str2[j]:
# #             break

# #         result += str1[i]
# #         i += 1
# #         j += 1

# #     return result


# # def longestCommon(strs):
# #     prefix = strs[0]
# #     for i in range(1 , len(strs)):
# #         prefix = compare(prefix , strs[i])

# #     return prefix


# # s = ["car" , "cog"]
# # print(longestCommon(s))
# # Problem Number 83
# # def flip(char):
# #     return "1"  if (char == "0") else "0"

# # def minFlip(str , expected):
# #     count = 0
# #     for i in range(len(str)):
# #         if str[i] != expected:
# #             count += 1
# # #         expected = flip(expected)
# # #     return count

# # # def returnFlip(str):
# # # #     return min(minFlip(str , "0") , minFlip(str , "1"))
# # # s = "001"
# # # print(returnFlip(s))
# # ### problem Number 84
# # # #####Problem Number 85
# # # def checkSwap(string):
# # #     arr1 = []
# # #     arr = list(string)
# # #     for i in range(len(arr)):
# # #         if arr[i] == "[":
# # #             arr1.append(arr[i])
# # #         elif arr[i] == "]":
# # #             if not arr1:
# # #                 return False
# # #             else:
# # #                 temp = arr1.pop()
# # #             if temp == "[":
# # #                 continue
# # #             else:
# # #                 return False
# # #     if not arr1: return True
# # # #     return False

# # # # def minSwap(arr , i):
# # # #     temp = arr[i]
# # # #     arr[i] = arr[i + 1]
# # # #     arr[i+1] = temp
# # # #     return arr

# # # # def bracket(string):
# # # def swapArr(string):
# # #     pos = []
# # #     for i in range(len(string)):
# # #         if string[i] == "[":
# # #             pos.append(i)

# # #     count , sum , idx = 0 , 0 , 0
# # #     arr = list(string)
# # #     for i in range(len(arr)):
# # #         if arr[i] == "[":
# # #             count += 1
# # #             idx += 1
# # #         elif arr[i] == "]":
# # #             count -= 1
# # #         if count < 0:
# # #             sum += pos[idx] - i
# # #             arr[i] , arr[pos[idx]]  = arr[pos[idx]] , arr[i]

# # #             idx += 1
# # #             count = 1
# # #     return sum


# # # arr = "[]][]["
# # # print(swapArr(arr))
# # ### Problem Number 86
# # # def Lcs(m , n , X , Y):
# # ### problem number 88
# # def checkString(x , arr):
# #     for i in range(len(arr)):
# #         if arr[i] not in x:
# #             return False
# #         return True
# # def smallestDistinct(string):
# #     x  = set(string)
# #     j = len(x)
# #     i = 0
# #     m = ""
# #     while(i + j <= len(string)):
# #         arr = list(string[i:j])
# #         if checkString(x , arr):
# #             m  = string[i:j]
# #         else:
# #             i += 1
# #             j += 1

# #     return m


# # s = "aabcbcdbca"
# # print(smallestDistinct(s))
# # Problem 88


# # ######## Problem - Line Number 101
# # # def occurnce(arr , n , m):
# # #     arr1 = list()
# # #     if m not in arr:
# # #         print("-1")
# # #     else:
# # #         for i in range(n):
# # #             if arr[i] == m:
# # #                 arr1.append(i)
# # #         print(arr1[0] , arr1[-1])

# # # # a = [1, 3, 5, 5, 5, 5, 7, 123, 125 , 5]
# # # a = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
# # # occurnce(a , len(a) , 8)
# # #### Problem - Line Number 102
# # # class Solution:

# # # 	def valueEqualToIndex(self,arr, n):
# # # 		# code here
# # # 		arr1 = list()
# # # # 	    for i in range(n+1):
# # # # 		    if i == arr[i -1]:
# # # # 		        arr1.append(arr[i-1])
# # # # 	    return arr1

# # # # #### Problem - Line Number 103
# # # # class Solution:
# # # #     def search(self, nums: List[int], target: int) -> int:
# # # #         for i in range(len(nums)):
# # # #             if nums[i] == target:
# # # #                 return i

# # # #         return -1

# # # #### Problem - Line Number 104
# # # # class Solution:
# # # #     def countSquares(self, N):
# # # #         # code here
# # # #         return int(math.sqrt(N -1))

# # # # # #### Problem - Line Number 107
# # def findTwoElement(arr, n):
# #     arr1 = []
# #     se = set()
# #         # code here
# #     for i in range(n):
# #         if i+ 1 not in arr:
# #             arr1.append(i + 1)

# #     for i in range(n):
# #         if arr[i] not in se:
# #             se.add(arr[i])
# #         else:
# #             arr1.append(arr[i])

# #     return arr1[::-1]

# # a = [1 , 3 , 3]

# # print(findTwoElement(a , 3 ))
# # problem Number - 108
# # from collections import Counter
# # def max(A , N):
# #     n = N // 2
# # #     dt = Counter(A)
# # #     for i in dt:
# # #         if dt[i] > n:
# # #             return i
# # #     return -1

# # # A = [1 , 2 , 3]
# # # N = 3
# # ##### problem Number - 108
# # # def pairdiff(arr , n , m):
# # #     x = set()
# # #     for i in arr:
# # #         x.add(i)
# # #     for i in arr:
# # #         if i + m in x:
# # #             return 1
# # #     return -1

# # # t = int(input())
# # # for _ in range(t):
# # #     n,k=map(int,input().strip().split())

# # #     arr = list(map(int,input().strip().split()))
# # #     print(pairdiff(arr , n , k))
# # ### problem Number - 109
# # # def fourSum(arr , k):
# # #     x = set()
# # #     arr1 =[]
# # #     for i in arr:
# # #         x.add(i)

# # #     for i in range(len(arr) - 2):
# # #         for j in range(i + 1 , len(arr) -1 ):
# # #             for k1 in range( j + 1 , len(arr)):
# # #                 if  k - (arr[i] + arr[j] + arr[k1]) in x:
# # #                     arr1.append([arr[i] , arr[j] , arr[k1] , k - (arr[i] + arr[j] + arr[k1]) ])

# # #     return arr1

# # # A = [0,0,2,1,1]
# # # print(fourSum(A , 3))
# # # print(max(A , 5))

# # ### problem Number 110
# # def fourSum(arr , k):
# #     arr1 = []
# #     arr.sort()
# #     for i in range(len(arr) - 3):
# #         for j in range( i + 1 , len(arr) - 2):
# #             l = j + 1
# #             r = len(arr) -1
# #             while l < r:
# #                 if arr[i] + arr[j] + arr[l] + arr[r] == k:
# #                     arr1.append([arr[i] , arr[j] , arr[l] , arr[r]])
# #                     l += 1
# #                     r -= 1
# #                 elif arr[i] + arr[j] + arr[l] + arr[r] < k:
# #                     l += 1
# #                 else:
# #                     r -= 1

# #     return arr1
# # A = [10,2,3,4,5,7,8]
# # print(fourSum(A ,23))
# # Problem Number - 111
# # # def find_max_sum(arr):
# # 	# incl = 0
# # 	# excl = 0

# # 	# for i in arr:

# # # 	# 	# Current max excluding i (No ternary in
# # # 	# 	# Python)
# # # 	# 	new_excl = excl if excl>incl else incl

# # # 	# 	# Current max including i
# # # 	# 	incl = excl + i
# # # 	# 	excl = new_excl

# # # 	# # return max of incl and excl
# # # 	# return (excl if excl>incl else incl)

# # # # Driver program to test above function
# # # # arr = [5, 5, 10, 100, 10, 5]
# # # # print(find_max_sum(arr) )
# # # ########## Problem Number 113
# # # def countTriplets(arr, n, sum):
# # #     # Your code goes here
# # #     triplet = 0
# # #     for i in range(n-2):
# # #         l = i + 1
# # #         r = n - 1
# # #         while l < r:
# # #             if arr[i] + arr[l] + arr[r] >= sum:
# # #                 r -= 1
# # #             else:
# # #                 triplet += r - l
# # #                 l += 1
# # #     return triplet

# # # arr = [5, 1, 3, 4, 7]
# # # print(countTriplets(arr , 5 , 12))
# # ######### Problem Number 114
# # with(space)
# # def merge(arr1, arr2, n, m):
# #     # code here
# #     arr= []
# #     i = 0
# #     j = 0
# #     while i < n and j < m:
# #         if arr1[i] < arr2[j]:
# #             arr.append(arr1[i])
# #             i += 1
# #         else:
# #             arr.append(arr2[j])
# # #             j += 1

# # #     while i < n:
# # #         arr.append(arr1[i])
# # #         i += 1
# # #     while j < m:
# # #         arr.append(arr2[j])
# # #         j += 1

# # #     return arr

# # # arr1 = [10, 12]
# # # arr2 = [5, 18, 20]
# # # print(merge(arr1 , arr2 , 2 , 3))
# # ####without Space
# # def merge(arr1 , arr2 , n , m):
# #     for i in range(m - 1 , - 1 , -1):
# #         last = arr1[n - 1]
# #         j = n - 2
# #         while(j >= 0 and arr2[i] < arr1[j]):
# #             arr1[j + 1] = arr1[j]
# #             j -= 1
# #         if  j != n -2 or last > arr2[i]:
# #             arr1[j + 1] = arr2[i]
# #             arr2[i] = last

# # # arr1 = [1, 3, 5, 7]
# # # arr2 = [0, 2, 6, 8, 9]
# # # merge(arr1 , arr2 , 4 , 5)
# # # print(arr1 + arr2)
# # ######problem number 115
# # def subarray(arr , n):
# #     count = 0
# #     sum = 0
# #     old_sum = 0
# #     x = set()
# #     for i in range(n):
# #         x.add(sum)
# #         old_sum = sum
# #         sum += arr[i]
# #         if sum in x:
# #             count += 1
# #         if old_sum == sum:
# #             count += 1
# #     print(x)
# #     return count
# # a = [6,-1,-3,4,-2,2,4,6,-12,-7]
# # print(subarray(a , 10))
# # Problem number 116
# # def prod(arr , n):
# # left = [0] * n
# # right = [0] * n
# # prod1 = [0] * n
# # left[0] = 1
# # right[n - 1] = 1
# # for i in range(1 , n):
# #     left[i] = arr[i - 1] * left[i -1]
# # for i in range(n - 2 , -1 , -1):
# #     right[i]  = arr[i + 1] * right[i + 1]

# # for i in range(n):
# #     prod1[i] = left[i] * right[i]

# # return prod1

# # Problem number 117
# # def minSwap(arr , n):


# # # a = [10, 3, 5, 6, 2]
# # # print(minSwap(a , 5))
# # # Problem from codechef
# # # def killMonster(a , b , c):
# # #     sum = a + b + c
# # #     temp = sum // 9
# # #     m = min(a , min(b , c))
# # #     if sum % 9 != 0 or m < temp:
# # #         print("No")
# # #     else:
# # #         print("Yes")

# # # killMonster(10 , 1 , 7)
# # # ### problem Number 119
# # # def bishuSoldiers(arr , n):
# # #     sum = 0
# # #     for i in range(len(arr)):
# # #         if arr[i] <= n:
# # #             sum += arr[i]
# # #     return sum
# # # a = [1, 2, 3, 4, 5, 6, 7]
# # # print(bishuSoldiers( a , 10 ))
# # ### Problem Number 120
# # ### Problem Number 122
# # def pivotBinary(arr , l , r ,k):
# #     pi = findPivot(arr , l , r)
# #     if pi == -1:
# #         return binarysearch(arr , l , r ,k)

# #     if arr[pi] == k:
# #         return pi
# #     if arr[0] <= k:
# #         return binarysearch(arr , l , pi - 1 , k)
# #     return binarysearch(arr , pi + 1 , r , k)


# # def findPivot(arr , l , r):
# #     if l > r:
# #         return -1
# #     if l == r:
# #         return l
# #     mid =  l + (r -l) // 2
# #     if mid < r and arr[mid]  > arr[mid + 1] :
# #         return mid
# #     if mid > l and arr[mid] < arr[mid - 1] :
# #         return (mid -1)
# # #     if arr[l] >= arr[mid] :
# # #         return findPivot(arr , l , mid - 1)
# # #     return findPivot(arr , mid + 1 , r)


# # # def binarysearch(arr ,l  ,r , k):
# # #     if l <= r:
# # #         mid = l + (r- l) // 2
# # #         if arr[mid] == k:
# # #             return mid
# # #         elif arr[mid] < k:
# # #             return binarysearch(arr , mid + 1 , r , k)
# # #         else:
# # #             return binarysearch(arr , l , mid - 1 , k)
# # # a = [5, 6, 7, 8, 9, 10, 1, 2, 3]
# # # # print(pivotBinary(a , 0 , len(a) - 1 , 3))
# # # ### Problem Number 123
# # # def kthElement(arr1 , arr2 , n , m , k):
# # #     i , j = 0 , 0
# # #     arr = []
# # #     while i < n and j < m:
# # #         if arr1[i] <= arr2[j]:
# # #             arr.append(arr1[i])
# # #             i += 1
# # # #         else:
# # # #             arr.append(arr2[j])
# # # #             j += 1
# # # #     while i < n:
# # # #         arr.append(arr1[i])
# # # #         i += 1
# # # #     while j < m :
# # # #         arr.append(arr2[j])
# # # #         j += 1

# # # #     return arr[k -1]

# # # # a = [2 , 3 ,6 , 7 , 9]
# # # # b = [1 , 4 , 8 , 10]

# # # # print(kthElement( a , b , 5 , 4  , 5))
# # # #### Problem Number 124
# # # # def angryCow()
# # # #### Problem 125

# # def isPossible(arr , n , m , current_min):
# #     student = 1
# #     sum = 0
# #     for i in range(n):
# #         if arr[i] > current_min:
# #             return False
# #         if sum + arr[i]  > current_min:
# #             student += 1
# # #             sum = arr[i]
# # #             if student > m:
# # #                 return False
# # #         else:
# # #             sum += arr[i]


# # #     return True

# # # def Allocate(arr , n , m):
# # #     result = 10**9
# # #     start , end = 0 , 0
# # #     for i in range(len(arr)):
# # #         end += arr[i]

# # #     while(start <= end):
# # #         mid = (end + start) // 2
# # #         if isPossible(arr , n , m , mid):
# # #             result = min(result , mid)
# # #             end = mid - 1
# # #         else:
# # #             start = mid + 1

# # #     return result

# # # arr = [12, 34, 67, 90]
# # # n = len(arr)
# # # m = 2   # No. of students
# # # print(Allocate(arr , n , m))


# # # ### Problem Number 126
# # def maxArr(arr):
# #     temp = arr[0]
# #     for i in arr:
# #         if i > temp:
# #             temp = i
# #     return temp

# # def minArr(arr):
# #     temp = arr[0]
# #     for i in arr:
# #         if i < temp:
# #             temp = i
# #     return temp

# # def dontCutTrees(arr , n ,k):
# #     start = minArr(arr)
# #     end = maxArr(arr)
# #     result = 10**9
# #     while(start <= end):
# #         sum = 0
# #         mid = (start + end) // 2
# #         for i in range(n):
# #             if (arr[i] - mid) > 0:
# #                 sum += (arr[i] - mid)
# #         print(mid)
# #         if sum == k:
# #             return mid
# #         if sum < k:

# #             end = mid - 1
# #         else:
# #             result = mid
# #             start = mid + 1

# #     return result


# # arr = [114, 55, 95, 131, 77, 111, 141 ]
# # print(dontCutTrees(arr , 7 , 95))
# # ### Problem Number 127
# # def job(arr1 , arr2 , arr3 , n):
# #     arr = []
# #     sum = 0
# #     for i in range(n):
# #         arr.append([arr2[i] , arr1[i] , i])
# #     arr.sort()
# #     arr = arr[::-1]
# #     print(arr)

# #     while i < n :
# #         if temp >= arr[i][0]:
# #             temp = arr[i][1]
# #             sum += arr3[arr[i][2]]
# #         else:
# #             i += 1
# #     return sum

# # a = [1 , 2 , 3 , 4 ,6]
# # b = [3 , 5 , 10 ,6 ,9]
# # c = [20, 20, 100, 70, 60]
# # print(job(a , b , c , 5 ))


# # Problem Number 128
# # def AM(A, B, C):
# #     temp = B - A
# #     if C == 0 and A == B:
# #         return 1
# #     elif C == 0 and A != B:
# #         return 0
# #     else:
# #         if temp % C == 0 and ((B > A and C > 0) or (B < A and C < 0)) or A == B:
# #             return 1
# #         else:
# #             return 0


# # a = 10
# # b = 10
# # c = 0
# # print(AM(a, b, c))
# # Problem Number 129
# # Problem Number 130
# # def isPossible(arr , n , m , current_min):
# #     student = 1
# #     sum = 0
# #     for i in range(n):
# #         if arr[i] > current_min:
# #             return False
# #         if sum + arr[i] > current_min:
# #             student += 1
# #             sum = arr[i]
# #             if student > m:
# #                 return False
# #         else:
# #             sum += arr[i]
# #     return True

# # # def maxArr(arr):
# # #     a = arr[0]
# # #     for i in arr:
# # #         if i > a:
# # #             a = i
# # #     return a
# # # def painters(a , b , arr):
# # #     if a >= len(arr):
# # #         return maxArr(arr)
# # #     else:
# # #         sum = 0
# # #         result = 10**9
# # #         for i in range(len(arr)):
# # #             sum += arr[i]

# # #         start , end = 0 , sum
# # #         while start <= end:
# # #             mid = (end + start) // 2
# # #             if isPossible(arr , len(arr) , a , mid):
# # #                 result = min(result , mid)
# # #                 end = mid - 1
# # #             else:
# # #                 start = mid + 1
# # #     return result

# # # A = 10
# # # B = 1
# # # C = [1, 8, 11, 3]
# # # print(painters(A , B , C))

# # ### Problem Number 134
# # ### Problem Number 135
# # def merge(arr1 , arr2):
# #     arr = []
# #     i , j = 0 , 0
# #     while(i < len(arr1) and j < len(arr2) ):
# #         if arr1[i] < arr2[j]:
# #             arr.append(arr1[i])
# #             i += 1
# #         else:
# #             arr.append(arr2[j])
# #             j += 1

# #     if i == len(arr1):   arr.extend(arr2[j:])
# #     else: arr.extend(arr1[i:])

# #     return arr

# # def merge_sort(arr):
# #     if len(arr) <= 1:
# #         return arr
# #     mid =  len(arr) // 2
# #     left = arr[:mid]
# #     right = arr[mid:]

# #     merge_sort(left)
# #     merge_sort(right)
# #     return merge(left , right)

# # a = [0 , 3 , 2 , 5]
# # print(merge_sort(a ))


# # # # # ### Fibonnaci sequence
# # # # # # def fib(n):
# # # # # #     if n ==1 or n == 2:
# # # # # #         return 1
# # # # # #     else:
# # # # # #         return fib(n -1 ) + fib(n -2)

# # # # # # print(fib(50))
# # # # # ########Linked List
# # # # # # #### Problem - Line Number 139
# # # # # class Node:
# # # # #     def __init__(self , data):
# # # # #         self.data = data
# # # # #         self.next = None

# # # # # class Linkedlist:
# # # # #     def __init__(self):
# # # # #         self.head = None

# # # # #     def push(self , new_data):
# # # # #         new_data = Node(new_data)
# # # # #         new_data.next = self.head
# # # # #         self.head = new_data

# # # # #     def reverse(self):
# # # # #         prev = None
# # # # #         current =  self.head
# # # # #         while( current is not None):
# # # # #             next = current.next
# # # # #             current.next = prev
# # # # #             prev = current
# # # # #             current = next
# # # # #         self.head = prev

# # # # #     def printlist(self):
# # # # #         temp = self.head
# # # # #         while temp:
# # # # #             print(temp.data)
# # # # #             temp = temp.next


# # # # # # #### Problem - Line Number 140
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

# # # #     def reverse(self ,head , k):
# # # #         current = head
# # # #         prev = None
# # # #         count = 0
# # # #         if not head or head.next is None:
# # #             return
# # #         while current is not None and count < k:
# # #             next = current.next
# # #             current.next = prev
# # #             prev = current
# # #             current = next
# # #         head = prev

# # #         self.reverse(head.next , k)


# # # ll = Linkedlist()
# # # ll.push(20)
# # # ll.push(18)
# # # ll.printlist()
# # # ll.reverse()
# # # ll.printlist()

# # ### deleting the linkedlist
# # def detect(head):
# #     slow = fast = head
# #     while slow and fast and fast.next:
# #         slow = slow.next
# #         fast = fast.next.next
# #         if slow == fast:
# #             return 1

# #     return 0

# # def removeloop(head):
# #     slow = fast = head
# #     while(1):
# #         slow = slow.next
# # #         fast = fast.next.next
# # #         if slow == fast:
# # #             break
# # #     slow = head
# # #     while slow.next != fast.next:
# # #         slow = slow.next
# # #         fast = fast.next
# # #     fast.next = None

# # # def movehead(head):
# # #     if not head or head.next is None :
# # #         return
# # #     temp = head
# # #     while(temp.next.next):
# # #         temp = temp.next
# # #     temp.next = head
# # #     head = temp.next
# # #     temp.next = None

# # # def removeDuplicates(head):
# # #     #code here
# # #     if head == None:
# # #         return
# # #     if head.next != None:
# # #         if head.data == head.next.data:
# # #            temp = head.next
# # #             head.next = head.next.next
# # #             removeDuplicates(head)
# # #         else:
# # #             removeDuplicates(head.next)

# # #     return head

# # #### Binary Trees
# # class Node:
# #     def __init__(self, data):
# #         self.left = None
# #         self.right = None
# #         self.data = data

# #     def insert(self , data):
# #         if self.data:
# #             if data > self.data:
# #                 if self.right is None:
# #                     self.right = Node(data)
# #                 else:
# #                     self.right.insert(data)

# #             if data < self.data:
# #                 if self.left is None:
# #                     self.left = Node(data)
# #                 else:
# #                     self.left.insert(data)

# #     def printlist(self):
# #         if self.left:
# #             self.left.printlist()
# #         print(self.data)
# #         if self.right:
# #             self.right.printlist()

# # def recursivInorder(root):
# #     if root is None:
# #         return
# #     recursivInorder(root.left)
# #     print(root.data , end = " ")
# #     recursivInorder(root.right)

# # def Inorder(root):
# #     stack = deque()
# #     current = root
# #     while stack or current:
# #         if current:
# #             stack.append(current)
# #             current = current.left
# #         else:
# #             temp = stack.pop()
# #             print(temp.data , end = " ")
# #             current = current.right

# # def preOrder(root):
# #     if root in None:
# #         return
# #     print(root.data , end = " ")
# #     preOrder(root.left)
# #     preOrder(root.right)

# # def ItterpreOrder(root):
# #     if root is None:
# #         return
# #     stack = deque()
# #     stack.append(root)
# #     while stack:
# #         curr = stack.pop()
# #         print(curr.data , end = " ")
# #         if curr:
# #             stack.append(curr.left)

# #         if curr:
# #             stack.append(curr.right)

# # def postOrder(root):
# #     if root is None:
# #         return

# #     postOrder(root.left)
# #     postOrder(root.right)
# #     print(root.data , end = " ")

# # def ItterpostOrder(root):
# #     if root is None:
# #         return
# #     stack = deque()
# #     stack.append(root)
# #     ans = deque()
# #     while stack:
# #         curr = stack.pop()
# #         ans.append(curr)
# #         if curr.left:
# #             stack.append(curr.left)

# # #         if curr.right:
# # #             stack.append(curr.right)

# # #     while ans:
# # #         print(ans.pop() , end =  " ")


# # # def leftView(root):
# # #     if root is None:
# # #         return
# # #     stack = deque()
# # #     stack.append(root)
# # #     while stack:
# # #         n = len(stack)
# # #         for i in range(1 , n + 1):
# # #             temp = stack.popleft()
# # #             if i == 1:
# # #                 print(temp.data , end = " ")
# # #             if temp.left:
# # #                 stack.append(temp.left)
# # #             if stack.right:
# # #                 stack.append(temp.right)


# # # def level(root , leve , max_level):
# # #     arr = []
# # #     if root is None:
# # #         return
# # #     if max_level[0] < leve:
# # #         arr.append(root.data)
# # #         max_level[0] = leve

# # #     level(root.right , leve + 1 , max_level)
# # #     level(root.left , leve + 1, max_level)

# # # # #     return arr

# # # # # def rightView(root):
# # # # #     max_level = [0]
# # # # #     level(root ,1 , max_level)

# # def zigzag(root):
# #     arr = []
# #     if root is None:
# #         return
# #     currnt = []
# #     next1 = []
# #     lt = True
# #     currnt.append(root)
# #     while len(currnt) > 0:
# #         temp = currnt.pop(-1)
# #         arr.append(temp)

# #         if lt :
# #             if temp.left:
# #                 next1.append(temp.left)
# #             if temp.right:
# #                 next1.append(temp.right)

# #         else:
# #             if temp.right:
# #                 next1.append(temp.right)
# #             if temp.left:
# #                 next1.append(temp.left)

# #         if len(currnt) == 0:
# #             lt = not lt
# #             currnt , next1 =  next1 , currnt
# # def searchBinary(root , k):
# #     if root is None or root.val == k:
# #         return root
# #     if root.val < k:
# #         return searchBinary(root.right , k)
# #     return searchBinary(root.left , k)

# # Insert in Binary tree
# # def Insert(root , k):
# #     if root is None:
# #         return Node(k)
# #     else:
# #         if root.key == k:
# #             return k
# #         elif root.key < k:
# #             root.right = Insert(root.right , k)
# #         else:
# #             root.left = Insert(root.left , k )

# #     return root
# # def minElement(root):
# #     if root is None:
# #         return
# #     return minElement(root)
# # def predandsucess(root , k , p , q):
# #     if root is None:
# #         return
# #     predandsucess(root.left , k , p , q )
# #     if root and root.data > k:

# #         if ((not p[0]) or p[0] and p[0] >root.data ):
# #             p[0] = root

# #     elif(root and root.data < k):
# #         q[0] = root
# #     predandsucess(root.right , k , p , q)

# #     return p , q
# # def CheckBST(root):
# # def deleting(root , k ):
# # class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.left = None
# #         self.right = None

# # def inorder(root):
# #     if root is not None:
# #         inorder(root.left)
# #         print(root.data)
# #         inorder(root.right)

# # def insert(node, key):
# #     if node is None:
# #         return Node(key)
# #     if key < node.key:
# #         node.left = insert(node.left, key)
# #     else:
# #         node.right = insert(node.right, key)
# #     return node
# # def minValueNode(node):
# #     current = node
# #     while(current.left is not None):
# #         current = current.left

# #     return current

# # def deleteNode(root, key):
# #     if root is None:
# #         return root
# #     if key < root.key:
# #         root.left = deleteNode(root.left , key)
# #     elif key > root.key:
# #         root.right = deleteNode(root.right , key)
# #     else:
# #         if root.left is None:
# #             temp = root.right
# #             root = None
# #             return temp
# #         elif root.right is None:
# #             temp = root.left
# #             root = None
# #             return temp

# #         temp = minValueNode(root.right)
# #         root.key = temp.key
# #         root.right  = deleteNode(root.right , temp.key)

# # root = None
# # root = insert(root, 50)
# # root = insert(root, 30)
# # root = insert(root, 20)
# # root = insert(root, 40)
# # root = insert(root, 70)
# # root = insert(root, 60)
# # root = insert(root, 80)
# # root = insert(root , 90)
# # print(inorder(root))
# # int_min = -9999
# # int_max= 99999
# # def bST(root):
# #     return isBST(root , int_min , int_max)
# # def isBST(root , min , max):
# #     if root is None:
# #         return True
# #     if root.key < min or root.key > max:
# #         return False
# #     tap = isBST(root.left , min , root.key - 1) and isBST(root.right , root.key + 1 , max)
# #     return tap
# # print(bST(root))
# # def findLCA(root  , n1 , n2) :
# #     if root is None : return None
# #     if root.key == n1 or root.key == n2:
# #         return root
# #     leftLCA = findLCA(root.left, n1 , n2)
# #     rightLCA = findLCA(root.right , n1 , n2 )
# #     if leftLCA and rightLCA:
# #         return root
# #     return leftLCA if leftLCA is not None else rightLCA
# # arr = []
# # def toBalance(root , arr):
# #     if root is not None:
# #         toBalance(root.left , arr)
# #         arr.append(root.key)
# #         toBalance(root.right , arr)
# #     return arr
# # def buildtree(arr , start , end):
# #     if start > end:
# #         return None
# #     mid = (start + end) // 2
# #     node = arr[mid]
# #     node.left = buildtree(arr , start , mid - 1)
# #     node.right = buildtree(arr , mid + 1 , end)
# #     return node

# # print(toBalance(root , arr))
# # def inorderTra(root , arr):
# #     if root is None:
# #         return
# #     inorderTra(root.left , arr)
# #     arr.append(root.key)
# #     inorderTra(root.right , arr)
# # def buildtree(arr , start , end):
# #     if start > end:
# #         return None
# #     mid = (start + end) // 2
# #     node = arr[mid]
# #     node.left = buildtree(arr , start , mid - 1)
# #     node.right = buildtree(arr , mid + 1 , end)
# #     return node

# # def mergeTwo(t1 , t2):
# #     arr1 , arr2 , arr3 = [] , [] , []
# #     inorderTra(t1 , arr1)
# #     inorderTra(t2 , arr2)
# #     arr3 = arr1 + arr2
# #     arr3.sort()
# #     buildtree(arr3 , 0 , len(arr3) - 1)
# # Problem Number 225
# # def kthLargest(root , k , c):
# #     if root is None or c[0] >= k:
# #         return
# #     kthLargest(root.right , k , c)
# #     c[0] += 1
# # #     if c[0] == k:
# # #         return root.data
# # #     kthLargest(root.left , k , c)

# # # def kthSmallest(root , k):
# # #     arr =  []
# # #     inorderTra(root , arr)
# # #     return arr[k -1]

# # # print(kthSmallest(root , 3))
# # # def findNode(root , k):
# # #     if root is None:
# # #         return False

# # #     if root.key == k:
# # #         return True

# # #     res = findNode(root.left , k)
# # #     if res :
# # #         return True
# # #     res2 = findNode(root.right , k)
# # #     return res2

# # # print(findNode(root , 15))
# # def inorderTra(root , arr):
# #     if root is None:
# #         return
# #     inorderTra(root.left , arr)
# #     arr.append(root.key)
# #     inorderTra(root.right , arr)
# # def countNode(root):
# #     c = 1
# #     if root is None:
# #         return 0
# #     c += countNode(root.left)
# #     c += countNode(root.right)
# #     return c
# # def getNode(root):
# #     arr = []
# #     k = countNode(root)
# #     inorderTra(root , arr)
# #     if k % 2 == 0:
# #         return (arr[k // 2] + arr[k // 2 - 1] ) / 2
# #     return arr[k // 2]

# # print(getNode(root))

# # def nodeLie(root , l , h ):
# #     if root is None:
# #         return 0
# #     if root.key >= l and root.key <= h:
# #         return 1 + nodeLie(root.left , l , h ) + nodeLie(root.right , l , h)
# #     if root.key < l:
# #         return nodeLie(root.right , l , h)
# #     else:
# #         return nodeLie(root.left , l , h)

# # print(nodeLie(root , 20 , 70))
# # def insert(root , k):
# #     global succ
# #     if root is None:
# #         return Node(k)
# #     if root.data < k:
# #         root.right = insert(root.right , k)
# #     else:
# #         succ = root
# #         root.left = insert(root.left , k)
# #     return root
# # root = None
# # root = insert(root , 20)
# # root = insert(root , 30)
# # root = insert(root ,50 )
# # root = insert(root , 60)
# # root = insert(root , 40)
# # print(inorder(root))
# # def arrtoBST(arr , n):
# #     global succ
# #     for i in range(n -1 , -1 , -1):
# #         succ = None
# #         root = insert(root , arr[i])

# #         if succ:
# #             arr[i] = succ.data
# #         else:
# #             arr[i] = -1
# #     return arr

# # # # # # # #### Problem - Line Number 238
# # # # def maximumMeetings(n,start,end):
# # # #     arr = list()
# # # #     arr2 = list()
# # # #     for i in range(len(start)):
# # # #         arr.append([end[i] , start[i] , i])
# # # #     arr.sort()
# # # #     arr = arr[::-1]
# # # #     arr2.append(arr[0][2] + 1)
# # # #     temp = arr[0][1]
# # # #     for i in arr:
# # # #         if i[0] < temp:
# # # #             arr2.append(i[2] + 1)
# # # #             temp = i[1]


# # # #     return arr2[::-1]


# # # # s = [1,3,0,5,8,5]
# # # # e = [2,4,6,7,9,9]
# # # # print(maximumMeetings(6 , s , e))
# # # # Problem - Line Number 239
# # # # def problemded(job , n):


# # # # job = [[1 , 4 , 20] , [2 , 1 , 10]]
# # # #### Problem Number 240
# # # ### Uninon of Two sorted array
# # def mergeArray(a , b , n , m ):
# #     arr = []
# #     i , j = 0 , 0
# #     while i < n and j < m:
# #         if a[i] <= b[j]:
# #             if a[i] not in arr:
# #                 arr.append(a[i])
# #                 i += 1
# #             else:
# #                 i += 1
# #         elif a[i]  > b[j]:
# #             if b[j] not in arr:
# #                 arr.append(b[j])
# #                 j += 1
# #             else:
# #                 j += 1

# #     while i < n:
# #         if a[i] not in arr:
# #             arr.append(a[i])
# #             i += 1
# #         else:
# #             i += 1
# #     while j < m:
# #         if b[j]  not in arr:
# #             arr.append(b[j])
# #             j += 1
# #         else:
# #             j += 1

# #     return arr


# # a = [2, 2, 3, 4, 5]
# # b = [1, 1, 2, 3, 4]
# # print(mergeArray(a , b , 5 , 5))
# # Problem 242
# # def FractionalKnapsack(W, value, weight, n):
# #     count = 0
# #     arr = [0]*n
# #     for i in range(n):
# #         arr[i] = ([value[i] / weight[i] , weight[i] , i])
# #     arr.sort(reverse=True)
# #     j = 0
# #     while W != 0 and j < n:
# #         if arr[j][1] <= W:
# #             count += arr[j][0] * arr[j][1]
# # #             W -= arr[j][1]
# # #             j += 1
# # #         else:
# # #             count += W * arr[j][0]
# # #             W = 0
# # #             j += 1

# # #     return count

# # # value = [60,100,120]
# # # weight = [10,20,30]
# # # print(FractionalKnapsack(50 ,value , weight , 3 ))
# # ## Problem 243
# # # def CoinPiles(n , arr , k):
# # #     arr.sort()
# # #     sumcoin = 0
# # #     extraCoin = 0
# # #     for i in range(n):
# # #         for j in range(i + 1 , n):
# # #             if arr[j] - arr[i] > k:
# # #                 sumcoin += arr[i]

# # #     for i in range(1 , n ):
# # #         if arr[i] - arr[0] > k:
# # #             extraCoin += arr[i] - k - arr[0]

# # #     if sumcoin < extraCoin:
# # #         return sumcoin
# # #     else:
# # #         return extraCoin

# # # a = [1 , 1 , 1 , 1 , 12]
# # # print(CoinPiles (5 , a , 9))
# # ### Problem Number 245
# # def minimumPlatform(n,arr,dep):
# #     '''
# #     :param n: number of activities
# #     :param arr: arrival time of trains
# #     :param dep: corresponding departure time of trains
# #     :return: Integer, minimum number of platforms needed
# #     '''
# #     # code here
# #     arr.sort()
# #     dep.sort()
# #     plat = 1
# #     result = 1
# #     i = 1
# #     j = 0
# #     while i < n and j < n:
# #         if arr[i] <= dep[j]:
# #             plat += 1
# #             i += 1
# #         elif arr[i] > dep[j]:
# #             plat -= 1
# #             j += 1
# #         if plat > result:
# #             result = plat

# #     return result
# # Problem Number
# # def BuyStock(n, arr, k):
# #     new_arr = []
# #     for i in range(n):
# #         new_arr.append([arr[i], i + 1])
# #     new_arr.sort()
# #     p = 0
# #     for j in range(n):
# #         p += min(new_arr[j][1], k // new_arr[j][0])
# #         k -= arr[j] * min(new_arr[j][1], k // new_arr[j][0])
# #     return p


# # a = [7,10,14]
# # print(BuyStock(3 , a , 100))
# # Problem Number
# # def  foodNeed(S , N , M):
# #     if ((N*6 < M*7) and S > 6 ) or M > N:
# #         return False
# #     else:
# #         day = (S*M) // N
# #     if (S*M) % N != 0:
# #         day += 1
# #         print(day)
# # print(foodNeed(10 , 16 , 2))
# # def meeting(arr1 , arr2):
# #     arr3 = []
# #     for i in range(len(arr1)):
# #         arr3.append([arr2[i] , arr1[i] , i])
# #     arr3.sort(reverse=True)
# #     temp = at
# #     for i in range(len(arr3)):
# ####
# # def maximizeSum(a, n, k):
# #     sum = 0
# #     minElement = -9999
# #     count =0
# #     for i in range(n):
# #         if a[i] < 0:
# #             count += 1

# #     for i in range(n):
# #         if k > count:
# #             sum += a[i] if a[i] > 0 else -a[i]
# #             a[i] = a[i] if a[i]  > 0 else -a[i]
# #         elif k == 0:
# #             sum += a[i]
# #     if k % count != 0:
# #         temp = k % count
# #         if temp % 2 != 0:
# #             sum -= minElement

# #     return sum

# # # a = [5, -2, 5, -4, 5, -12, 5, 5, 5, 20]
# # # print(maximizeSum( a , 10 , 5))
# # # problem 255
# # # def maxper(arr , n):
# # #     arr.sort()
# # #     i = 0
# # #     j = n -1
# # #     sum = 0
# # #     while i < j:
# # #         sum += (arr[j] - arr[i]) + (arr[j] - arr[i + 1])
# # #         i += 1
# # #         j -= 1
# # #     if n % 2 != 0:
# # #         return sum + (arr[j] - arr[0])
# # #     return sum + (arr[j + 1] - arr[0])
# # # a = [1, 2, 4, 8 ]
# # # print(maxper(a ,4))
# # # def check(arr , n):
# # #     if n not in arr:
# # #         return True
# # #     return False
# # # def pageFaults(arr , f):
# # #     count = 0
# # #     j = 0
# # #     for i in range(f -1 , len(arr)):
# # #         if check(arr[:f] , arr[i]):
# # #             arr[j] = arr[i]
# # #             j += 1
# # #             count += 1
# # #     return count + f
# # # # arr = [5, 0, 1, 3, 2, 4, 1, 0, 5]
# # # # arr = [3 ,1 , 0 ,2 , 5 , 4 , 1 , 2]
# # # # arr = [1, 2, 3, 4, 1, 5, 1]
# # # arr = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, ]
# # # print(pageFaults(arr , 4))
# # # Problem Number 264
# # # def badProblem(arr):
# # #     if len(arr) == 0:
# # #         return 0
# # #     sum = 0
# # #     for i in range(len(arr)):
# # #         arr[i+1]  = arr[i]
# # #         sum += abs(arr[i])
# # #     return sum

# # # #### problem 265
# # # # def googleCodeJam(N,K,B,T,arr,vel ):
# # # #     count = 0
# # # #     swap = 0
# # # #     canReach = 0
# # # #     for i in range(N - 1 , -1 , -1):
# # # #         distance = B - arr[i]
# # # #         canCover = T * vel[i]
# # # #         if distance <= canCover:
# # # #             count += 1
# # # #             if canReach > 0:
# # # #                 swap += canReach
# # # #         else:
# # # #             canReach += 1
# # # #         if count == K:
# # # #             break
# # # #     else:
# # # #         return False
# # # # probkem 249 and 266
# # # def cutBoard(arr1 , arr2 , n , m):
# # #     arr1.sort(reverse = True)
# # #     arr2.sort(reverse = True)
# # #     res = 0
# # #     hor = 1
# # #     ver = 1
# # #     i , j = 0 , 0
# # #     while i < n and j < m:
# # #         if arr1[i] > arr2[j]:
# # #             res += arr1[i] * ver
# # #             i += 1
# # #             hor += 1
# # #         else:
# # #             res += arr2[j]* hor
# # #             j += 1
# # #             ver += 1
# # #     total = 0
# # #     while i < n:
# # #         total += arr1[i]
# # #         i += 1
# # #     res += total * ver

# # #     total = 0
# # #     while j < m:
# # #         total += arr2[j]
# # #         j += 1
# # #     res += total * hor

# # #     return res

# # # aa = [2, 1, 3, 1, 4]
# # # bb = [4, 1, 2]
# # # print(cutBoard(aa , bb , 5 , 3))
# # ### Backtracking
# # ### Stack
# # ## Problem - 302
# # # def revese(s):
# # #     stack = list(s)
# # #     return ''.join(stack[::-1])
# # # print(revese('geeks'))
# # ## Problem - 303
# # def push(arr, ele):
# #     # Code here
# #     arr.append(ele)

# # # Function should pop an element from stack
# # def pop(arr):
# #     # Code here
# #     arr.pop()

# # # # function should return 1/0 or True/False
# # # def isFull(n, arr):
# # #     # Code here
# # #     if len(arr) == n:
# # #         return True
# # #     return False


# # # # function should return 1/0 or True/False
# # # def isEmpty(arr):
# # #     #Code here
# # #     if len(arr) < n:
# # #         return True
# # #     return False

# # # # function should return minimum element from the stack
# # # def getMin(n, arr):
# # #     # Code here
# # #     minEle = arr[0]
# # #     for i in range(n):
# # #         if arr[i] < minEle:
# # #             minEle = arr[i]
# # #     return minEle

# # # def nextLargest(arr ,n):
# #     # newArr = [0]*n
# #     # newArr[n-1] = arr[n-1]
# #     # for i in range(n -2 , -1 , -1):
# #     #     if arr[i] > newArr[i + 1]:
# #     #         newArr[i] = arr[i]
# #     #     else:
# #     #         if arr[i] > arr[i + 1] and arr[i] < newArr[i + 1]:
# #     #             newArr[i] = newArr[i+1]
# #     #         else:
# #     #             newArr[i] = arr[i+1]
# #     # for i in range(n):
# #     #     if arr[i] == newArr[i]:
# #     #         j = i +1
# #     #         while j < n :
# #     #             if arr[i] < arr[j]:
# #     #                 newArr[i] = arr[j]
# #     #                 break
# #     #             else:
# #     #                 j += 1
# #     # for i in range(n):
# #     #     if newArr[i] == arr[i]:
# #     #         newArr[i]  = -1

# #     # return newArr
# # def createStack():
# #     stack = []
# #     return stack

# # def isEmpty(stack):
# #     return len(stack) == 0

# # def push(stack, x):
# #     stack.append(x)

# # def pop(stack):
# #     if isEmpty(stack):
# #         print("Error : stack underflow")
# #     else:
# #         return stack.pop()

# # def nextLargest(arr , n):
# #     s = createStack()
# #     element = 0
# #     next = 0
# #     push(s , arr[0])
# #     for i in range(1 , len(arr)):
# #         next = arr[i]
# #         if  isEmpty == False:
# #             element = pop(s)
# #             while element < next:
# #                 print(next)
# #                 if isEmpty == True:
# #                     break
# #                 element = pop(s)
# #             if element > next:
# #                 push(s , element)

# #         push(s , next)

# #     while isEmpty(s) == False:
# #         element = pop(s)
# #         next = -1
# #         print(next)
# # arr = [6,8,0,1,3]
# # arr = [1,3,2,4]
# # arr = [10, 3, 12, 4, 2, 9, 13, 0, 8, 11, 1, 7, 5, 6]
# # print(nextLargest(arr , 14))
# # problem - 307
# # def check(s):
# #     if s == '+' or s == '-' or s == '/' or s == '*':
# #         return True
# #     return False

# # def postFix(S):
# #     stack = []
# #     for i in range(len(S)):
# #         if not check(S[i]):
# #             stack.append(int(S[i]))
# #         else:
# #             k1 = stack.pop()
# #             k2 = stack.pop()
# #             if S[i] == '+':
# #                 stack.append(k1 + k2)
# #             elif S[i] == '-':
# #                 stack.append(k2 - k1)
# #             elif S[i] == '/':
# #                 stack.append(k2 // k1)
# #             else:
# #                 stack.append(k2 *k1)

# #     return stack.pop()
# # print(postFix('123+*8-'))

# # Reverse Stack - 309
# # def isEmpty(s):
# #     if len(s) == 0:
# #         return True
# #     return False
# # def push(s, a):
# #     s.append(a)
# # def pop(s):
# #     return s.pop()

# # def remove(s, items):
# #     if isEmpty(s):
# #         push(s,items)
# #     else:
# #         temp = pop(s)
# #         remove(s, items)
# #         push(s , temp)
# # def reverse(s):
# #     if not isEmpty(s):
# #         temp = pop(s)
# #         reverse(s)
# #         remove(s,temp)
# # def isGreater(s,items):
# #     if isEmpty(s) or items > s[:-1]:
# #         push(s,items)
# #     else:
# #         temp = pop(s)
# #         isGreater(s,items)
# #         s.append(s)

# # def sort(s):
# #     if not isEmpty(s):
# #         temp = pop(s)
# #         sort(s)
# #         isGreater(s,temp)
# # Problem - 311
# # def overlappedInterval(parr,n):
# #     parr.sort()
# #     arr = []
# #     arr.append(parr[0][0])
# #     temp = parr[0][1]
# #     for i in range(1 , len(parr)):
# #         if  temp < parr[i][0]:
# #             arr.append(temp)
# #             arr.append(parr[i][0])
# #             temp = parr[i][1]
# #         elif temp > parr[i][0] and temp < parr[i][1]:
# #             temp = parr[i][1]
# #         else:
# #             continue
# #     arr.append(temp)
# #     return arr

# # # arr = [[6,8],[1,9],[2,4],[4,7]]
# # #arr = [[1,3],[2,4],[6,8],[9,10]]
# # arr = [[1,3],[2,6],[8,10],[15,18]]
# # print(overlappedInterval(arr,4))
# # Problem 313
# ###
# # def unWanted(S):
# #     stack = []
# #     for ch in S:
# #         if ch == ")":
# #             top = S[-1]
# #             stack.pop()
# #             bool = True
# #             while top != "(":
# #                 if top == "+" or top == "-" or top == "/" or top == "*":
# #                     bool = False
# #                 top = S[-1]
# #                 stack.pop()
# #                 if bool == True:
# #                     return True
# #         else:
# #             stack.append(ch)
# #     return False
# # def  CircularTour(list , n):
# #     i,sum,dis = 0,0,0
# #     while i < n-1:
# #         if sum + list[i][0] < dis + list[i][1]:
# #             temp = list.pop(0)
# #             list.append(temp)
# #             i += 1
# #             sum += list[i][0]
# #             dis += list[i][1]
# # Problem 328
# # def problem328(arr, n, k):
# #     stack = []
# #     for i in range(n-k+1):
# #         flag = False
# #         for j in range(0, k):
# #             if arr[i + j] < 0:
# #                 stack.append(arr[i+j])
# #                 flag = True
# #                 break
# #         if flag == False:
# #             stack.append(0)
# #     return stack
# # def problem328(arr,n,k):
# #     stack =[]
# #     first = 0
# #     for i in range(k-1,n):
# #         while first < i and (arr[first] > 0 or first <= i -k):
# #             first += 1
# #         stack.append(arr[first]) if arr[first] < 0   else stack.append(0)
# #     return stack

# # arr = [12, -1, -7, 8, -15, 30, 16, 28]
# # print(problem328(arr, 8, 3))
# # Heap and Heap Sort
# # import sys


# # class Heap:
# #     def __init__(self, maxsize):
# #         self.maxsize = maxsize
# #         self.size = 0
# #         self.Heap = [0]*(self.maxsize + 1)
# #         self.Heap[0] = sys.maxsize

# #     def parent(self, pos):
# #         return pos//2

# #     def left(self, pos):
# #         return 2*pos

# #     def right(self, pos):
# #         return 2*pos + 1

# #     def isleaf(self, pos):
# #         if pos >= self.size // 2 and pos <= self.size:
# #             return True
# #         return False

# #     def swap(self, i, j):
# #         self.Heap[i], self.Heap[j] = self.Heap[j], self.Heap[i]

# #     def maxHeap(self, pos):
# #         if not self.isleaf(pos):
# #             if self.Heap[pos] < self.Heap[self.left(pos)] or self.Heap[self.Heap[pos]] < self.Heap[self.right(pos)]:
# #                 if self.Heap[self.right(pos)] < self.Heap[self.left(pos)]:
# #                     self.swap(pos, self.left(pos))
# #                     self.maxHeap(self.left(pos))
# #                 else:
# #                     self.swap(pos, self.right(pos))
# #                     self.maxHeap(self.right(pos))

# #     def insert(self, element):
# #         if self.size >= self.maxsize:
# #             return
# #         self.size += 1
# #         self.Heap[self.size]  = element
# #         current = self.size
# #         while self.Heap[current] > self.Heap[self.parent(current)] :
# #             self.swap(current,self.parent(current) )
# #             current = self.parent(current)

# # def heapSort(arr,n):
# #     for i in range(n//2-1,-1,-1):
# #         Heap.maxHeap(i)

# # def maxHeap(arr,n,i):
# #     largest = i
# #     l = 2*i +1
# #     r = 2*i + 2
# #     if l < n and arr[l] > arr[largest]:
# #         largest = l
# #     if r < n and arr[r] > arr[largest]:
# #         largest = r
# #     if largest != i:
# #         arr[i],arr[largest] = arr[largest],arr[i]
# #         maxHeap(arr,n,largest)
# # def sortlist(a,b):
# #     result = None
# #     if a == None:
# #         return b
# #     if b == None:
# #         return a
        
# #     if a.data <= b.data:
# #             result = a
# #             result.next = sortlist(a.next,b)
# #     else:
# #         result = b
# #         result.next = sortlist(a,b.next)
# #     return result        
# def KsortedLinkedLis(arr,N):


    

# arr = [[1, 2, 3], [4, 5, 6]]
# print(KsortedLinkedLis(arr))
### Problem 348
# def countNode(root):
#     if root is None:
#         return 0
#     return 1 + countNode(root.left) + countNode(root.right)     

# def isBinary(root):
#     if root.left is None and root.right is None:
#         return True
#     if root.right is None:
#         return root.data >= root.left.data    
#     else:
#         if root.data >= root.left.data and root.data >= root.right.data:
#             return isBinary(root.left) and isBinary(root.right)
#         else:
#             return False
### Problem Number - 357
# def bfs(graph,root):
#     visited = []
#     queue = []
#     visited.append(root)
#     queue.append(root)
#     while queue:
#         element = queue.pop(0)
#         print(element)
#         for i in graph[element]:
#             if i not in visited:
#                 visited.append(i)
#                 queue.append(i)
### 359

# def dfs(graph,root,visited):
#     if root not in visited:
#         visited.append(root)
#     for k in graph[root]:
#         dfs(graph,k,visited)   
# visited = dfs()        
# print(visited)         

### cycle in Directed graph - 359
# def Directed(v,visited,rstack,graph):
#     visited[v] = True
#     rstack[v] = True
#     for i in graph[v]:
#         if visited[i] == False:
#             if Directed(i,visited,rstack,graph) == True:
#                 return True
#         elif rstack[i] == True:
#             return True
# def main(graph,V):
#     visited = [False]*V
#     rstack = [False]*V
#     for k in range(V):
#         if visited[k] == False:
#             if Directed(k,visited,rstack,graph) == True:
#                 return True
#         return False                             
##### cyce in undirected 
# def isutil(v,visited,graph,parent):
#     visited[v] = True,
#     for i in range(graph[v]):
#         if visited[i] == False:
#             if isutil(i,visited,graph,v):
#                 return True
#         elif parent != v:
#             return True
#     return False
### Problem 362
# class cell:
#     def __init__(self,x,y,dis=0):
#         self.x = x
#         self.y = y
#         self.dis = 0
# def isInside(x,y,N):
#     if (x >= 1 and x <= N) and (y >= 1 and y <= N):
#         return True
#     return False    
# def steps(KnightPos,TargetPos,N):
#     dx = [2,2,-2,-2,-1,-1,1,1]
#     dy=[2,2,-2,-2,-1,-1,1,1]
#     queue = []
#     queue.append(cell(KnightPos[0],KnightPos[1],0))
#     visited = [[False for j in range(N+1)] for i in range(N+1) ]
#     visited[KnightPos[0]][KnightPos[1]]=True
#     while len(queue) > 0:
#         t = queue[0]
#         queue.pop(0)
#     if t.x == TargetPos[0] and t.y== TargetPos[1]:
#         return t.dist
#     for i in range(8):
#         x = t.x + dx[i]
#         y = t.y + dy[i]  
#         if isInside(x,y,N) and visited[x][y] == False:
#             visited[x][y] = True
#             queue.append(cell(x,y,t.dis+1)) 
# if __name__ == '__main__':        
#     N = 30
#     knightpos = [2, 1] 
#     targetpos = [30, 30] 
#     print(steps(knightpos, targetpos, N)) 
# class cell:
#     def __init__(self,x,y,dis=0):
#         self.x = x
#         self.y = y
#         self.dis = 0
def isInside(x,y,image):
    if (x >= 0 or x <= len(image[0])) or (y >= 0 or y <= len(image)) and image[x][y] == 1:
        return True
    return False   
def nowMain(sr,sc,image,newColor):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    visited = [[False for i in range(len(image[0]))] for j in range(len(image))]                      
    queue = []
    queue.append([sr,sc])
    visited[sr][sc] = True
    image[sr][sc] = newColor
    while queue:
        tx = queue[0][0]
        ty = queue[0][1]
        image[tx][ty] = newColor

        queue.pop(0)
        for i in range(4):
            x = tx + dx[i]
            y = ty + dy[i]
            if isInside(x,y,image) and visited == False:
                queue.append([x,y])
                visited[x][y] = True
    return image

image = [[1,1,1],[1,1,0],[1,0,1]]
newColor = 2
print(nowMain(0,0,image,newColor))                






                