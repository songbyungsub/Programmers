#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {
    bool answer = false;
    int r = 0;
    int i = x;
    while (i != 0) {
        r += i % 10;
        i /= 10;
    }
    if (x % r == 0)
        answer = true;
    else if (x % r != 0)
        answer = false;
    return answer;
}