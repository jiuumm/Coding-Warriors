'''
test_lst에 있는 수들이 search_lst안에 있으면
1을 출력, 아니면 0을 출력!
'''

N=int(input())
search_lst = list(map(int, input().split()))

M= int(input())
test_lst = list(map(int, input().split()))
    

search_lst.sort()
for i in test_lst:
    
    lt = 0
    rt = N-1
   
    # 목표값: i
    while lt<=rt:
        mid =(lt+rt)//2
        if i == search_lst[mid]:
            print(1)
            break
        elif i<search_lst[mid]:
            rt=mid-1
        elif i>search_lst[mid]:
            lt = mid+1
            
    if i != search_lst[mid]:
        
        print(0)      