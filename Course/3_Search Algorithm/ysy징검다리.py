# 이분탐색할 기준: 바위를 제거할 거리 기준
def solution(distance, rocks, n):
    # 최솟값 l, 최댓값 r
    l = 1
    r = distance # 최대 거리
    rocks.sort(); # 오름차순 정렬
    
    while l <= r :
        # 중앙값 m, 제거한 바위 수 removed, 이전 바위 위치 previous
        m = (l + r) // 2
        removed = 0
        previous = 0 # 출발지점부터
        
        for rock in rocks + [distance] :
            dis = rock - previous
            
            if dis < m : # 기준보다 낮다면
                removed += 1 # 바위 제거
                if removed > n: # 제거 개수가 n보다 크면
                    break
            else : # 기준과 일치하거나 높다면
                previous = rock
        
        if removed > n: # 제거 개수가 n보다 크므로 기준이 너무 높음
            r = m - 1
        else:
            answer = m # 제거 개수가 n보다 작거나 같으므로 기준이 너무 낮거나 적정함
            l = m + 1
    
    return answer
