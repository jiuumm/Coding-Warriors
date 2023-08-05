array=[7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
    min_index=i #가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index]>array[j]:
            min_index=j
    array[i], array[min_index]= array[min_index], array[i] #스와프
print(array)
     
    
 #백준 1427번
 
lst = list(input())
for i in range(len(lst)):#O(n)
    lst[i] = int(lst[i]) 

for i in range(len(lst)):
    #일단 최소값을 갖는 인덱스 찾으러 가기
    max_idx = i
    for j in range(i+1, len(lst)):
        if lst[max_idx]<lst[j]:
            max_idx = j
    lst[i], lst[max_idx]= lst[max_idx], lst[i]

for i in lst:
    print(i, end="")         