#230729(SAT)
#004. 구간 합 구하기2(백준 실버1 11660번)

#답을 구하는 '공식'을 먼저 도출해내기
#D[X2][Y2]-D[X1-1][Y2]-D[X2][Y1-1]+D[X1-1][Y1-1]

'''n:리스트크기 / m:질의 수
   A:원본 리스트 / D:합 배열'''
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
A = [[0] * (n+1)]                       #입력받은 n으로 A배열 초기화
D = [[0] *(n+1) for _ in range(n+1)]    #입력받은 n으로 D배열 초기화

for i in range(n):
    ARow = [0] + [int(x) for x in input().split()]
    A.append(ARow)                      #A배열 저장, 각 행 앞에 0추가

for i in range(1,n+1):
    for j in range(1,n+1):
        #합배열 구하기
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

for _ in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    #구간 합배열로 질의에 답변
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)

