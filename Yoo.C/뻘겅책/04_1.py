n=int(input())
lst = [0]*n

for i in range(n):
    lst[i]= int(input())

for i in range(n-1):
    for j in range(n-1-i):
        if lst[i]>lst[j+1]:
            tmp = lst[j]
            lst[j]= lst[j+1]
            lst[j+1]=tmp
            
for i in range(n):
    print(lst[i])