#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    int left = 0;
    int right = 0;

    for (int i = 0; i < sizes.size(); i++) {
        left = max(left, min(sizes[i][0], sizes[i][1]));
        right = max(right, max(sizes[i][0], sizes[i][1]));
    }
    return left * right;
}