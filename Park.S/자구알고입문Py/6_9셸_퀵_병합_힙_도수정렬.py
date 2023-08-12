#230719 WED
#06-5 셸 정렬

#실습 6-8
#셸 정렬 알고리즘 구현하기

from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    '''셸 정렬'''
    n = len(a)
    h = n//2
    while h>0:
        for i in range(h,n):
            j = i-h
            tmp = a[i]
            while j>=0 and a[j] > tmp:
                a[j+h] = a[j]
                j -= h
            a[j+h] = tmp
        h//2

if __name__ == '__main__':
    print('셸 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    shell_sort(x)       #배열 x를 셸 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')


#실습 6-9
#셸 정렬 알고리즘 구현하기(h*3+1의 수열 사용)

from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    '''셸 정렬(h*3+1의 수열 사용)'''
    n = len(a)
    h = 1

    while h<n //9:
        h = h*3+1

    while h>0:
        for i in range(h,n):
            j= i-h
            tmp = a[j]
            while j>=0 and a[j] > tmp:
                a[j+h] = a[j]
                j -= h
            a[j+h] = tmp
        h //= 3

if __name__ == '__main__':
    print('셸 정렬을 수행합니다(h*3+1의 수열 사용).')
    num = int(input('원소 수를 입력하세요: '))
    x = [None] *num     #원소 수가 num인 배열 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    shell_sort(x)       #배열 x를 셸 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')


#06-6 퀵 정렬

#실습 6-10
#배열을 두 그룹으로 나누기

from typing import MutableSequence

def partition(a: MutableSequence) -> None:
    '''배열을 나누어 출력'''
    n = len(a)
    pl = 0  #왼쪽 커서
    pr = n-1 #오른쪽 커서
    x = a[n//2] #피벗(가운데 원소)

    while pl<= pr:
        while a[pl] < x: pl +=1
        while a[pr] > x: pr -=1
        if pl<= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    print(f'피벗은 {x}입니다.')

    print('피벗 이하인 그룹입니다.')
    print(*a[0: pl])        #a[0] ~a[pl-1]

    if pl> pr+1:
        print('피벗과 일치하는 그룹입니다.')
        print(*a[pr+1: pl])     #a[pr+1] ~a[pl-1]

        print('피벗 이상인 그룹입니다.')
        print(*a[pr+1: n])      #a[pr+1] ~ a[n-1]

if __name__ == '__main__':
    print('배열을 나눕니다.')
    num = int(input('원소 수를 입력하세요: '))
    x= [None] * num         #원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    partition(x)            #배열 x를 나눠서 출력


#실습 6-11
#퀵 정렬 알고리즘 구현하기

from typing import MutableSequence

def qsort(a: MutableSequence, left:int, right:int) -> None:
    '''a[left] ~a[right]를 퀵정렬'''
    pl = left       #왼쪽 커서
    pr = right      #오른쪽 커서
    x = a[(left+right) //2]     #피벗(가운데 원소)

    # (실습 6-10 동일)

def quick_sort(a:MutableSequence) -> None:
    '''퀵 정렬'''
    qsort(a,0,len(a)-1)

if __name__ == '__main__':
    print('퀵 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요: '))
    x = [None] *num         #원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)       #배열 x를 퀵정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

# (배열을 나누는 과정)
# print(f'a[{left}] ~ a[{right}]:', *a[left : right +1])
# 새로 추가된 부분임


#실습 6-12
#비재귀적인 퀵 정렬 구현하기
#주요 코드

range.push((left,right))

while not range.is_empty():
    pl,pr = left,right = range.pop()

    if left<pr: range.push((left,pr))
    if pl < right: range.push((pl, right))


#실습 6-13
#퀵 정렬 알고리즘 구현하기(원소 수가 9미만이면 단순 삽입 정렬)

from typing import MutableSequence

def sort3(a: MutableSequence, idx1:int, idx2: int, idx3: int) -> None:
    '''a[idx1], a[idx2], a[idx3]을 오름차순으로 정렬하고
    중앙값의 인덱스를 반환'''

    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    if a[idx3] < a[idx2] : a[idx3], a[idx2] = a[idx2], a[idx3]
    if a[idx2] < a[idx1] : a[idx2], a[idx1] = a[idx1], a[idx2]
    return idx2

def insertion_sort(a: MutableSequence, left:int, right:int) -> None:
    '''a[left] ~a[right]를 단순 삽입 정렬'''
    for i in range(left+1, right+1):
        j = i
        tmp = a[i]
        while j >0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -=1
        a[j] = tmp

def qsort(a: MutableSequence, left: int, right: int) -> None:
    '''퀵 정렬'''
    if right-left <9:
        insertion_sort(a, left,right)
    else:
        pl = left
        pr = right
        m = sort3(a,pl,(pl+pr) //2,pr)
        x = a[m]

        a[m], a[pr-1] = a[pr-1], a[m]
        pl +=1
        pr -=2
        while pl <= pr:
            while a[pl] < x:pl +=1
            while a[pr] < x:pr -=1
            if pl <=pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl +=1
                pr -=1

        if left < pr:qsort(a,left,pr)
        if pl< right: qsort(a,pl,right)

    def quick_sort(a:MutableSequence) -> None:
        '''퀵 정렬'''
        qsort(a,0,len(a)-1)

    if __name__ =='__main__':
        print('퀵정렬을 합니다(원소 수가 9 미만이면 단순삽입정렬)')
        num = int(input('원소 수 입력: '))
        x= [None] * num     #원소 수가 num인 배열 생성

        for i in range(num):
            x[i] = int(input(f'x[{i}]: '))

        quick_sort(x)       #배열 x를 퀵 정렬

        print('오름차순으로 정렬했습니다.')
        for i in range(num):
            print(f'x[{i}] = {x[i]}')


    # sorted()함수를 사용해 정렬할 수 있다!

    #06-7 병합 정렬

    #실습 6-14
    #정렬을 마친 두 배열 병합하기

    from typing import Sequence, MutableSequence

    def merge_sorted_list(a:Sequence, b:Sequence,c:MutableSequence) -> None:
        '''정렬을 마친 배열a 와 b를 병합해 c에 저장'''
        pa, pb,pc = 0,0,0           #각 배열의 커서
        na,nb,nc = len(a), len(b), len(c)   #각 배열의 원소 수

        while pa<na and pb< nb:
            if a[pa] <= b[pb]:
                c[pc] = a[pa]
                pa +=1
            else:
                c[pc] = b[pb]
                pb +=1
            pc +=1

        while pa<na:
            c[pc] = a[pa]
            pa +=1
            pc +=1

        while pb< nb:
            c[pc] = b[pb]
            pb += 1
            pc +=1

if __name__ == '__main__':
    a = [2,4,6,8,11,13]
    b = [1,2,3,4,9,16,21]
    c = [None]*(len(a)+len(b))
    print('정렬을 마친 두 배열의 병합을 수행합니다.')

    merge_sorted_list(a,b,c)    #배열a,b 병합해 c에 저장

    print('배열 a와 b를 병합해 배열 c에 저장했습니다.')
    print(f'배열 a: {a}')
    print(f'배열 b: {b}')
    print(f'배열 c: {c}')

# sorted()함수로도 병합 정렬 할 수 있음!
# 정렬을 마치지 않아도 적용할 수 있지만, 속도가 느림
# 빠르게 병합하려면, heapq모듈의 merge()함수 사용!

#병합 정렬 알고리즘 구현

from typing import MutableSequence

def merge_sort(a:MutableSequence) -> None:
    '''병합 정렬'''

    def _merge_sort(a:MutableSequence, left: int, right: int)-> None:
        if left< right:
            center = (left_right) //2

            _merge_sort(a,left,center)  #배열 앞부분 병합정렬
            _merge_sort(a,center+1, right) #배열 뒷부분 병합정렬

            p = j= 0
            i = k = left

            while i<= center:
                buff[p] = a[i]
                p+=1
                i+=1

            while i<= right and j<p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j+=1
                else:
                    a[k] = a[i]
                    i +=1
                k+=1

            while j<p:
                a[k] = buff[j]
                k+=1
                j+=1

        n = len(a)
        buff=[None] *n      #작업용 배열 생성
        _merge_sort(a,0,n-1)    #배열 전체를 병합정렬
        del buff                #작업용 배열 소멸

#06-8 힙 정렬
# 힙정렬 알고리즘 구현

from typing import MutableSequence

def heap_sort(a:MutableSequence) -> None:
    '''힙 정렬'''

    def down_heap(a:MutableSequence, left:int, right:int) -> None:
        temp = a[left]          #루트

        parent = left
        while parent < (right +1)//2:
            cl = parent*2+1         #왼쪽자식
            cr = cl+1               #오른쪽자식
            child = cr if cr<=right and a[cr] > a[cl] else cl   #큰값 선택
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)

    for i in range((n-1) // 2,-1,-1):
        down_heap(a,i,n-1)

    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        down_heap(a,0,i-1)

if __name__ == '__main__':
    print('힙 정렬 수행')
    num = int(input('원소 수 입력하세요: '))
    x = [None] * num            #원소수가 num인 배열 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    heap_sort(x)        #배열 x를 힙정렬

    print('오름차순으로 정렬했습니다')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

# heapq 모듈을 사용하면 heappush(), heappop()함수 사용 가능
# 이 모듈 사용 시 힙 정렬 매우 간결하게 구현가능

#06-9 도수 정렬

#도수 정렬 알고리즘 구현하기

from typing import MutableSequence

def fsort(a: MutableSequence, max : int) -> None:
    '''도수정렬(배열 원솟값은 0이상 max 이하)'''
    n = len(a)          #정렬할 배열a
    f=[0]*(max+1)       #누적 도수분포표 배열 f
    b= [0]*n            #작업용 배열b

    for i in range(n):          f[a[i] +=1]
    for i in range(1,max+1):    f[i]+=1f[i-1]
    for i in range(n-1,-1,-1):  f[a[i]] -= 1; b[f[a[i]]] =a[i]
    for i in range(n):          a[i] = b[i]

def counting_sort(a:MutableSequence) -> None:
    '''도수 정렬'''
    fsort(a,max(a))

if __name__ == '__main__':
    print('도수 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요: '))
    x = [None] *num

    for i in range(num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >=0: break
    counting_sort(x)        #배열 x를 도수정렬

    print('오름차순으로 정렬했습니다.')

    for i in range(num):
        print(f'x[{i}] = {x[i]}')