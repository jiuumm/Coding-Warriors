#병합 정렬 알고리즘 구현하기

from typing import MutableSequence

def merge_sort(a: MutableSequence)-> None:
    """병합 정렬"""
    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        """a[left] ~ a[right]를 재귀적으로 병합 정렬"""
        if left < right:
            center = (left + right) //2

            _merge_sort(a, left, center)                      #배열 앞부분 병합정렬
            _merge_sort(a, center+1, right)                   #배열 뒷부분 병합정렬

            p = j = 0                                         #앞부분과 뒷부분 병합과정
            i = k = left

            while i <= center:                                # left <= center
                buff[p] = a[i]                                # buff의 커서: p, 배열의 앞부분 커서: i
                p += 1                                        # 배열의 앞부분을 buff에 똑같이 옮긴다
                i += 1

            while i <= right and j<p:                         # 배열의 뒷부분과 앞부분을 비교한다
                if buff[j] <= a[i]:                           # 정렬된 뒷부분과 앞부분을 앞에서 부터 비교한다 -> 뒷부분 첫번째/앞부분 첫번째 원소부터 go
                    a[k] = buff[j]                            # 비교한 결과를 작은 순서대로 배열에 저장한다
                    j+=1
                else:
                    a[k] = a[i]
                    i+= 1
                k += 1

            while j < p:                                      # 남은 나머지 원소를 배열에 복사
                a[k] = buff[j]
                k += 1
                j += 1

    n = len(a)
    buff = [None]*n                                               #작업용 배열 생성
    _merge_sort(a, 0, n-1)                                        #배열 전체 병합 정렬
    del buff                                                      #작업용 배열 소멸

if __name__ == '__main__':
    print('병합 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요: '))
    x = [None]*num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    merge_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')