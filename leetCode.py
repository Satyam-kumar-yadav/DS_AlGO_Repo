### Prblem Number 4
def Median(list1 , list2):
    list1 = sorted(list1 + list2)
    list2.clear()
    n = len(list1)
    if n % 2 == 0 : 
        return (list1[n // 2 - 1] + list1[n // 2]) / 2
    return list1[n // 2]

a = [1 , 2]
b = [3 , 4]
print(Median(a , b))
#### Problem Number 10