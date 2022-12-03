def solution(s):
    answer = 0
    check = [s[0]]
    j = 0
    for i in range(1,len(s)):
        j = len(check)-1
        if check == []:
            j = 0
        if check == [] or s[i] != check[j]:
            check.append(s[i])
        elif s[i] == check[j]:
            check.pop()
    if check == []:
        answer = 1
    return answer

# def solution(s):
#     a=[]
#     for i in s:
#         if len(a)==0:
#             a.append(i)
#         elif i == a[-1]:
#             a.pop()
#         else:
#             a.append(i)
#     if len(a)==0:
#         return 1
#     return 0