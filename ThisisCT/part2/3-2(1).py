while True :
  n,m,k = map(int, input().split())
  if k <= m :
    break

while True :
  data = list(map(int, input().split()))
  if len(data) == n :
    break

data.sort()
first = data[n-1]
second = data[n-2]

result = 0
while True:
  for i in range (k) :
    if m == 0 :
      break
    result += first
    m -= 1
  result += second
  m -= 1
  if m == 0 :
      break

print(result)

# break 한번만 쓰고 해결할 수 없나
# 코테에서 예외처리 다 안해도 되나
