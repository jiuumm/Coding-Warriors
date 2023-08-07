#230804(FRI)
#009. DNA 비밀번호(백준 실버5 12891번)

#슬라이딩 윈도우 : 포인터 2개로 범위 지정->범위 유지한 채로 이동
'''슈도코드
#전역변수 선언
checkList(비밀번호 체크리스트)
myList(현재 상태 리스트)
checkSecret(몇 개의 문자와 관련된 개수를 충족했는지 판단하는 변수)

#함수 선언
myadd(문자 더하기 함수):
    myList에 새로운 값을 더하고 조건에 따라 checkSecret값 업데이트
myremove(문자 빼기 함수):
    myList에 새로운 값을 제거하고 조건에 따라 checkSecret값 업데이트

#메인 코드
S : 문자열 크기
P : 부분 문자열 크기
A : 문자열 데이터
checkList 데이터 받기
checkList 탐색하여 값이 0인 데이터 개수만큼 checkSecret 값 증가
#값이 0 == 비밀번호 개수 조건 이미 충족
P 범위 (0 ~ P-1) 만큼 myList 및 checkSecret에 적용 후, 유효 비밀번호인지 판단

for ~
print~

기존 검사 결과에 새로들어온/제거되는 문자열만 반영해 확인하는 게 핵심!
'''

checkList = [0] *4
myList = [0] *4
checkSecret = 0

def myadd(c):
    global checkList, myList, checkSecret
    if c =='A':
        myList[0] +=1
        if myList[0] == checkList[0]:
            checkSecret +=1
    elif c == 'C':
        myList[1] +=1
        if myList[1] == checkList[1]:
            checkSecret +=1
    elif c =='G':
        myList[2] +=1
        if myList[2] == checkList[2]:
            checkSecret +=1
    elif c =='T':
        myList[3] +=1
        if myList[3] == checkList[3]:
            checkSecret +=1

def myremove(c):
    global checkList, myList, checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -=1
        myList[0] -=1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -=1
        myList[1] -=1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -=1
        myList[2] -=1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -=1
        myList[3] -=1

S, P = map(int,input().split())
result = 0
A = list(input())
checkList = list(map(int, input().split()))

for i in range(4):
    if checkList[i] ==0:
        checkSecret +=1

for i in range(P):
    myadd(A[i])

if checkSecret ==4:
    result +=1

for i in range(P,S):
    j = i-P
    myadd(A[i])
    myremove(A[j])
    if checkSecret ==4:
        result += 1

print(result)