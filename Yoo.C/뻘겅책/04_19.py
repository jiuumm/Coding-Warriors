import sys
input=sys.stdin.readline
n, k =map(int, input().split())
A= list(map(int, input().split()))

def quickSort(s,e,k):
    global A
    if s<e:
        pivot = partition(s,e)
        if pivot==k:
            return
        elif k<pivot:
            quickSort(s,pivot-1,k)
        else:
            quickSort(pivot+1,e,k)
    
def swap(i,j):
    global A
    tmp = A[i]
    A[i]=A[j]
    A[j]=tmp
    
def partition (s,e):
    global A
    if s+1==e:
        if A[s]>A[e]:
            swap(s,e)
        return e
    m=(s+e)//2
    swap(s,m)
    pivot=A[s]
    i=s+1
    j=e
    
    while i<=j:
        while pivot<A[j] and j>0:
            j=j-1
        while pivot>A[i] and i<len(A)-1:
            i=i+1
        if i<=j:
            swap(i,j)
            i=i+1
            j=j-1
            
    A[s]=A[j]
    A[j]=pivot
    return j

quickSort(0,n-1, k-1)
print(A[k-1])