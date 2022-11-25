#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(int n, int m) {
    vector<int> answer;
    int result;
    int a, b;
    a = n;
    b = m;
    while (b != 0)
    {
        result = a % b;
        a = b;
        b = result;
    }
    answer.push_back(a);
    answer.push_back(n * m / a);
    return answer;
}