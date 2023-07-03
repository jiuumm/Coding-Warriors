n=int(input("100 보다 작은 정수:"))
for i in range(1,n+1):
  x=i//10
  y=i%10
  if y==3 or y==6 or y==9:
    if x==3 or x==6 or x==9:
       print("XX", end=' ')
    else:
       print("X", end=' ')
  else:
    print(i, end=' ')
