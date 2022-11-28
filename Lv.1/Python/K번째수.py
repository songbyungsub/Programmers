def solution(array, commands):
    answer = []
    arr =[]
    for i in range(len(commands)):
        arr = array[commands[i][0]-1:commands[i][1]]
        arr.sort()
        answer.append(arr[commands[i][2]-1])
    return answer
# def solution(array, commands):
#     answer = []

#     for i in commands:
#         temp = array[i[0]-1:i[1]]
#         temp.sort()
#         answer.append(temp[i[2]-1])

#     return answer
