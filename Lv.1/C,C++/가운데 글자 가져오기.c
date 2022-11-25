#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


char* solution(const char* s) {
    char* answer;
    int len = 0;
    while (s[len])
        len++;
    if (len % 2 == 1)
    {
        answer = (char*)malloc(sizeof(char) * 2);
        answer[0] = s[len / 2];
        answer[1] = '\0';
    }
    else if (len % 2 == 0)
    {
        answer = (char*)malloc(sizeof(char) * 3);
        answer[0] = s[len / 2 - 1];
        answer[1] = s[len / 2];
        answer[2] = '\0';
    }
    return answer;
}