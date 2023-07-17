'''
코드업 #6096
1. 입력
-19*19 크기의 정수값
-십자 뒤집기 횟수: n
-> n만큼 입력됨
ex)
정수값 리스트 입력
2
10 10 #(9,9)위치 제외하고 (다시 돌아오니깐)9행의 모든 바둑돌을 반대

12 12 #(11,11)위치 제외하고(다시 돌아오니깐) 11열 모든 바둑돌을 반대


'''
#19*19 바둑판 만들기
arr=[]
for i in range(19):
    arr.append(list(map(int, input().split())))

#십자 뒤집기 횟수=n
n= int(input())

#십자 뒤집기 횟수만큼 반복
for i in range(n):
    a,b=map(int, input().split())
    # arr[a-1][x]의 바둑돌을 모두 반대로 뒤집는다.
    #즉 , 행 고정
    for j in range(19):#j: 0~18
        if arr[a-1][j]==0:
            arr[a-1][j]=1

        else:
            arr[a-1][j]=0

   #arr[x][b-1]의 바둑돌을 모두 반대로 뒤집는다.
   #즉, 열 고정
    for j in range(19):
        if arr[j][b-1]==0:
            arr[j][b-1]=1

        else:
            arr[j][b-1]=0

        
for i in range(19):
    for j in range(19):
        print(arr[i][j], end=' ')
    print()    
        