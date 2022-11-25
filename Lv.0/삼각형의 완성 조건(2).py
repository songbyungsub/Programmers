# def solution(sides):
#     answer = 0
#     s = sum(sides)
#     m = max(sides)
#     mm = min(sides)
#     if m == mm:
#         answer = 1
#     for i in range(1,1001):
#         if (m >= i and i+mm > m) or (m+mm > i and i > m):
#             answer +=1
#     return answer

def solution(sides):
    answer = 0
    a = max(sides) - min(sides) 
    b = max(sides) + min(sides) 
    return b-a-1