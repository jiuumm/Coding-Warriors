#BOOK_26
#백준 1260


                                                                # A와 visited의 크기가 모두 N이 아니라 N+1인 이유는 파이썬의 인덱스는 시작이 0부터 인데 그래프의 노드 번호는 1부터 시작이므로 노드번호와 리스트 인덱스를 서로 맞추기 위해서
from collections import deque                                   # BFS는 큐를 사용함: 이는 덱을 통해 구현하므로
N, M, Start = map(int, input().split())                         # N: 노드수, M: 에지수, Start: 시작점
A = [[] for _ in range(N+1)]                                    # A: 그래프의 데이터를 저장하는 인접 리스트 

for _ in range(M):                                              # 인접 리스트에 데이터 저장
    s, e = map(int, input().split())
    A[s].append(e)                                              # 에지가 양방향이므로 양쪽에 에지를 더함
    A[e].append(s)

for i in range(N+1):                                            # '노드가 여러 개일 경우 노드 번호가 작은 것을 먼저 방문'
    A[i].sort()                                                 # 따라서 오름차순으로 정렬

def DFS(v):
    print(v, end=' ')                                           # 현재 노드 출력
    visited[v] = True                                           # 방문 리스트 업뎃
    for i in A[v]:                                              # 방문하지 않은 노드 DFS
        if not visited[i]:
            DFS(i)

visited = [False]*(N+1)                                         # 방문 리스트 초기화
DFS(Start)                                                      

def BFS(v):
    queue = deque()
    queue.append(v)                                             # 현재 노드 저장
    visited[v] = True                                           # 방문 리스트 업뎃
    while queue:                                                # 큐가 비어있지 않을 때
        now_Node = queue.popleft()                              # 현재 
        print(now_Node, end=' ')                                # 가져온 노드 출력
        for i in A[now_Node]:                                   # 현재 노드의 연결 노드들
            if not visited[i]:                                  # 미방문 노드            
                visited[i] = True                               # 방문 리스트 업뎃
                queue.append(i)                                 # 큐에 삽입

print()
visited = [False]*(N+1)                                         # 방문 리스트 초기화
BFS(Start)