#230719 WED
#07-1 브루트 포스법

#실습 7-1
#브루트 포스법으로 문자열 검색하기

def bf_match(txt: str, pat: str) -> int:
    pt = 0          #txt를 따라가는 커서
    pp = 0          #pat를 따라가는 커서

    while pt != len(txt) and pp!= len(pat):
        if txt[pt] == pat[pp]:
            pt +=1
            pp +=1
        else:
            pt = pt - pp +1
            pp = 0

    return pt - pp if pp == len(pat) else -1

if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요: ')
    s2 = input('패턴을 입력하세요: ')

    idx = bf_match(s1,s2)

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{(idx +1)}번째 문자가 일치합니다.')

#멤버십 연산자 / 표준 라이브러리로 문자열 검색 가능
'''find, index계열 함수
with 계열 함수 로 구현 가능'''

#07-2 KMP법
#브루트 포스법보다 효율적

#실습 7-2
#KMP법으로 문자열 검색하기

def kmp_match(txt:str, pat: str)-> int:
    pt = 1
    pp = 0
    skip = [0] * (len(pat)+1)

    #건너뛰기 표 만들기
    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt +=1
            pp +=1
            skip[pt] = pp
        elif pp ==0:
            pt +=1
            skip[pt] ==pp
        else:
            pp = skip[pp]

    #문자열 검색하기
    pt = pp = 0
    while pt != len(txt) and pp!=len(pat):
        if txt[pt] == pat[pp]:
            pt +=1
            pp +=1
        elif pp ==0:
            pt +=1
        else:
            pp = skip[pp]

    return pt-pp if pp==len(pat) else-1

if __name__ == '__main__':
    s1 = input('텍스트 입력: ')
    s2 = input('패턴 입력: ')

    idx = kmp_match(s1,s2)

    if idx == -1:
        print('텍스트 안에 패턴이 존재를 안합니다')
    else:
        print(f'{(idx+1)}번째 문자가 일치합니다.')

#07-3 보이어 무어법
#KMP법보다 더 효율적 -> 많이 사용하는 알고리즘

#실습 7-3
#보이어 무어법으로 문자열 검색하기_문자열 길이는 0~255개

def bm_match(txt: str, pat: str) -> int:
    skip = [None]* 256          #건너뛰기 표

    #건너뛰기 표 만들기
    for pt in range(256):
        skip[pt] = len(pat)
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) -pt-1

    #검색하기
    while pt < len(txt):
        pp = len(pat) -1
        while txt[pp] == pat[pp]:
            if pp ==0:
                return pt
            pt -=1
            pp -=1
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp\
            else len(pat) -pp

    return -1

if __name__ == '__main__':
    s1 = input('텍스트 입력: ')
    s2 = input('패턴 입력: ')

    idx = bm_match(s1,s2)

    if idx == -1:
        print('텍스트 안에 패턴이 존재를 안합니다')
    else:
        print(f'{(idx+1)}번째 문자가 일치합니다.')
