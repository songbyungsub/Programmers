def solution(score):
    answer = []
    avg = []
    for i in score:
        avg.append(sum(i)/len(i))
    
    avg.sort(reverse=True)
    # for i in score:
    #     answer.append(avg.index(sum(i)/len(i))+1)
    
    return avg