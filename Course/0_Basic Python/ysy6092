#번호를 부른 숫자와 부른 번호 입력받기
n = int(input())
a = input().split() #부른 번호 리스트에 입력하기

#int로 형변환하기
for i in range(n) :
    a[i] = int(a[i])

d = list()
for i in range(24) :
    d.append(0) #기본으로 값 0 할당하기

for i in range(n) :
    d[a[i]] += 1 #불릴 때마다 +1하기

for i in range(1, 24) :
    print(d[i], end = ' ') #공백으로 구분해서 출력하기
