
def DFS(x):
    if x>0:
        DFS(x-1)
        print(x, end = ' ')

#실행되면 main부터 실행된다.
if __name__=="__main__":
    n= int(input())
    DFS(n)
    