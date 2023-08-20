#리스트와 배열의 차이점!!
#map함수 
n= int(input())
lst = list(map(int, input().split()))
count_lst = []
for i in range(23):
    count_lst.append(0)
for i in range(n):
    count_lst[lst[i]-1]+=1

for i in range(23):
    print(count_lst[i], end=" ")
