'''
1. 입력
2 2 2(빛의 가짓수)-> 0~1까지 두가지 색이 있다.

2. 출력
0 0 0
0 0 1
0 1 0
0 1 1
1 0 1
1 1 0
1 1 1
8(개수 출력)
'''

r,g,b=map(int, input().split())
count=0

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j,k)
            count+=1
print(count)
        
    
