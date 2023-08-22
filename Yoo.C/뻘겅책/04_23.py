import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def DFS(x):
    visited[x]= True
    for i in A[x]:#연결된 노드들 싹다 확인
        if not visited[i]:#만약 방문 안했다면
            DFS(i)#재귀호출
        
        


if __name__=='__main__':
    v, e = map(int, input().split())
    visited = [False]*(v+1)
    A=[[] for _ in range(v+1)] #vertex개수+1만큼 연결리스트
    for _ in range(e):
        n,m = map(int, input().split())
        A[n].append(m)
        A[m].append(n)
    
    cnt=0
    for i in range(1, v+1):#1~v까지 탐색
        if not visited[i]:
            cnt+=1
            DFS(i)
    print(cnt)
            
            