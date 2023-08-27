#BOOK_23
#백준 11724



import sys
sys.setrecursionlimit(10000)                                    # setrecursionlimit() : 재귀 호출의 최대 깊이 제한 설정
input = sys.stdin.readline                                      #n: 노드개수, m: 에지개수
n, m = map(int, input().split())
A = [[]for _ in range(n+1)]
visited = [False] * (n+1)                                       #방문리스트

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)                                              #양방향 에지이므로 양쪽에 에지를 더함
    A[e].append(s)


count = 0

for i in range(1, n+1):                                         #연결 노드 중 방문하지 않았던 노드만 탐색
    if not visited[i]:
        count+=1
        DFS(i)

print(count)