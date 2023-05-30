#include <stdio.h>

int main(){
    char data[21];
    scanf("%s", data);
    for (int i=0; data[i]!='\0'; i++){
        printf("\'%c\'\n", data[i]);
    }
}

-----
  
https://codeup.kr/problem.php?id=1024
- 문자열 입력시 주소연산자 사용하지 않아도 됨.
- for 반복문의 기본 구조
  for(초기화 ; 조건문 ; 증가 감소식)
{
  // ... 
}
