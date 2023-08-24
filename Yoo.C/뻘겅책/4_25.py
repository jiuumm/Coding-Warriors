from collections import deque
n, m, start = map(int, input().split())
A = [[] for _ in range(n+1)]

for _ in range(m):
    s,e  = map(int, input().split())
    A[s].append(e)
    A[e].append(s)
    
for i in range(n+1):
    A[i].sort()

def DFS(x):
    print(x, end = ' ')
    visited[x]=True
    for i in A[x]:
        if not visited[x]:
            DFS(i)
            
visited = [False]*(n+1)
DFS(start)

def BFS(x):
    queue = deque()
    queue.append(x)
    visited[x] = True
    while queue:
        nNode = queue.popleft()
        print(nNode, end = ' ')
        for i in A[nNode]:
            if not visited[i]:
                visited[i]= True
                queue.append(i)


print()
visited = [False]*(n+1)
BFS(start)
