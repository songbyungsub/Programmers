def solution(common):
    answer = 0
    for i in common:
        if (common[1] - common[0]) == (common[2]-common[1]):
            answer = common[-1]+ (common[1] - common[0])
        elif(common[1] / common[0]) == (common[2] / common[1]):
            answer = common[-1]*(common[1]/common[0])
    return answer