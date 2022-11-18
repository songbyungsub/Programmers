def solution(n):
    answer = 0
    result = 0
    while n > 0:
        result += n % 10
        n = n//10
    return result
# def solution(n):
#     n=str(n)
#     answer=0
#     for i in n:
#         answer+=int(i)
#     return n