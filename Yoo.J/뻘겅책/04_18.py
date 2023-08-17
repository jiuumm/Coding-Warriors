#삽입정렬 
# array=[7,5,9,0,3,1,6,2,4,8]
# for i in range(1, len(array)):
#     for j in range(i,0,-1):
#         if array[j]<array[j-1]:
#             array[j],array[j-1]= array[j-1], array[j]
#         else:
#             break
        
n= int(input())
time = list(map(int, input().split()))
for i in range(1, n):
    for j in range(i,0,-1):
        if time[j]<time[j-1]:
            time[j], time[j-1]= time[j-1], time[j]
        else:
            break
new = [0]*n
new[0]= time[0]

for i in range(1,n):
    new[i]= new[i-1]+time[i]
    
res=0
for i in range(n):
    res+=new[i]
print(res)