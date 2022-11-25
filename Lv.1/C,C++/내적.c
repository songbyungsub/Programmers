#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int a[], size_t a_len, int b[], size_t b_len) {
    int answer = 0;
    int i;
    i = 0;
    int result = 0;

    while (i < a_len && i < b_len)
    {
        result = a[i] * b[i];
        answer += result;
        i++;
    }
    return answer;
}