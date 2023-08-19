#셸정렬 알고리즘


from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    
    n = len(a)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 2

if __name__ == '__main__':
    print('셸 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    shell_sort(x)  

    print('오름차순으로 정렬!')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
        
#퀵정렬

from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) -> None:

    pl = left                  
    pr = right                 
    x = a[(left + right) // 2]  

    while pl <= pr:    
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    
    qsort(a, 0, len(a) - 1)

if __name__ == '__main__':
    print('퀵 정렬')
    num = int(input('원소수 입력 : '))
    x = [None] * num   

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)      

    print('오름차순으로 정렬')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
        
        