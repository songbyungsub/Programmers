def solution(brown, yellow):
    answer = []
    tt = brown + yellow
    for w in range(1,tt+1):
        h = tt//w
        if w * h == tt and w >= h:
            if (2*w) + (2*h) - 4 == brown and (w-2) * (h-2) == yellow:
                answer.append(w)
                answer.append(h)
    return answer
# 2w + 2h - 4 = brown
# w-2 * h-2 = yellow
# wh - 2w -2h +4 = yellow
# wh - brown = yellow
# wh = tt