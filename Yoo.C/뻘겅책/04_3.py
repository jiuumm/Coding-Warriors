import sys
print = sys.stdout.write
lst = list(input())

for i in range(len(lst)):
    MaxIdx = i
    for j in range(i+1, len(lst)):
        if lst[j]>lst[MaxIdx]:
            MaxIdx= j
        if lst[i]<lst[MaxIdx]:
            tmp = lst[i]
            lst[i]= lst[MaxIdx]
            lst[MaxIdx]= tmp
            
for j in range(len(lst)):
    print(lst[j])