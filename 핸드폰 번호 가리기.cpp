#include <string>
#include <vector>

using namespace std;

string solution(string phone_number) {
    string answer = "";
    int len = phone_number.size();
    for (int i = 0; i < len - 4; i++) {
        answer.push_back(42);
    }
    for (int i = len - 4; i < len; i++) {
        answer.push_back(phone_number[i]);
    }


    return answer;
}