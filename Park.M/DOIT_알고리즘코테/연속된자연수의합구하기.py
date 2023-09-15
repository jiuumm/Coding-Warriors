#BOOK_6
#백준 2018
#투 포인터


n = int(input())
count = 1                                                           #모든 변수의 값을 1로 초기화하는 이유: n자체인 경우는 자동으로 포함되기 때문
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    if sum == n:
        count += 1
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index

print(count)