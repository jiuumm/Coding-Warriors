def factorial(n: int)-> int:
    if n>0:
        return n*factorial(n-1)
    
    else:
        return 1
if __name__=='__main__':
    n=int(input("출력할 팩토리얼 값 입력:"))
    print(f'{n}의 팩토리얼은 {factorial(n)}입니다.')
    
#유클리드 호제법!(이산수학 때 배웠던..) 
def gcd(x: int, y: int)-> int: #최대공약수 구하는 함수
    if y==0:
        return x
    else:
        return gcd(y, x%y)
#순수한 재귀(여러번 재귀호출)
'''
하향식 분석: 위-> 아래
->같은 함수를 여러번 호출하는 경우가 있어서 반드시 효율적이라고는 할 수 없다.
상향식 분석: 아래 -> 위
-> 
'''    
def recur1(n: int)-> int:
    if n>0:
        recur1(n-1)
        print(n)
        recur1(n-2)
 
#재귀알고리즘의 비재귀적 표현
# 1. 꼬리 재귀 제거
def recur2(n: int)-> int:
    if n>0:
        recur2(n-1)
        print(n)
        n=n-2
        
# 2. 스택 사용    recur3함수는 recur1함수와 같은 결과를 출력하는 함수!
from stack import Stack   
def recur3(n: int)-> int:
    s= Stack(n)
    #n=4
    while True:
        if n>0:
            s.push(n) #스택에 4 푸시
            n=n-1# n=3이 됨-> 스택에 3,2,1이 쌓임.
            continue #다시 while문으로 돌아감
        if not s.is_empty(): #스택이 비어있지 않으면
            n=s.pop() # 
            print(n)#
            n=n-2#
            continue
        break      