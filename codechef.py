### CodeChef jan long
### Div 3
### Problem 1
def contest(arr , N , K , D):
    sum = 0
    temp = 0
    for i in range(N):
        sum += arr[i]

    if K * D < sum:
         temp = D
    else:
        temp = sum // D

    return temp       

n = 2 
m = 5 
d = 7
arr = [20,  36 ]
print(contest(arr , n , m , d))


