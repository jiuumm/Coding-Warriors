# 이분탐색할 기준: 총 소요 시간
def solution(n, times): # 사람 수 n, 심사관 당 소요 시간 배열 times
    # 최솟값 l, 최댓값 r
    l = 1
    r = max(times) * n # 최대 소요 시간
    
    while l <= r :
        m = (l + r) // 2 # 가운데 m
        ok = 0 # 심사완료 사람 수 ok
     	
        for time in times :
            ok += m // time
            if ok >= n :
                break
        
        if ok >= n : # 크거나 같을 때
            answer = m
            r = m - 1
        else : # 작을 때
            l = m + 1
    
    return answer
