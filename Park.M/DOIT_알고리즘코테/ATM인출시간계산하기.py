N = int(input())                                        #데이터 개수

A = list(map(int, input().split()))                     #리스트 생성_걸리는 시간 입력
S = [0]*N                                               #합배열 생성

for i in range(1, N):                                   #삽입 정렬
    insert_point = i
    insert_val0ue = A[i]
    for j in range(i-1, -1, -1):
        if A[j] < A[i]:
            insert_point = j+1
            break
        if j == 0:
            insert_point = 0
    for j in range(i, insert_point, -1):
        A[j] = A[j-1]
    A[insert_point] = insert_value

S[0] = A[0]                                             #A리스트의 첫번째 원소를 누적 합 배열의 첫번째 원소로 초기화하기 위함. A리스트의 첫번째 원소를 누적 합 배열의 첫 번째 원소로 사용하기 위함

for i in range(1, N):                                   #합배열 만들기
    S[i] = S[i-1] + A[i]

sum = 0

for i in range(0, N):                                   #합 배열 총합
    sum += S[i]

print(sum)