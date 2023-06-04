# N,M,K를 공백으로 구분하여 입력받기
while True :
  n,m,k = map(int, input().split())
  if k <= m :
    break

# N개의 수를 공백으로 구분하여 입력받기
while True :
  data = list(map(int, input().split()))
  if len(data) == n :
    break

data.sort() #입력받은 수들 정렬하기
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수

result = 0
while True:
  for i in range (k) : # 가장 큰 수를 K번 더하기
    if m == 0 : # m이 0이라면 반복문 탈출
      break
    result += first
    m -= 1
  result += second # 두 번째로 큰 수를 한 번 더하기
  m -= 1 # 더할 때마다 1씩 빼기
  if m == 0 :
      break

print(result) # 최종 답안 출력

# break 한번만 쓰고 해결할 수 없나
# 코테에서 예외처리 다 안해도 되나
