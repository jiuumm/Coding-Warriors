A,B,C= map(int, input().split())

lst=[0]*3
lst[0]=A
lst[1]=B
lst[2]=C

for i in range(len(lst)-1):
    for j in range(0, len(lst)-1-i):
        if lst[j]>lst[j+1]:
            tmp=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=tmp
            
print(lst[1])

