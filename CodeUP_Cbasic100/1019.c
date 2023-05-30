#include <stdio.h>

int main(){
    int y, m, d;
    scanf("%d.%d.%d", &y,&m,&d);
    printf("%04d.%02d.%02d", y,m,d);
}

-----
  
https://codeup.kr/problem.php?id=1019
%02d를 사용하면 2칸을 사용해 출력하는데, 한 자리 수인 경우 앞에 0을 붙여 출력한다.
