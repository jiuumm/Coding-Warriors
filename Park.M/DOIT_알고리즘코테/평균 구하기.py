#BOOK_2
#백준 1546



N = int(input())                                            #시험 본 과목의 개수 N
scorelist = list(map(int, input().split()))                 #성적 저장하는 리스트
M = max(scorelist)                                          #점수의 최댓값 M
sum = sum(scorelist)                                        #점수의 합 sum

# 새로운 점수 : 점수/M*100
# 새로운 점수들의 평균 : (점수1+점수2+점수3)*100/M/점수개수
#                     (점수 합)*100/M/점수개수

print((sum*100)/M/N)


# function : list()   -> 다른 iterable 객체를 리스트로 변환
# function : map()    -> 주어진 함수를 iterable 객체의 모든 요소에 적용하여 새로운 iterator를 반환