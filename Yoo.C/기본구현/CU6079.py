
'''
1. 입력
 정수 n
 
2. 출력
10
-> 1+2+...+10(합)>=55
*while문->자바와 파이썬의 차이점 알아두기
'''
n= int(input())
sum=0
count=0
while sum<n:
    sum+=(count+1)
    count+=1
    if(sum>=n):
        break
print(count)