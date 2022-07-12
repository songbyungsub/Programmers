#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(long long n) {
    vector<int> answer;
    int i = 0;
    while (1) {
        answer.push_back(n % 10);
        n /= 10;
        if (n == 0)
            break;
    }
    return answer;
}