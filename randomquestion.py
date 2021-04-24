# def sumElement(arr):
#  arr1 = [1]
#  for i in range(len(arr)-1):
#    arr1.append(arr[i] + arr[i+1])
#  return arr1 + [1]
# def recu(n):
#  if n == 1:
#    return 1
#  if n == 2:
#    return [1]*2
#  else:
#    return sumElement(recu(n-1))
# print(recu(5))
# Google KickStart
#def goodNess(str1, n, k):
#    count = 0
#    for i in range(n // 2):
#        if str1[i] != str1[n-i-1]:
#            count += 1
#    return abs(k - count)

#def oSRec (arr, i, j, Sum):
 
#    if (j == i + 1):
#        return max(arr[i], arr[j])
#    return max((Sum - oSRec(arr, i + 1, j, Sum - arr[i])),
#                (Sum - oSRec(arr, i, j - 1, Sum - arr[j])))
#def optimalStrategyOfGame(arr, n):
    
#    Sum = 0
#    Sum = sum(arr)
#    k = oSRec(arr, 0, n - 1, Sum)
#    return  k , (Sum - k)
#arr = [4, 1, 2, 10]
#print(optimalStrategyOfGame(arr,4))

#def PredictTheWinner(nums):
#        if len(nums) == 1: return nums[0] , 0
#        dp = [[-1 for i in range(len(nums)+1)] for j in range(len(nums)+1)]
        
#        def game(i,j):
#            if i > j:
#                return 0
#            if i == j:
#                return nums[i]
#            if dp[i][j] != -1: 
#                return dp[i][j]
#            op1 = nums[i] + min(game(i+2,j),game(i+1,j-1))
#            op2 = nums[j] + min(game(i,j-2),game(i+1,j-1))
            
#            dp[i][j] = max(op1,op2)
#            return dp[i][j]
        
#        result = game(0,len(nums)-1)
#        total = sum(nums)
#        return result , (total-result)
#arr = [4,1]
#print(PredictTheWinner(arr))
#def max_hap(arr):
#    o = [0]*len(arr)
#    for i in range(len(arr)):
#        for j in range(len(arr)-1, i,-1):
#            if arr[i] - arr[j] > 0 and i != j:
#                o[i] = j - i -1
#                print(o[i])
#                k = o[i]
#                if k == 0:
#                    o[i] = 111
#                break
#    for i  in range(len(o)):
#        if o[i] == 0:
#            o[i] = -1
#        elif o[i] == 111:
#            o[i] = 0
            
    
##arr = [15,1 ,8, 15, 3]
#arr = [4,10,3,12,7,11]
#print(max_hap(arr))