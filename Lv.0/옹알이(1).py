def solution(babbling):
    c = 0
    for b in babbling:
        for w in [ "aya", "ye", "woo", "ma" ]:
            if w * 2 not in b: #연속된 문자열을 골라내기 위함
                b = b.replace(w, ' ')
        if len(b.strip()) == 0:
            c += 1
    return c