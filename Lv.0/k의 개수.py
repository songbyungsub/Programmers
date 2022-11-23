def solution(i, j, k):
    answer = 0
    k = str(k)
    arr =[]
    for a in range(i,j+1):
        arr.append(str(a))
    answer = "".join(arr)
    return answer.count(k)

# def solution(i, j, k):
#     answer = 0
#     for n in range(i, j + 1):
#         answer += str(n).count(str(k))
#     return answer