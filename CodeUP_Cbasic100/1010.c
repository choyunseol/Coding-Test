#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    printf("%d", n);
    return 0;
}

-----
  
https://codeup.kr/problem.php?id=1010

printf 함수는 두 가지 방법으로 사용
1. printf("abc");
2. printf("%s", abc);

scanf 함수는 입력을 위해 사용
scanf("%d", &x);
앞은 제어 문자열(입력 시 문자를 어떻게 해석할 것인지를 명시), 뒤는 주소 값

변환문자
c(단일 문자) d(십진 정수) e(과학 표기법으로 표현하는 부동 소수점 숫자)
f(부동 소수점 숫자) g(e형과 f형 중 짧은 것) s(문자열)
