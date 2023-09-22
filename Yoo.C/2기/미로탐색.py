def dfs(board, visited, n, m,x,y):
    nx, ny = 0, 0
    visited[x][y]=True
    if x==n-1 and y== m-1:
        return
    #if 0<=x<n and 0<=y<m and not visited[x][y] and board[x][y+1]=='1' and board[x+1][y]=='1':
        #nx=x
        #ny=y+1
        #dfs(board, visited, n, m, nx, ny)
    if 0<=x<=n-2 and 0<=y<=m-2 and board[x][y+1]=='1' and board[x+1][y]=='0':
        nx=x
        ny=y+1
        dfs(board, visited, n, m, nx, ny)
    elif 0<=x<=n-2 and 0<=y<=m-2 and  board[x][y+1]=='0' and board[x+1][y]=='1':
        nx=x+1
        ny=y
        dfs(board, visited, n, m, nx, ny)
    elif 0<=x<=n-2 and 0<=y<=m-2 and  board[x][y+1]=='1' and board[x+1][y]=='1':
        nx=x+1
        ny=y
        dfs(board, visited, n, m, nx, ny)
    #가장 마지막 행에 있을 때
    elif x==n-1 and 0<=y<m and board[x][y+1]=='1'and board[x-1][y]=='0':
        nx=x
        ny=y+1
    elif x==n-1 and 0<=y<m and board[x][y+1]=='0' and board[x-1][y]=='1':
        nx=x-1
        ny=y
        

if __name__=='__main__':
    #n:행, m:열
    n, m= map(int, input().split())
    board=[]
    for i in range(n):
        board.append(input())
    visited=[[False]*m for _ in range(n)]
    cnt=0
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue
            else:
                dfs(board, visited, n, m,0,0)
                cnt+=1
                
    print(cnt)