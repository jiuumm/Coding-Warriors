#230719 WED
#06-1 정렬 알고리즘
#핵심은 교환,선택, 삽입!

#06-2 버블 정렬
#실습 6-1
#버블 정렬 알고리즘 구현하기

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    '''버블 정렬'''
    n= len(a)
    for i in range(n-1):
        for j in range(n-1, i,-1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j],a[j-1]

if __name__ == '__main__':
    print('버블 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num #원소 수가 num인 배열 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    bubble_sort(x)      # 배열 x를 버블 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')


#실습 6-2
#버블 정렬 알고리즘 구현하기(정렬 과정을 출력)

from typing import MutableSequence

def bubble_sort_verbose(a: MutableSequence) -> None:
    '''버블 정렬(정렬 과정을 출력)'''
    ccnt = 0    #비교 횟수
    scnt = 0    #교환 횟수
    n= len(a)
    for i in range(n-1):
        print(f'패스{i+1}')
        for j in range(n-1,i,-1):
            for m in range(0,n-1):
                print(f'{a[m]:2}' + (' ' if m!= j-1 else
                                     '+' if a[j-1] > a[j] else '-'),
                      end='')
                print(f'{a[n-1]:2}')
                ccnt+=1
                if a[j-1] > a[j]:
                    scnt += 1
                    a[j-1], a[j] = a[j], a[j-1]
            for m in range(0,n-1):
                print(f'{a[m]:2}', end=' ')
            print(f'{a[n-1]:2}')
        print(f'비교를 {ccnt}번 했습니다.')
        print(f'교환을 {scnt}번 했습니다.')
        #생략..

    #실습 6-3
    #버블 정렬 알고리즘 구현하기(알고리즘 개선1)

    from typing import MutableSequence

    def bubble_sort(a: MutableSequence) -> None:
        '''버블 정렬(교환 횟수에 따른 중단)'''
        n = len(a)
        for i in range(n-1):
            exchng = 0      #패스에서 교환 횟수
            for j in range(n-1,i,-1):
                if a[j-1] > a[j]:
                    a[j-1], a[j] = a[j], a[j-1]
                    exchng += 1
            if exchng ==0:
                break

    #실습 6-5
    #셰이커 정렬 알고리즘 구현하기

    from typing import MutableSequence

    def shaker_sort(a:MutableSequence) -> None:
        '''셰이커 정렬'''
        left = 0
        right = len(a)-1
        last = right
        while left < right:
            for j in range(right, left, -1):
                if a[j-1] > a[j]:
                    a[j-1], a[j] = a[j], a[j-1]
                    last = j
            left = last

            for j in range(left,right):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
                    last = j
            right = last


    #06-3 단순 선택 정렬
    #단순 선택 정렬 알고리즘 구현하기

    def selection_sort(a:MutableSequence) -> None:
        '''단순 선택 정렬'''
        n = len(a)
        for i in range(n-1):
            min = i     #정렬할 부분에서 가장 작은 원소의 인덱스
            for j in range(i+1, n):
                if a[j] < a[min]:
                    min = j
            a[i], a[min] = a[min], a[i]
                #정렬할 부분에서 맨 앞의 원소와 가장 작은 원소를 교환


    #06-4 단순 삽입 정렬
    '''알고리즘의 개요
        for i in range(1,n):
        tmp <- a[i]를 넣습니다
        tmp를 a[0], ... , a[i-1]의 알맞은 위치에 삽입합니다'''

    # 단순 삽입 정렬 알고리즘 구현하기

    def insertion_sort(a: MutableSequence) -> None:
        '''단순 삽입 정렬'''
        n = len(a)
        for i in range(1,n):
            j=i
            tmp = a[i]
            while j>0 and a[j-1] > tmp:
                a[j] = a[j-1]
                j -= 1
            a[j] = tmp

    if __name__ == '__main__':
        print('단순 삽입 정렬을 수행합니다.')
        num = int(input('원소 수를 입력하세요: '))
        x = [None] *num     #원소 수가 num인 배열 생성

        for i in range(num):
            x[i] = int(input(f'x[{i}]: '))

        insertion_sort(x)   #배열 x를 단순 삽입 정렬

        print('오름차순으로 정렬했습니다.')
        for i in range(num):
            print(f'x[{i}] = {x[i]}')

#이진 삽입 정렬 알고리즘 구현하기

def binary_insertion_sort(a:MutableSequence) -> None:
    '''이진 삽입 정렬'''
    n = len(a)
    for i in range(1,n):
        key = a[i]
        pl = 0                  #검색범위 맨앞원소 인덱스
        pr = i-1                #검색범위 맨끝원소 인덱스

        while True:
            pc = (pl+pr) //2    #검색범위 가운데원소 인덱스
            if a[pc] ==key:     #검색 성공
                break
            elif a[pc] == key:
                pl = pc +1      #검색 범위를 뒤쪽 절반으로 좁힘
            else:
                pr = pc -1      #검색 범위를 앞쪽 절반으로 좁힘
            if pl>pr:
                break

        pd = pc+1 if pl<= pr else pr+1  #삽입해야 할 위치의 인덱스

        for j in range(i,pd,-1):
            a[j] = a[j-1]
        a[pd] = key

if __name__ == '__main__' :
    print('이진 삽입 정렬을 수행합니다.')
    num = int(input("원소 수를 입력하세요: "))
    x = [None] * num                #원소수가 num인 배열 생성

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))

    binary_insertion_sort(x)        #배열 x를 이진삽입정렬

    print('오름차순으로 정렬했습니다')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')


# 이진 삽입 정렬 알고리즘 구현(bisect.insort 사용)

import bisect

def binary_insertion_sort(a:MutableSequence) ->None:
    '''이진 삽입 정렬(bisect.insort사용)'''
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0,i)
