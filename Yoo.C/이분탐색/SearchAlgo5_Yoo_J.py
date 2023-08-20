'''
1. 입력
- test 개수 :T
- 수첩 1: N
- 수첩 1 데이터들
- 수첩 2: M
- 수첩 2 데이터들
목표: 수첩2의 데이터들을 하나씩 뽑아와서 수첩1에
있는 데이터들이 있는지 확인
- 있으면 1, 없으면 0을 엔터 단위로 출력한다.

'''
import sys
sys.stdin = open("in2.txt", "rt")



def check(target):
    lt=0
    rt=N-1
    
    while lt<=rt:
        mid = (lt+rt)//2
        if target<수첩1[mid]:
            rt=mid-1
        elif target>수첩1[mid]:
            lt=mid+1
        else:
            print(1)
            break
    
    if target !=수첩1[mid]:
        print(0)
            

T=int(input())
for j in range(T):
    
    N=int(input())
    수첩1=list(map(int, input().split()))

    M= int(input())
    수첩2=list(map(int, input().split()))

    수첩1.sort()

    for i in 수첩2: 
        check(i)