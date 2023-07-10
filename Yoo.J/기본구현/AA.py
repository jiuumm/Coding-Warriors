
N= int(input())
word=[]
for i in range(N):
    tmp = input()
    tmp=tmp.lower()
    word.append(tmp)


#k는 배열 안에 있는 문자열
def check(k):
    
    if k==k[::-1]:

        return True
    else:
        return False
        


for i in range(N):
    if check(word[i])==True:
        print("#",i+1, sep='', end=' ')
        print("YES")
    else:
        print("#",i+1, sep='', end=' ' )
        print("NO")


n=int(input())
for i in range(n):
    s=input()
    s=s.upper()
    size=len(s)
    for j in range(size//2):
        if s[j]!= s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))
        
        