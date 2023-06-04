n=1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
list = [500,100,50,10]
for coin in list:
  count += n // coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
  n %= coin
  
print(count)

# 동전의 개수가 K개일 때, 위 코드의 시간복잡도는 

'''
<연산자>
덧셈 +, 뺄셈 -, 곱셈 *, 나눗셈 /, 거듭제곱 **, 몫 //, 나머지 %

<반복문>
for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    ...
'''