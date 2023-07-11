'''
test_lst에 있는 수들이 search_lst안에 있으면
1을 출력, 아니면 0을 출력!

###시간초과 !!!->해결하기
'''
import sys
sys.stdin = open("in2.txt", "rt")
N=int(input())
search_lst = list(map(int, input().split()))

M= int(input())
test_lst = list(map(int, input().split()))
#elem: test_lst[i]
def check(elem):
    search_lst.sort()

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
