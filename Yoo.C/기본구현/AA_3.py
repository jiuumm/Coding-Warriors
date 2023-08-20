'''
* 입력
N: N장의 카드 존재(1~100중 하나, 중복허용)
여기서 3장을 뽑았을 때 가능한 모든 경우 기록
K: K번째로 큰 수 출력
ex) N:10, K=3
13 15 34 23 45 65 33 11 26 42
이 중 3장을 뽑았을 때 가능한 모든 경우

[알고리즘 절차]
1. n개의 수를 가진 리스트에서 중복 제거
11 13 15 23 26 33 34 42 45 65
2. 이 중 3개씩 묶는다.
가능한 조합의 수: 10C3-> 120가지
3. K번째 큰 값
뒤에서 3번째
'''

n, k = map(int, input().split())
#n개의 수를 모두 받기
lst=list(map(int, input().split()))
#set(): 중복을 제거함-
#미리 중복을 제거하는 set자료구조형 res를 선언
res=set()

for i in range(n):
     for j in range(i+1, n):
          for m in range(j+1,n):
               res.add(lst[i]+lst[j]+lst[m])

#res를 set형 자료구조로, sort를 사용하려면
#리스트로 바꿔줘야 함!
res=list(res)
res.sort(reverse=True)
print(res[k-1])

    
    

   
    
    
    
    