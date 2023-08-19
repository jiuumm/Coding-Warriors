

a=[6,4,3,7,1,9,8]
n=len(a)
#오름차순
for i in range(n-1):
    for j in range(n-1,i, -1):
        if a[j]<a[j-1]:
            a[j-1], a[j]= a[j], a[j-1]    
print("오름차순 정리")

for i in range(n):
    print(a[i], end= " ")
    
a=[6,4,3,7,1,9,8]
print()
#내림차순
for i in range(n-1):
    for j in range(1, n-i):
        if a[j]>a[j-1]:
            a[j-1], a[j]= a[j], a[j-1]   
print("내림차순 정리") 
for i in range(n):
    print(a[i], end= " ")
print()
#버블정렬 개선
#더이상 swap을 하지 않으면 빠져나온다. 
for i in range(n-1):
    exchange=0
    for j in range(n-1,i, -1):
        if a[j]<a[j-1]:
            a[j-1], a[j]= a[j], a[j-1]    
            exchange+=1
    if exchange==0:
        break

for i in range(n):
    print(a[i], end= " ")