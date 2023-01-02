# def solution(participant, completion):
#     answer = ''
#     result =[]
#     for i in participant:
#         if participant.count(i) == 1:
#             if i not in completion:
#                 result.append(i)
#     return result

def solution(participant, completion):
    completion.sort()
    participant.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return  participant[-1]; 