#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int nums[], size_t nums_len) {
    int answer = 0;
    int sum = 0;
    for (int i = 0; i < nums_len; i++) {
        for (int j = i + 1; j < nums_len; j++) {
            for (int k = j + 1; k < nums_len; k++) {
                sum = nums[i] + nums[j] + nums[k];
                int count = 0;
                for (int h = 2; h < sum; h++) {
                    if (sum % h == 0)
                        count++;
                }
                if (count == 0)
                    answer++;
            }
        }
    }
    return answer;
}