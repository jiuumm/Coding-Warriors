import sys
<<<<<<< HEAD
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
=======
sys.stdin = open("input.txt", "r")
n= int(input())
input= sys.stdin.readline
lst = list(map(int, input().split()))
lst.sort()
res=0
for i in range(n):
    lt=0
    rt=n-1
    cnt=0
    #목표값: lst[i]
    while lt<rt:
        if lst[lt]+lst[rt]<lst[i]:
            lt+=1
        elif lst[lt]+lst[rt]>lst[i]:
            rt-=1
        else:
            #값이 같을 때
            if lt != i and rt != i:
                cnt+=1
                break
            elif lt==i:
                lt+=1
                
            elif rt==i:
                rt-=1
                
    res += cnt       
print(res)
>>>>>>> f1303b936392b292854e5d9f0d9047a7b48bf7b5
