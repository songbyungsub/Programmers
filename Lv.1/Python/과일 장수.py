def solution(k, m, score):
    answer = []
    score.sort(reverse = True)
    box=[]
    for i in range(0,len(score),m):
        box.append(score[i:m+i])
    for i in box:
        if len(i) == m:
            answer.append(min(i)*m)
    return sum(answer)

#[3,3,2,2,1,1,1]
#[4,4,4,4,4,4,2,2,2,2,1,1]