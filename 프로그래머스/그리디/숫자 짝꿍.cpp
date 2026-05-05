#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string X, string Y) {
    string answer = "";
    int countX[10] = {0};
    int countY[10] = {0};
    
    for (int i = 0 ; i < X.size() ; i++){
        int num = X[i] - '0'; // 문자 -> 숫자
        countX[num]++;
    }
    for (int i = 0 ; i < Y.size() ; i++){
        int num = Y[i] - '0';
        countY[num]++;
    }
    
    for (int num = 9 ; num >= 0 ; num--){
        int C = min(countX[num], countY[num]);
        for (int j = 0 ; j < C ; j++){
            answer += char(num + '0'); // 숫자 -> 문자
        }
    }
    if (answer.empty()) {
        return "-1";
    }

    if (answer[0] == '0') {
        return "0";
    }
    
    return answer;
}