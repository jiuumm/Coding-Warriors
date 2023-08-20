# 코드업 #6096

'''
1. 격자판
세로: h(행)
가로: W(열)

2. 막대
막대개수: n
막대 길이: l
막대 놓는 방향: d(가로: 0, 세로: 1)
막대를 놓는 막대의 가장 왼쪽 or위쪽 위치:(x,y)
-> x: 행 , y: 열

3. 입력
첫 줄: h, w
두번째 줄: n(막대개수)
세번째줄: l(막대 길이),d(막대 놓는 방향가로:0, 세로:1
), (x,y)

4. 출력
모든 막대를 놓는 격자판의 상태
막대로 가려진 경우:1

'''
#sol
#입력 받기
h,w= map(int, input().split())
n = int(input())
#처음에 오류난 이유
'''
어이없게도 h와 w의 자리를 바꿔 썼다..
'''
#격자판 만들기
arr=[]
for i in range(w):
    lst = []
    for j in range(h):
        lst.append(0)
    arr.append(lst)  

#입력 받기(n: 막대 개수)    
for i in range(n):
    l,d,x,y=map(int, input().split())


    
    #분류기준: d=0 or 1
    #막대를 가로방향으로 놓을 때
    if d==0:
        for j in range(l):
            arr[x-1][y-1]=1
            y+=1
    #막대를 세로방향으로 놓을 때
    elif d==1:
        for j in range(l):
            arr[x-1][y-1]=1
            x+=1
  
       

for i in range(h):
    for j in range(w):
        print(arr[i][j], end=' ')

    print()        
    