# N, M, K를 공백으로 구분하여 입력받기 
while True :
  n,m,k = map(int, input().split())
  if k <= m :
    break

# N개의 수를 공백으로 구분하여 입력받기
while True :
  data = list(map(int, input().split()))
  if len(data) == n :
    break

data.sort() #입력받은 수 정렬
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수 더하기

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1))*k
count += m%(k+1)

result = 0
result += (count)*first # 가장 큰 수 더하기
result += (m-count)*second # 두 번째로 큰 수 더하기

print(result) # 최종 답안 출력
