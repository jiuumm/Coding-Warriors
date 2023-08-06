'''
병합정렬은 퀵정렬과 다르게 최악의 경우에도
nlogn의 시간 복잡도를 보장한다.

=> 일단 반으로 나누고 나중에 합친다.
'''

# num=8
# sorted=[0]*num#미리 선언해줘야 함!

# def merge(array, m, mid, n):#m: 시작점, mid: 중간점, n: 끝점
#     i=m
#     j=mid+1
#     k=m
#     #작은 순서대로 배열에 삽입
#     while(i<=mid and j<=n):
#         if(array[i]<=array[j]):
#             sorted[k]=array[i]
#             i+=1
#         else:
#             sorted[k]=array[j]
#             j+=1
#         k+=1
#     #남은 데이터도 삽입
#     if(i>mid): #i가 먼저 끝났다면
#         for t in range(j,n+1):
#             sorted[k]=array[t]
#             k+=1
#     else:
#         for t in range(i, mid+1):
#             sorted[k]=array[t]
#             k+=1
#     # 정렬된 배열을 원본 배열에 삽입!
#     for t in range(m,n+1):
#         array[t]= sorted[t]

# #분할 함수
# def mergeSort(array, m, n):
#     if m<n:
#         mid = (m+n)//2
#         mergeSort(array,m, mid)
#         mergeSort(array, mid+1,n)
#         merge(array,m,mid, n)

# array=[7,6,5,8,3,5,9,1]
# mergeSort(array,0, len(array)-1)
# for i in array:
#     print(i, end=" ")
import sys
N= int(input())
sorted_lst = [0]*N
not_sorted = [0]*N
for i in range(N):
    not_sorted[i]=int(sys.stdin.readline())

def merge(array, m, mid, n):#m: 시작점, mid: 중간점, n: 끝점
    i=m
    j=mid+1
    k=m
    #작은 순서대로 배열에 삽입
    while(i<=mid and j<=n):
        if(array[i]<=array[j]):
            sorted_lst[k]=array[i]
            i+=1
        else:
            sorted_lst[k]=array[j]
            j+=1
        k+=1
    #남은 데이터도 삽입
    if(i>mid): #i가 먼저 끝났다면
        for t in range(j,n+1):
            sorted_lst[k]=array[t]
            k+=1
    else:
        for t in range(i, mid+1):
            sorted_lst[k]=array[t]
            k+=1
    # 정렬된 배열을 원본 배열에 삽입!
    for t in range(m,n+1):
        array[t]= sorted_lst[t]

#분할 함수

def mergeSort(array, m, n):
    if m<n:
        mid = (m+n)//2
        mergeSort(array,m, mid)
        mergeSort(array, mid+1,n)
        merge(array,m,mid, n)
        
mergeSort(not_sorted, 0, N-1)       
for t in sorted_lst:
    print(t)