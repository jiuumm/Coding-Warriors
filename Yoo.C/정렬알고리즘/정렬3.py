#병합정렬


from typing import MutableSequence

def merge_sort(a: MutableSequence) -> None:
   

    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        #재귀적 병합정렬
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center)            
            _merge_sort(a, center + 1, right)       

            p = j = 0
            i = k = left

            while i <= center:
                 buff[p] = a[i]
                 p += 1
                 i += 1

            while i <= right and j < p:
                 if buff[j] <= a[i]:
                     a[k] = buff[j]
                     j += 1
                 else:
                     a[k] = a[i]
                     i += 1
                 k += 1

            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1

    n = len(a)
    buff = [None] * n           
    _merge_sort(a, 0, n - 1)    
    del buff                    


#힙정렬!
'''
병합정렬과 퀵정렬만큼 빠른 정렬 알고리즘!
힙트리구조라는 것을 이용하는 방법

이진트리: 모든 노드의 자식 노드가 2개이하인 트리 구조
트리의 최상단: 루트
트리의 최하단: 리프

완전 이진트리: 이진 트리의 노드가 중간에 비어있지 않고 빽빽히 가득찬 구조
힙(heap): 최솟값이나 최댓값을 빠르게 찾아내기 위해 완전 이진트리를 기반으로 하는 트리
최대 힙: 부모노드가 자식 노드보다 큰 힙
힙 정렬을 만들기 위해서는 정해진 데이터를 힙 구조를 가지도록 만들어야 함.
ex)
        11
    5        8
7       4
힙 생성알고리즘을 사용
힙 생성 알고리즘: 특정한 하나의 노드에 대해서 수행하는 것
하나의 노드를 제외하고는 최대 힙이 구성되어 있는 상태!
(5를 제외하고 최대힙이 구성됨)

-> 특정한 노드의 두 자식 중에서 더 큰 자식과 자신의 위치를 바꾸는 알고리즘
 시간복잡도: log N
 
 배열에 있는 인덱스를 차례대로 트리를 표현하면 됨
 배열을 다시 완전 이진트리로 표현 
 데이터 갯수가 N개-> 전체트리를 힙구조로 만드는 복잡도: N*logN
 
         7
    6        5
8       3  5    9
1  6
         9
    8        7
6       3  5    5
1  6
         6
    8        7
6       3  5    5
                        -> 9 빼주기!
1  9


'''

from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
  

    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        
        #루트
        temp = a[left]     

        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1     
            cr = cl + 1             
            child = cr if cr <= right and a[cr] > a[cl] else cl  
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)
    #다시 a[i] ~ a[n-1]=> 힙 
    for i in range((n - 1) // 2, -1, -1):  
        down_heap(a, i, n - 1)
    #a[0](최댓값), a[i]교환
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0] 
        # a[0] ~ a[i-1]=> 힙    
        down_heap(a, 0, i - 1)      


#도수 정렬
'''
원소의 대소관계를 판단하지 않고 빠르게 정렬하는 알고리즘
매우 빠름
<단계>
1. 도수분포표 만들기
2. 누적도수분포표 만들기
3. 작업용 배열 만들기
4. 배열 복사

'''
from typing import MutableSequence

#1
def fsort(a: MutableSequence, max: int) -> None:
    
    n = len(a)       
# 2  
    f = [0] * (max + 1)  
# 3 
    b = [0] * n          
#4
    for i in range(n):              f[a[i]] += 1                    
    for i in range(1, max + 1):     f[i] += f[i - 1]                
    for i in range(n - 1, -1, -1):  f[a[i]] -= 1; b[f[a[i]]] = a[i]  
    for i in range(n):              a[i] = b[i]                      
#4
def counting_sort(a: MutableSequence) -> None:
    
    fsort(a, max(a))