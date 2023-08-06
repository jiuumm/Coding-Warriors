
def solution(pw):
    pw=str(pw)
    for l in range(10):
        for k in range(10):
            for j in range(10):
                    for i in range(10):
                        r=f'{l}{k}{j}{i}'
                        if r==pw:
                            print("찾았습니다!", r, pw)

solution(2312)