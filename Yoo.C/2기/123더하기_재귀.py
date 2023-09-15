def go(sm, n, cnt):
    global answer
    if sm>n:
        return 
    if sm==n:
        #합이 n이 되는 순간 answer값 갱신
        answer+=1
        return

    else:
        #1,2,3더하기 
        for i in range(1,4):
            go(sm+i, n, cnt)
        
    
if __name__=='__main__':
    t= int(input())
    for _ in range(t):
        n= int(input())
        #n을 만드는게 목표!
        answer=0
        go(0,n,0)
        print(answer)
        