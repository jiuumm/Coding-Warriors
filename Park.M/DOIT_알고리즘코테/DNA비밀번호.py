#BOOK_9
#백준 12891
#슬라이딩 윈도우 알고리즘 : 시간복잡도 O(n)


#전역변수 선언
checkList = [0]*4
myList = [0]*4
checkSecret = 0                                                 #몇 개의 문자와 관련된 개수를 충족했는지 판단하는 변수

#함수정의
def myadd(c):                                                   #새로 들어온 문자를 처리하는 함수
    global checkList, myList, checkSecret                       
            #함수 내에서 전역변수의 값을 변경하려고 하면 global 키워드를 사용하여 변수가 전역변수임을 명시해야함 
    if c=='A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c=='C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c=='G':
        myList[2]+=1
        if myList[2]==checkList[2]:
            checkSecret += 1
    elif c=='T':
        myList[3]+=1
        if myList[3] == checkList[3]:
            checkSecret += 1

def myremove(c):                                                #제거되는 문자를 처리하는 함수
    global checkList, myList, checkSecret
    if c=='A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret-=1
        myList[2]-=1
    elif c=='T':
        if myList[3]==checkList[3]:
            checkSecret -=1
        myList[3]-=1

S, P = map(int, input().split())
Result = 0
A = list(input())
checkList = list(map(int, input().split()))

for i in range(4):                                              
    if checkList[i] == 0:
        checkSecret +=1

for i in range(P):                                              #초기 P부분
    myadd(A[i])

if checkSecret == 4:                                            #초기 P부분에서 관련 크기 모두 충족될 때 유효한 비밀번호
    Result += 1

for i in range(P, S):                                           #윈도우가 옮겨가면서 추가, 삭제되는 값 업데이트
    j = i-P                                                     #추가되는 값이 A[i], 삭제되는 값이 A[j]
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        Result += 1

print(Result)