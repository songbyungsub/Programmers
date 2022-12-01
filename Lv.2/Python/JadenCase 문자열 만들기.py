# def solution(s):
#     answer = ''
    
#     words = s.split(' ')
#     for i in range(len(words)):
#         words[i] = words[i].capitalize()
        
#     answer = ' '.join(words)
    
#     return answer
def solution(s):
    answer = ""
    temp = list(s)
    for i in range(len(temp)):
        if (i == 0) or (temp[i-1] == " "):
            answer += temp[i].upper()
        else:
            answer += temp[i].lower()
    return answer