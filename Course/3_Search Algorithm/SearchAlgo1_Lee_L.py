#입국심사
def solution(n, times):
    answer = 0
    pl= 1
    pr=max(times)*n
    while pl<=pr:
        pc=(pl+pr)//2
        people=0
        for time in times:
            people+=pc//time
        if people>=n:
            answer=pc
            pr=pc-1
        else: 
            pl=pc+1

    return answer