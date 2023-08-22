n=int(input()) #수열의 개수
arr = [0]*n
stack=[]
for i in range(n):
    arr[i]=int(input())

now=1
res=""
flag=True

for i in range(n):
    if arr[i]>=now:
        while arr[i]>=now:
            stack.append(now)
            now+=1
            res+="+\n"
        stack.pop()
        res+="-\n"
    else:
        num= stack.pop()
        
        if num>arr[i]:
            print("NO")
            flag=False
            break
        else:
            res+="-\n"
if flag==True:
    print(res)
            
   
