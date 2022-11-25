def solution(n):
    answer = 0
    lst=[]
    new=[]
    for i in range(1,201):
        if i%3 != 0:
            lst.append(i)
    for i in lst:
        if '3' not in str(i):
            new.append(i)
    for i in new:
        answer = new[n-1]
    return answer

# def solution(n):
#     answer = 0
#     for _ in range(n):
#         answer += 1
#         while answer %3 == 0 or '3' in str(answer):
#             answer += 1
#     return answer