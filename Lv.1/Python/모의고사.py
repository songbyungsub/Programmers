def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5,]
    count=[0,0,0]
    for i in range(len(answers)):
        if answers[i] == a[(i%5)]:
            count[0] += 1
        if answers[i] == b[(i%8)]:
            count[1] += 1
        if answers[i] == c[(i%10)]:
            count[2] += 1
            
    for i in range(len(count)):
        if count[i] == max(count):
            answer.append(i+1)

    return answer

#1 : 12345
#2 : 21232425
#3 : 3311224455