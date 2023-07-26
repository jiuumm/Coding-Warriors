N = int(input())                      #숫자의 개수

# 파이썬에서 input()함수는 항상 문자열을 반환함

# x = [None]*N
#               -> 이 부분은 필요없음 : 파이썬은 동적으로 타입 지원 -> 변수의 타입을 직접 명시안해도 됨
#                                    --> 미리 배열 선언 불필요

numbers = input()                     #N개의 숫자들을 공백없이 입력받는다

sum = 0
                                     #공백 없이 주어진 N개의 숫자
for i in numbers:                    #여기서 range(N) X -> 기본적 로직은 같지만 반복 방식이 다름
    sum += int(i)                    #range(N): 문자열을 인덱스로 접근 /in numbers: 문자열 자체 반복하며 문자 하나씩 가져옴         

print(sum)