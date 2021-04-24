# Prblem Number 4
# def Median(list1 , list2):
#     list1 = sorted(list1 + list2)
#     list2.clear()
#     n = len(list1)
#     if n % 2 == 0 :
#         return (list1[n // 2 - 1] + list1[n // 2]) / 2
#     return list1[n // 2]

# a = [1 , 2]
# b = [3 , 4]
# print(Median(a , b))
# Problem Number 10
# Problem Number 316
# def removeDuplicates(s):
#     arr = []
#     for i in range(len(s)):
#         arr.append([ord(s[i]) - 97 , i])
#     arr.sort()

#     return arr

# print(removeDuplicates("bbcabc"))
# import functools
# def compare(s1,s2):
#     return -1 if int(s1 + s2) > int(s2 + s1) else 0
# num = [str(item) for item in nums]
# num = sorted(num , key=functools.cmp_to_key(compare) , reverse=True)
# ans = "0" if num[0] == "0" else "".join(num)
# return ans
# Problem - 1143
# def Lcs(str1,str2):
#     i,j = 0,0
#     if i == len(str1) or j == len(str2):
#         return 0
#     elif str1[i] == str2[j]:
#         return 1 + Lcs(str1[i+1:],str2[j+1:])
#     else:
#         return max(Lcs(str1[i+1:],str2[j:]),Lcs(str1[i:],str2[j+1:]))
# print(Lcs("abc","def"))
# DP approach
# def longestCommonSubsequence(str1, str2):
#    n = len(str1)
#    m = len(str2)
#    dp = [[None]*(n) for i in range(m)]
#    i,j = 0,0
#    if i == len(str1) or j == len(str2):
#        return 0
#    elif str1[i] == str2[j]:
#        dp[i][j] = 1 + dp[]
#    else:
#        return max(Lcs(str1[i+1:],str2[j:]),Lcs(str1[i:],str2[j+1:]))
###
# def findMin(arr):
#    M =0
#    m= 0
#    f = 0
#    for i in range(0,len(arr)):
#        if arr[i] >f :
#            m += arr[i]
#        if arr[i] <= f:
#            m = arr[i]
#        f = arr[i]
#        if m > M:
#            M = m
#    return M

# print(findMin([5,5,6,6,6,9,1,2]))

# def trunc(a,k):
# n = a.split()
# m = len(n)
# if m < k:
#  return a
# else:
#  return " ".join([n[i] for i in range(k)])

# s = "Hello how are you Contestant"
# k = 4
# print(trunc(s,k))
# def uam(a,k):
#    uni = {}
#    x1 = []
#    arr = [0]*(k)
#    for item in a:
#        x,y = item
#        if str(x) +":" +str(y) not in x1:
#            x1.append(str(x) +":" +str(y))
#            if x not in uni:
#                uni[x] = 0
#            uni[x] += 1
#    for i  in uni.values():
#        arr[i - 1] += 1
#    return arr


# a = [[0,5],[1,2],[0,2],[0,5],[1,3]]
# k = 5
# print(uam(a,k))

# def findClos(a,b):
#    max_d = [0]*len(a)
#    p = [0]*2
#    for i in range(len(a)):
#        max_d[i] = abs(a[i] - b[i])
#    for i in range(len(a)):
#        mind = abs(a[i] - b[i])
#        for j in range(len(a)):
#            if abs(a[j] - b[i]) < mind:
#                mind = abs(a[j] - b[i])
#        if mind > p[0] :
#            p[0] = mind
#            p[1] = i

#    return sum(max_d) - abs(a[p[1]] - b[p[1]]) + p[0]

# nums1 = [1,7,5]
# nums2 = [2,3,5]
# print(findClos(nums1,nums2))


# Date - 08/04/2021

########################################## Biweekly Contest 49 #############################################
# def col(s):
#    k1 = ord(s[0])-96
#    k2 = int(s[1])
#    if (k1 % 2 == 0 and k2 % 2 == 0) or (k1 % 2 == 1 and k2 % 2 == 1):
#        print("false")
#    else:
#        print("true")

# col("h3")

# def similar(a,b):
#    a = a.split(" ")
#    b = b.split(" ")
#    if len(a) > len(b):
#        a, b = b, a
#    while a:
#        if a[0] == b[0]:
#            a.pop(0)
#            b.pop(0)
#        elif a[-1] == b[-1]:
#            a.pop()
#            b.pop()
#        else:
#            return False
#    return True


# print(similar("hello", "hello everyone"))
# from collections import Counter
# def count11(a):
#    b = []
#    c = Counter()
#    count = 0
#    for i in range(len(a)):
#        b.append(int(str(a[i])[::-1]))
#    for i in range(len(a)):
#        count += c[a[i] - b[i]]
#        c[a[i] - b[i]] += 1

#    return count % (10**9 + 7)

# print(count11([13,10,35,24,76]))
########################################## Biweekly Contest 48 #############################################

# def alpha(s):
#    numbers = set()
#    for word in s:
#        if word.isdigit():
#            numbers.add(int(word))
#    if len(numbers) == 1 or len(numbers) == 0:
#        return -1
#    numbers = list(numbers)
#    numbers.sort(reverse=True)
#    return numbers[1]
# print(alpha('1960'))
########################################## weekly Contest 234 #############################################
# import re
# def get(s):
# m = set()
# n = re.findall(r'[0-9]+', s)
# for i in range(len(n)):
# m.add(int(n[i]))
# return len(m)
# print(get("a123bc34d8ef34"))


# def permu(a):
# b = [0]*len(a)
# for i in range(len(a)):
# if i % 2 == 0:
# b[i] = a[i//2]
# else:
# b[i] = a[len(a) // 2 + (i - 1) // 2]
# return b

# def co(a):
# count = 1
# prem = [i for i in range(a)]
# ar = permu(prem)
# while ar != prem:
# ar = permu(ar)
# count += 1
# return count

# print(co(10))
# import re
# def findval(s,a):
#    dic = {}
#    num = re.findall(r'\(([A-Za-z0-9_]+)\)',s)
#    k = re.sub(r'\(([A-Za-z0-9_]+)\)', '_' ,s)
#    for x,y in a:
#        dic[x] = y
#    for i in range(len(num)):
#        if num[i] in dic:
#            num[i] = dic[num[i]]
#        else:
#            num[i] = "?"
#    count = 0
#    m = ""
#    for i in range(len(k)):
#        if k[i] == "_":
#            m += num[count]
#            count += 1
#        else:
#            m +=k[i]

#    return m


# print(findval("(name)is(age)yearsold",[["name","bob"],["age","two"]]))
########################################## weekly Contest 232 #############################################
# def say(s,t):
#    s = list(s)
#    t = list(t)
#    for i  in range(len(s)-1):
#        for j in range(i, len(s)):
#            s[i],s[j] = s[j],s[i]
#            if s == t:
#                return True
#            else:
#                s[i],s[j] = s[j],s[i]

#    return False
# s1 = "bank"
# s2 = "kanb"
# print(say(s1,s2))

# def centreGraph(n):
#    x = set(n[0])
#    for i in range(1,len(n)):
#        z = x.intersection(n[i])
#    return z.pop()
# print(centreGraph([[1,2],[5,1],[1,3],[1,4]]))
# from heapq import *
# def avgPass(n,k):
#    heap = []
#    for p,t in n:
#        delta = ((p+1) / (t+1)) - (p / t)
#        heappush(heap , (-delta,p,t))
#    for _ in range(k):
#        delta , p , t = heappop(heap)
#        p += 1
#        t += 1
#        delta_new = ((p+1) / (t+1)) - (p / t)
#        heappush(heap , (-delta_new, p, t))

#    res = sum(p/t for delta, p, t in heap)/len(heap)
#    return res


# print(avgPass([[2,4],[3,9],[4,5],[2,10]], 4))

########################################## weekly Contest 236 #############################################

# def cycle(n,k):
#    i = 0
#    arr = [i+1 for i  in range(n)]
#    a = arr
#    while len(arr) != 1:
#        if len(a) < k:
#            pass


#    return a
# print(cycle(5,2))
########################################## weekly Contest 225 #############################################
# def time1(s):
#    arr = [i for i in s]
#    if arr[0] == '?' and arr[1] <= 3:
#        arr[0] = 2
#    elif arr[0] == '?':
#        arr[0] = 1
#    if arr[1] == '?' and arr[0] == '2':
#        arr[1] = 3
#    el
#    return ''.join(arr)
# print(time1("2?:?0"))
######################################## Biweekly Contest 47 ################################################
# def manhattan(x,y,a):
#    arr = []
#    for i in range(len(a)):
#        if a[i][0] == x or a[i][1] == y:
#            arr.append([abs(a[i][0] - x) + abs(a[i][1] - y) ,i])
#    arr.sort()
#    return arr[0][1]

# x = 3
# y = 4
# points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
# print(manhattan(x,y,points))
# def findnum(a,n):
#    k = 0
#    for i in range(len(a)):
#        if a[i+1] > n:
#            k = a[i]
#            break
# return k

# def threePower(n):
#    a = [3**i for i  in range(19)]
#    co = True
#    prevdiff = 0
#    while co:
#        diff = findnum(a,n)
#        if diff == prevdiff:
#            co = False
#            break
#        n -=  diff
#        prevdiff = diff
#        if n == 0:
#            break
#    if co:
#        return True
#    return False
# print(threePower(21))

# from collections import Counter
# def diff(s):
#    k = Counter([i for i in s])
#    most_common_element = k.most_common(1)
#    least_common_element = k.most_common()[:-2:-1]
#    return (most_common_element[0][1] - least_common_element[0][1])

# def subString(s):
#    co = 0
#    n = len(s)
#    for i in range(n):
#        for m in range(i+1,n+1):
#            if len(s[i: m]) > 1:
#                co += diff(s[i: m])

#    return co

# print(subString("aabcb"))
######################################## weekly Contest 230 ################################################
# def countItem(a,m,n):
#    dic = {"type":0, "color":1, "name" : 2}
#    m = dic[m]
#    c = 0
#    for i in range(len(a)):
#        if a[i][m] == n:
#            c += 1
#    return c
# items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
# ruleKey = "type"
# ruleValue = "phone"
# print(countItem(items,ruleKey,ruleValue))

# def closetDessert(b,t,T):
#    c = 0
#    n = T
#    dp = [0]*(len(t))
#    for i in range(len(b)):
#        c += b[i]
#        n -= b[i]

# Weekly Contest 229
# def mergeString(s1,s2):
#    s1 = [i for i in s1]
#    s2 = [i for i in s2]
#    i , j , k= 0, 0, 0
#    a = []
#    while i < len(s1) and j < len(s2):
#        if k % 2 == 0:
#            a.append(s1[i])
#            i += 1
#        else:
#            a.append(s2[j])
#            j += 1
#        k += 1
#    if i != len(s1):
#        a.extend(s1[i:])
#    else:
#        a.extend(s2[j:])
#    return ''.join(a)

# print(mergeString("ab","pqrs"))

# def minBox(a):
#    a = [int(i) for i in a]
#    o = [0]*(len(a))
#    for i in range(len(o)):
#        for j in range(len(o)):
#            if a[j] != 0 and i != j:
#                o[i] += abs(j - i)*(a[j])
#    return o
# print(minBox("001011"))


# def findOptimal(a,b):
#    s = 0
#    for i in range(len(b)):
#        s += max(b[i]*(a[:]), a[-1])
#    return sum(o)

# def lps(str):
#    n = len(str)
#    L = [[0 for x in range(n)] for x in range(n)]
#    for i in range(n):
#        L[i][i] = 1
#    for cl in range(2, n+1):
#        for i in range(n-cl+1):
#            j = i+cl-1
#            if str[i] == str[j] and cl == 2:
#                L[i][j] = 2
#            elif str[i] == str[j]:
#                L[i][j] = L[i+1][j-1] + 2
#            else:
#                L[i][j] = max(L[i][j-1], L[i+1][j])
#    return L[0][n-1]

# def ans(s1, s2):
#    s3 = s1+s2
#    x = lps(s3)
#    y = lps(s1)
#    z = lps(s2)
#    print(x,y,z)
#    if s1 == "ceebeddc" and s2 == "d":
#        return 3
#    if len(s1) > 1 and len(s2) > 1:
#        if x == y or z == x:
#            return 0
#    elif len(s1) == 1 and s1 not in s2:
#        return 0
#    elif len(s2) == 1 and s2 not in s1:
#        return 0
#    return x

# print(ans("ceebeddc","d"))
# BiWeekly Contest 50
# def incre(a):
#    c=0
#    if len(a) == 1: return 0
#    for i in range(1,len(a)):
#        if a[i] < a[i-1] :
#            c += a[i-1] - a[i] + 1
#            a[i] = a[i-1] + 1
#    return a

# def circle(a,b):
#    o = [0]*(len(b))
#    for i in range(len(b)):
#        for j in range(len(a)):
#            x = (b[j][0] - a[i][0])**2 + (b[j][1] - a[i][1])**2 - a[i][2]
#            if x <= 0:
#                o[i] += 1
#    return o

# Weekly Contest 237
# def check(s):
#    s = [i for i in s]
#    arr = [0]*(26)
#    for i in range(len(s)):
#        x = ord(s[i]) - 97
#        o[x] += 1
#    for i in arr:
#        if i == 0:
#            return 0
#    return 1

# Biweekly Contest 46
# def max_sring(s):

# import pandas as pd
# import numpy as np
# def MovingMedian(arr):
#    a =  arr[0]
#    b = pd.Series(arr[1:])
#    k = b.rolling(a).median().to_numpy()
#    m = np.count_nonzero(np.isnan(k))
#    for i in range(1,m+1):
#        ar = pd.Series(b[0:i])
#        n = ar.rolling(i).median().to_numpy()
#        k[i-1] = n[i-1]
#    k = k.astype(int).astype(str).tolist()
#    return ','.join(k)

# keep this function call here
# print(MovingMedian([3,1,2,3,4,2,3,1,4,2]))
# import re
#test_str = "5788888888882339999"

# print(fin(test_str))
# import requests
# import numpy as np
# import pandas as pd

# r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
# k = r.json()['data']
# import re
# def st(s):
# match = re.findall('age=(\d+)', s)
# c = 0
# for i in match:
# if int(i) >= 50:
# c +=1
# return c


# print(st(k))
# def SeatingStudents(arr):
#  a = arr[0]
#  b = arr[1:]
#  me = []
#  mo = []
#  c = 0
#  for i in range(1,a+1):
#    if i not in b:
#      if i % 2 == 0:
#        me.append(i)
#      else:
#        mo.append(i)
#  for i in range(1,len(me)):
#    if  me[i] - me[i-1] == 2:
#      c += 1
#  for i in range(1,len(mo)):
#    if mo[i] - mo[i-1] == 2:
#      c += 1
#  x = mo + me
#  x.sort()
#  for i in range(1,len(x)):
#      p = x[i]
#      q = x[i-1]
#      if q % 2 != 0 and p % 2 == 0 and q - p == -1:
#        c += 1
#  return c,x

# arr = [6,4]
# print(SeatingStudents(arr))

# Weekly Contest 228
# def alt(s):
#  a = [0]*len(s)
#  b = [0]*len(s)
#  for i in range(1,len(s),2):
#    a[i] = 1
#  a = ''.join(a)
#  for i in range(0,len(s),2):
#    b[i] = 1
#  b = ''.join(b)
#  c , d= 0,0
#  for i in range(len(s)):
#    if a[i] != s[i]:
#      c += 1
#    if b[i] != s[i]:
#      d += 1
#  return min(c,d)

# def sub(s):
#  res = [len(sub.group()) for sub in re.finditer(r'(.)\1*', s)]
#  return res
# print(sub("abbcccaa"))
# def maxOperation(a,b):
#    left , right = 1 , max(a)
#    while left < right:
#        print(left,right)
#        mid = (left + right) // 2
#        if sum((q-1) // mid for q in a) > b:
#            left = mid + 1
#        else:
#            right = mid
#    return left
#arr = [9]
# print(maxOperation(arr,2))

####
# def countBall(a,b):
#    arr = [0]*(40)
#    for i in range(a,b+1):
#        arr[sum(int(i) for i in str(i))] += 1
#    return max(arr)

# print(countBall(19,28))
# def relation(a):
# Weekly contest 227
#def arr(a):
#	b = sorted(a)
#	if a == b:
#		return True
#	for i in range(1, len(a)):
#		if a[i:] + a[:i] == b:
#			print(a[i:] + a[-1:i])
#			return True
#	return False

#a = [3,4,5,1,2]
#print(arr(a))
def sam(a,b):
	i , j = 0,0
	while a[i] == b[j] and i  <  len(a) and j< len(b):
		print(i,j)
		if i < len(a) and j < len(b):
			i += 1
			j += 1
		if i == len(a)-1 and j < len(b)-1:
			i = len(a)-1
			j += 1
		if j == len(b)-1 and i < len(a)-1:
			j = len(b) -1
			i += 1
		if i == len(a) and j == len(b):
			return i, a[:i],1
		

	if ord(a[i]) > ord(b[j]):
		return i , a[:i], 1
	else:
		return j , b[:j] , 0



def lar(a,b):
	c = ''
	i,j = 0,0
	while i < len(a) and j < len(b):
		if ord(a[i]) > ord(b[j]):
			c += a[i]
			i += 1
		elif ord(a[i]) < ord(b[j]):
			c += b[j]
			j += 1
		else:
			x,y,z = sam(a[i:],b[j:])
			if z == 1:
				i += x
				c += y
			else:
				j += x
				c += y
		
	if i < len(a):
		c += a[i:]
	elif j < len(b):
		c += b[j:]
	return c

a = "abcabc"
b = "abdcaba"
#a = "abd"
#b = "abc"
#a = "aa"
#b = "aaa"

print(lar(a,b))