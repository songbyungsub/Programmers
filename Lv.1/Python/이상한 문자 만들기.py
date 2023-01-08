def solution(s):
    answer= s.split(' ')
    a =[]
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            if j % 2 == 0:
                a.append(answer[i][j].upper())
            else:a.append(answer[i][j].lower())
        a.append(' ')
    del a[-1]
    return "".join(a)