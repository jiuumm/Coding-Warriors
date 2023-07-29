import sys

N, M= map(int, sys.stdin.readline().split())

lst_input= [[0]*(N+1)]
lst_sum=[[0]*(N+1) for _ in range(N+1)]

for i in range(N):
    lst_input_row = [0]+ [int(x) for x in sys.stdin.readline().split()]
    lst_input.append(lst_input_row)
    
#합배열 만들기
for i in range(1,N+1):#1~N
    for j in range(1, N+1): #1~N
        lst_sum[i][j] = lst_sum[i][j-1]+lst_sum[i-1][j]-lst_sum[i-1][j-1]+lst_input[i][j]

for i in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    res = lst_sum[x2][y2]-lst_sum[x1-1][y2]-lst_sum[x2][y1-1]+lst_sum[x1-1][y1-1]
    print(res)
    