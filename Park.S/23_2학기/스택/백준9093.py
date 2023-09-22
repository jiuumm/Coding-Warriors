#230921(THUR) / 스택 / 백준9093(브론즈1)
#문자열리스트를 차례로 push하고 pop하며 출력

''' 
파이썬에서는 reverse함수 OR 슬라이싱[::-1] 사용......

T = int(input())
for _ in range(T):
    string = input()
    words = string.split()
    result = ' '.join(word[::-1] for word in words)
    print(result)

'''

def reversing(String):          #뒤집기 함수 정의
    stack = []
    result = []
    word = []

   
    for char in String:
        if char != ' ':          #공백 만나기 전까지의 단어를 word에 push
            word.append(char)
        else:
            while word:          #word에서 역순으로 꺼내서(pop해서) stack에 push + 공백까지 push
                stack.append(word.pop())
            stack.append(' ')

    while word:             #word에 문자 남아있는 동안 word -> stack 옮기기
        stack.append(word.pop())

    return ''.join(stack)   #문자열 합치기

def main():
    T = int(input())
    for _ in range(T):
        String = input()
        result = reversing(String)
        print(result)

if __name__ == "__main__":
    main()
