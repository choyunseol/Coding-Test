#include <stdio.h>

int main(){
    float x;
    scanf("%f", &x);
    printf("%.2f", x);
    return 0;
}

-----
  
https://codeup.kr/problem.php?id=1015
%.3f 와 같은 형식으로 지정하면,
소수점 이하 넷 째 자리에서 반올림하여 소수점 이하 셋 째 자리까지 출력하라는 의미
