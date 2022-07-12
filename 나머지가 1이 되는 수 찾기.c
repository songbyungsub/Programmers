#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    int i = 2;

    while (n > i)
    {
        if (n % i == 1) {
            answer = i;
            break;
        }
        i++;
    }

    return answer;
}