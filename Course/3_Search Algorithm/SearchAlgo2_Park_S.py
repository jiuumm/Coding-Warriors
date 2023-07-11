# 백준 1920

import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())
nArr = list(map(int, input().split()))
m = int(input())
mArr = list(map(int, input().split()))

# 이진 탐색 함수 정의
def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True             # 중간 값 == 찾는 값 이면 True
        elif arr[mid] < target:
            start = mid + 1         # 중간 값 < 찾는 값이면 오른쪽 탐색 위해 범위 좁힘
        else:
            end = mid - 1           # 중간 값 > 찾는 값이면 왼쪽 탐색 위해 범위 좁힘
    return False                    # 탐색을 종료해도 찾는 값 없으면 False

# nArr 정렬
nArr.sort()

# 이진 탐색
for num in mArr:
    if binarySearch(nArr, num):
        print(1)
    else:
        print(0)
