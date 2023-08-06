'''
백준#1920
test_lst에 있는 수들이 search_lst안에 있으면
1을 출력, 아니면 0을 출력!

###시간초과 !!!->해결하기->완료!
check 함수안에 sort()메서드를 넣었더니 시간초과가 발생했다.
아무래도 for문을 돌때마다 sort를 하니깐 시간이 오래걸렸던 것 같다.
'''
import sys
sys.stdin = open("in2.txt", "rt")
N=int(input())
search_lst = list(map(int, input().split()))

M= int(input())
test_lst = list(map(int, input().split()))
#elem: test_lst[i]
search_lst.sort()
def check(elem):
    

    lt = 0
    rt = N-1
   
    # 목표값: elem
    while lt<=rt:
        mid =(lt+rt)//2
        if elem == search_lst[mid]:
            print(1)
            break
        elif elem<search_lst[mid]:
            rt=mid-1
        elif elem>search_lst[mid]:
            lt = mid+1
            
    if elem != search_lst[mid]:
        
        print(0)        


for i in range(M):
    check(test_lst[i])
