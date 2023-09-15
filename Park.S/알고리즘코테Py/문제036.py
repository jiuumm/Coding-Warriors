#230826(SAT)
#036.최솟값을 만드는 괄호배치 찾기(백준 실버2 1541번)

answer = 0
A = list(map(str, input().split("-")))

def mySum(i):
    sum = 0
    temp = str(i).split("+")
    for i in temp:
        sum += int(i)
    return sum

for i in range(len(A)):
    temp = mySum(A[i])
    if i == 0:
        answer += temp
    else:
        answer -= temp

print(answer)