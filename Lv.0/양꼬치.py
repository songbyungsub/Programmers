def solution(n, k):
    answer = 12000 *n + 2000*k
    i = 0
    if n >= 10:
      i = (n // 10) * 2000
    return answer - i