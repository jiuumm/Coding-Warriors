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
