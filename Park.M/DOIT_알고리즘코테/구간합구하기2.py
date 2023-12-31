#BOOK_4
#백준 11660
#이차원 배열 구간합 구하기


import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = [[0]* (n+1)]                                                                #A : 원본 리스트 : 처음엔 요소 하나
D = [[0]* (n+1) for _ in range(n+1)]                                            #D : 합배열   -> 파이썬에서 이중 리스트를 생성하는 방법

for i in range(n):                                                              #요소를 추가하며 2차원 리스트 생성
    A_row = [0] + [int(x) for x in input().split()]                             
    A.append(A_row)

for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]                  # 2차원 배열 구간합 구하기


for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]              # [x1,y1]~[x2,y2] 구간합 구하기
    print(result)