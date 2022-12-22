# import Counter
# def solution(X, Y):
#     answer = ''
#     x = sorted(list(X),reverse=True)
#     y = sorted(list(Y),reverse=True)
#     lst =[]
#     for i in x:
#         if i in y:
#             lst.append(i)
#     lst.sort(reverse=True)
#     lst2=[]
#     for i in range(len(lst)):
#         if lst[i] == y[i]:
#             lst2.append(lst[i])
#     return lst

from collections import Counter

def solution(X, Y):
    answer = '-1'
    
    list_X, list_Y = list(X), list(Y)
    set_X, set_Y = set(list_X), set(list_Y)
    cnt_X, cnt_Y = Counter(list_X), Counter(list_Y)
    
    intersection = set_X & set_Y
    
    if intersection:
        answer = ''
        sorted_number = sorted(intersection, reverse=True)
        
        for num in sorted_number:
            answer += num * min(cnt_X[num], cnt_Y[num])
        
        if sum(list(map(int, list(answer)))) == 0:
            answer = "0"
    
    return answer