#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool solution(string s) {
    bool answer = true;
    if (s.size() != 4 && s.size() != 6)
        answer = false;
    for (int i = 0; i < s.size(); i++) {
        if (isdigit(s[i]) == false)
            answer = false;
    }
    return answer;
}