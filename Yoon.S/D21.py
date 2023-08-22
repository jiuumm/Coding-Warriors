import sys
input = sys.stdin.readline
result = 0 #정답 result

def merge_sort(s, e): #시작점 s, 종료점 e
    global result #global 전역변수 선언
    if e - s < 1: return #시작점과 종료점이 같다면 멈춤
    m = int(s + (e - s) / 2) #중간점 m
    #재귀 함수 형태로 구현
    merge_sort(s, m) #시작점과 중간점
    merge_sort(m + 1, e) #(중간점 + 1)과 종료점
    #결국 병합정렬의 순서대로 함수가 작동하게 됨
    for i in range(s, e + 1): #s부터 e까지
        tmp[i] = A[i] #tmp에 저장
    k = s #정렬용 인덱스 k
    index1 = s #앞쪽 그룹 시작점
    index2 = m + 1 #뒤쪽 그룹 시작점
    while index1 <= m and index2 <= e: #두 포인터가 두 그룹의 경계선을 넘지 않을 때까지
        if tmp[index1] > tmp[index2]: #앞쪽 그룹 원소가 뒤쪽 그룹 원소보다 크면
            A[k] = tmp[index2]
            result = result + index2 - k #앞으로 이동한 거리만큼 더함
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

N = int(input()) #리스트의 개수 N
A = list(map(int, input().split())) #리스트 A
A.insert(0, 0) #(N + 1)
tmp = [0] * int(N + 1) #저장용 리스트 tmp
merge_sort(1, N) #시작점 1, 종료점 N으로 함수 호출
print(result)
