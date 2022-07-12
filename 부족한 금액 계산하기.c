#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int price, int money, int count) {
    long long answer = 0;
    long long total = 0;
    while (count > 0)
    {
        total += count * price;
        count--;
    }
    if (money >= total)
        return 0;
    else if (total > money)
        answer = total - money;
    return answer;
}