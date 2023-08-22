#DFS1함수로 실행하면 1101이 출력됨.
def DFS1(x):
    if x==0:
        return
    #함수에서 return하면 종료시켜라는 의미이기도 하다.
    else:
        print(x%2, end=" ")
        DFS1(x//2)

#DFS2함수로 실행하면 1011이 출력됨
def DFS2(x):
    if x==0:
        return
    #함수에서 return하면 종료시켜라는 의미이기도 하다.
    else:
        DFS1(x//2)
        print(x%2, end=" ")
        

#실행되면 main부터 실행된다.
if __name__=="__main__":
    n= int(input())
    DFS1(n)
    print()
    DFS2(n)
    