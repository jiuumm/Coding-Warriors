n= int(input())
A= list(map(int, input().split()))

res=""
flag=True
for i in range(n):
    max= A[i]
    for j in range(i+1, n): #i보다 오른쪽 탐색
        if max< A[j]:
            max=A[j]
            res+=str(max)+' '
            flag=True
            break

        else:
            flag=False
    if flag==False:
        res+='-1 '
res+='-1 '
print(res)
        