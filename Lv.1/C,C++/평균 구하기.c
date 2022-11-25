#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

double solution(int arr[], size_t arr_len) {
    double answer = 0;
    int i = 0;

    while (i < arr_len) {
        answer += arr[i];
        i++;
    }
    answer /= arr_len;
    return answer;
}