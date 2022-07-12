#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    int ch = 0;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == ' ') {
            ch = 0;
            continue;
        }
        if (ch % 2 == 0 && (s[i] >= 'a' && s[i] <= 'z')) {
            s[i] -= 32;
        }
        else if (ch % 2 == 1 && (s[i] >= 'A' && s[i] <= 'Z')) {
            s[i] += 32;
        }
        ch++;
    }
    answer = s;
    return answer;
}