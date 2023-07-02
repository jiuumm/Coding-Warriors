#코드업 1408번
s = input()

for i in range(len(s)):
    print(chr(ord(s[i])+2), end='')
print()    
for i in range(len(s)):
    print(chr(ord(s[i])*7%80+48), end='')    