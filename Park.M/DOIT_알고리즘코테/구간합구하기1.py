#BOOK_3
#백준 11659



import sys                                                          #입력속도를 개선하기 위한 표준 입출력 관련 코드 -> input() 대체
input = sys.stdin.readline                                          #입력함수 재정의 : input()함수 호출시 sys.stdin.readline()함수 호출됨
                                                                                    # input() : 한 줄을 입력받아 문자열로 변환 -> 입력이 큰 경우 slow
                                                                                    # sys.stdin.readline : 개행문자 포함 한 줄 읽어옴

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
sum =[0]                                                            #값이 0인 하나의 요소를 가진 리스트 생성
tmp = 0

for i in numbers:
    temp = temp+i
    sum.append(temp)                                                #합배열

for i in range(M):
    s, e = map(int, input.split())
    print(sum[e] - sum[s-1])                                        #구간합