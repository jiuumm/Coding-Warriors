n= int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#B배열은 내림차순으로 정렬
B.sort(reverse=True)

#A배열은 오름차순으로 정렬
A.sort()
res=0
for i in range(n):
    res += A[i]*B[i]

print(res)


