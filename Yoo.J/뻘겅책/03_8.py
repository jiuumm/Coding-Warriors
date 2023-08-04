import sys
input= sys.stdin.readline

S, P = map(int, input().split())
dna_lst = list(input())
tmp = list(map(int, input().split()))
dic = {'A': tmp[0], 'C': tmp[1], 'G': tmp[2], 'T': tmp[3]}
check = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

cnt = 0
for i in range(S-P+1):
    boool = True

    if i == 0:
        for j in range(P):
            check[dna_lst[j]] += 1
    else:
        check[dna_lst[i+P-1]] += 1
        check[dna_lst[i-1]] -= 1

    for i in ('A', 'C', 'G', 'T'):
        if check[i] < dic[i]:
            boool = False
            break

    if boool:
        cnt += 1

print(cnt)