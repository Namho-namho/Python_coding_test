#include <string>
#include <vector>

using namespace std;

bool kant(long long i){ //64bit 정수형
    while (i > 0){
        if (i % 5 == 2){
            return false;
        }
        i /= 5;
    }
    return true;
}

int solution(int n, long long l, long long r) {
    int answer = 0;
    
    for (long long i = l - 1; i < r; i++){
        if (kant(i)){
            answer++;
        }
    }
    return answer;
}