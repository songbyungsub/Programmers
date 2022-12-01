def solution(n):
    if n < 3:
        return n
    dp = [1,2]
    for i in range(3,n+1):
        dp.append(dp[-2]+dp[-1])
    return dp[-1] % 1234567


#2:2, 3:3, 4:5, 5:8, 6:13