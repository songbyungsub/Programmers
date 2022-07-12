#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int numbers[], size_t numbers_len) {
    int i;
    int answer;
    answer = 0;
    i = 0;
    while (i < numbers_len)
    {
        answer += numbers[i];
        i++;
    }
    answer = 45 - answer;

    return answer;
}