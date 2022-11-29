def solution(n):
    answer = 0
    lst = []
    for i in range(1,n+1):
        if n % i == 1:
            lst.append(i)
    return lst[0]