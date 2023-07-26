#과목 개수
N= int(input())
scores = list(map(int, input().split()))

#최댓값 구하기
max = scores[0]
for i in range(1, N):
    if max<scores[i]:
        max= scores[i]
sum=0
for i in scores:
    i = i/max*100
    sum+=i


res = sum/N
print(res)