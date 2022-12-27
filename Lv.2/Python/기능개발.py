def solution(progresses, speeds):
    answer = []
    work = []
    for i in range(len(progresses)):
        if speeds[i] == 1:
            work.append(100-progresses[i])
        elif speeds[i] != 1 and 100 % speeds[i] == 0:
            work.append((100//speeds[i]) - (progresses[i]//speeds[i]))
        elif speeds[i] != 1 and 100 % speeds[i] != 0:
            work.append(((100-progresses[i])//speeds[i]) +1)
    count = 1
    point = work[0]
    i = 1
    while i < len(work):
        if work[i] <= point:
            count +=1
        else:
            answer += [count]
            point = work[i]
            count = 1
        i += 1
    answer += [count]
    return answer

print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))