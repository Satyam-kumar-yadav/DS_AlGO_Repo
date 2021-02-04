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
#### Problem - 1143
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
def longestCommonSubsequence(str1, str2):
    n = len(str1)
    m = len(str2)
    dp = [[None]*(n) for i in range(m)]
    i,j = 0,0
    if i == len(str1) or j == len(str2):
        return 0
    elif str1[i] == str2[j]:
        dp[i][j] = 1 + dp[]
    else:
        return max(Lcs(str1[i+1:],str2[j:]),Lcs(str1[i:],str2[j+1:]))

