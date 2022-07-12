#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int left, int right) {
    int answer = 0;
    int i;
    int count_num;
    int num = left;
    while (num <= right)
    {
        i = 1;
        count_num = 0;
        while (i <= num)
        {
            if (num % i == 0)
                count_num++;
            i++;
        }
        if (count_num % 2 == 0)
            answer += num;
        else
            answer -= num;

        num++;
    }
    return answer;
}