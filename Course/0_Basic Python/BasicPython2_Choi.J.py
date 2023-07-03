#1498번
n, g = map(int, input().split())
data = list(map(int, input().split()))

result = []
for i in range(0, n, g):
    group = data[i:i+g]
    min_value = min(group)
    result.append(min_value)

for value in result:
    print(value, end=' ')
