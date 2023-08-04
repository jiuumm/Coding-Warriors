'''
*투포인터 문제
특정한 합을 가지는 부분 연속 수열 찾기
완전 탐색을 이용하면 O(n^2)이 나오게 되어 안됨
목표: O(n)
'''

N= int(input())
lst_N= []
for i in range(N):
    lst_N.append(i+1)

lt=0
rt=1
sum=lst_N[0]
cnt=0
while True:
    if sum<N:#N=6
        if rt<N:
            sum+=lst_N[rt]
            rt+=1
        else:
            break

    
    elif sum==N:
        cnt+=1
        sum-=lst_N[lt]
        lt+=1
    else:
        sum-=lst_N[lt]
        lt+=1
print(cnt)
    