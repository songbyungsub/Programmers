def solution(lottos, win_nums):
    answer = []
    count = 0
    zero = 0
    lst = []
    for i in lottos:
        if i != 0 and i in win_nums:
            count += 1
        elif i == 0:
            zero += 1
    lst.append(count+zero)
    lst.append(count)
    
    for i in lst:
        if 7 - i >=6:
            i = 6
            answer.append(i)
        else:
            answer.append(7-i)
    return answer