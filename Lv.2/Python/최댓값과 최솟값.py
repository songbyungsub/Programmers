# def solution(s):
#     answer = []
#     answer2 = []
#     a = s.split(' ')
#     for i in a:
#         answer.append(int(i))
#     answer.sort()
#     answer2.append(str(answer[0]))
#     answer2.append(' ')
#     answer2.append(str(answer[-1]))
#     return ''.join(answer2)

def solution(s):
    s = list(map(int,s.split()))
    answer = str(min(s)) + " " + str(max(s))
    return s