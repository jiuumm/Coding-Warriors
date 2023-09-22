def solution(s):
    cnt1 = 0
    cnt2 = 0

    for i in range(len(s)):
        if s[i] == "(":
            cnt1 += 1
        elif s[i] == ")":
            cnt2 += 1

        if cnt1 < cnt2:
            return False

    return cnt1 == cnt2