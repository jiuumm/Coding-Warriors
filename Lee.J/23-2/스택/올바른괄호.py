def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    stack=[]
    for i in s:
        if i=='(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
                
    if stack:
        return False
    else:
        return True

    