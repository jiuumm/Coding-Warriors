#230727(THU)
#002. 평균 구하기 (백준 브론즈1 1546번)

N = int(input())
myList = list(map(int,input().split())) #점수정보 저장
myMax = max(myList)                     #최댓값 저장
sum = sum(myList)              #아래 수식으로 한번에 계산 가능
print(sum*100/myMax/int(N))
