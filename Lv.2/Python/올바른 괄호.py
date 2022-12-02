# def solution(s):
#     answer = []
#     for i in s:
#         if i == '(':
#             answer.append(i)
#         else:
#             if answer == []: return False
#             else:
#                 answer.pop()
#     if answer == []: return True
#     else: return False

def solution(s):
    answer = []
    for i in range(len(s)):
        if s[i] == '(':
            answer.append(s[i])
        elif s[i] == ')' and s[i-1] == '(':
                answer.append(s[i])
    # if answer == []: return True
    # else: return False
    return answer