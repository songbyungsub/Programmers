#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int a, int b) {
    long long answer = 0;

    if (a == b)
        answer = a;
    if (a < b) {
        long long count = 0;
        while (a <= b)
        {
            count += a;
            a++;
        }
        return count;
    }
    if (a > b) {
        long long count = 0;
        while (b <= a)
        {
            count += b;
            b++;
        }
        return count;
    }

    return answer;
}