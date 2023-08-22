a=[31,39,29,28,58,68,70,95,5]
lt=0
rt=len(a)-1

a.sort()

key=100
while lt<=rt:
    mid=(lt+rt)//2
    if a[mid]<key:
        lt=mid+1
    elif a[mid]>key:
        rt=mid-1
    else:
        print("탐색 성공! 종료합니다..")
        break
if a[mid] !=key:
    print("탐색 실패! 해당 key값을 리스트에 없습니다..")