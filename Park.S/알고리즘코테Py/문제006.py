#230731(WED)
#006. 연속된 자연수의 합 구하기(백준 실버5 2018번)
#투 포인터 : 2개의 포인터로 알고리즘 시간복잡도 최적화

N = int(input())
count = 1       #N 자기자신도 정답 케이스에 포함
startIndex = 1
endIndex = 1
sum = 1

while endIndex != N:
    if sum == N:    #정답 케이스
        count += 1
        endIndex +=1
        sum += endIndex
    elif sum > N:
        sum -= startIndex
        startIndex +=1
    else:
        endIndex += 1
        sum += endIndex

print(count)