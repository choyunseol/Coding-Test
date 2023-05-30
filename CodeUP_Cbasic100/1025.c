#include <stdio.h>
#include <math.h>

int main(){
    int num[5];
    scanf("%1d%1d%1d%1d%1d", &num[0], &num[1], &num[2], &num[3], &num[4]);
    for (int i=0; i<5;i++){
        int mul = pow(10,4-i);
        printf("[%d]\n",num[i]*mul);
    }
}

-----

https://codeup.kr/problem.php?id=1025
- 제곱함수 : pow(밑, 지수) (math 라이브러리)
  
질문 : 왜 num[i]*pow(10,4-i)하면 
[1026]
[1025]
[1025]
[1024]
[0]
이렇게 출력될까
