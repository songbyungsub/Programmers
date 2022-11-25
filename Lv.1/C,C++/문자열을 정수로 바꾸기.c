#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(const char* s) {
    int answer = 0;
    int i = 0;
    int m = 1;

    if (s[i] == '+')
        i++;
    if (s[i] == '-')
    {
        m = -1;
        i++;
    }
    while (s[i] && s[i] >= '0' && s[i] <= '9')
    {
        answer = answer * 10 + (s[i] - '0');
        i++;
    }

    return (answer * m);
}