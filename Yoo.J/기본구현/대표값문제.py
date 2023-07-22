
#4-대표값 문제
import sys
sys.stdin = open("in2.txt", "rt")
N= int(input())
a = list(map(int, input().split()))

avr=0

    
#전체 학생 평균(소수 첫번째 자리에서 반올림)

avr = round(sum(a)/N)

min=2147000000
for idx, x in enumerate(a):
    #temp= 편차
    #abs()함수: 절댓값 함수!
    temp = abs(x-avr)
    if temp<min:
        min=temp
        score=x
        res=idx+1
    #같은 거리의 성적이 존재하면
    #점수가 높은 사람이 정답
    elif temp==min:
        if x>score:
            score=x
            res= idx+1
print(avr, res)