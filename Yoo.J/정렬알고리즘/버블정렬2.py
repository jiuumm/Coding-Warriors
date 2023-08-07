arr=[5,2,3,4,1]
n = len(arr)#n=5
for i in range(n-1):#i: 0~3:총 4번의 루프를 돈다.
    for j in range(0, n-1-i):
        if arr[j]>arr[j+1]:#오름 차순으로 정렬
            tmp = arr[j]
            arr[j]= arr[j+1]
            arr[j+1]=tmp
for i in arr:
    print(i, end=" ")
    
N=int(input())
lst=[0]*N
for i in range(N):
    lst[i]=int(input())
    
for i in range(N-1):
    for j in range(0, N-1-i):
        if lst[j]>lst[j+1]:
            tmp = lst[j+1]
            lst[j+1]=lst[j]
            lst[j]=tmp
for i in lst:
    print(i)
    
