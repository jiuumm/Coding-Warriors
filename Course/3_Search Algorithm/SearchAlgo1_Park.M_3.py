K, N = map(int, input().split())

li = []
for _ in range(K):
    li.append(int(input()))

li.sort()

pl, pr = 1, sum(li) // N
ans = 0

while pl <= pr:
    pc = (pl + pr) // 2
    count = sum(word // pc for word in li)
    if count >= N:
        ans = pc
        pl = pc + 1
    else:
        pr = pc - 1

print(ans)
