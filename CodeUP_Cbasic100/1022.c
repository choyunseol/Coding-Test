#include <stdio.h>

int main(){
    char data[2001];
    fgets(data, 2000, stdin);
    printf("%s", data);
}

-----

https://codeup.kr/problem.php?id=1022
- fgets( ) 를 사용하면 공백문자가 포함되어잇는 문장을 입력받아 저장할 수 있다.
- scanf("%s", ... ) 를 이용해 문장을 입력받으면, 첫 번째 단어까지만 저장된다.
