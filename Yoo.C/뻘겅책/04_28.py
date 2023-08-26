import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(x, y):
    
    for a, b in graph[x]:

        if visited[a] == -1:
            visited[a] = b + y 
            dfs(a, b + y) 


v = int(input())

graph = [[] for _ in range(v + 1)]
for _ in range(v):
    x = list(map(int, input().split()))
    for j in range(1, len(x) - 2, 2):
        graph[x[0]].append([x[j], x[j + 1]])


visited = [-1] * (v + 1)
visited[1] = 0
dfs(1, 0) 

start = visited.index(max(visited)) 
visited = [-1] * (v + 1)
visited[start] = 0
dfs(start, 0) 

print(max(visited))