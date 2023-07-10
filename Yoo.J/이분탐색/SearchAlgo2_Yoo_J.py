

N= int(input())
s_card = list(map(int, input().split())) 
M= int(input())
test_card = list(map(int, input().split()))

def check(arr):
    #arr: s_card(상근이 카드)
    #일단 들어온 리스트 오름차순 정리
    arr.sort()
    

    #test_card의 크기만큼 반복

    for i in range(len(test_card)):
        lt=0
        rt=len(arr)-1
        #목표값: arr의 i번째 원소
        goal = test_card[i]
        
        while lt<=rt:
            mid=(lt+rt)//2
            if s_card[mid]==goal:
                print(1, end=' ')
                break
            elif s_card[mid]<goal:
                lt=mid+1
                
            else:
                rt=mid-1
        
        if s_card[mid] !=goal:
            print(0, end=' ')
                
                
#목표: 상근이 카드를 탐색할 것이다.        
check(s_card)