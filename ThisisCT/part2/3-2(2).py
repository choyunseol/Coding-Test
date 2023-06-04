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

count = int(m/(k+1))*k
count += m%(k+1)

result = 0
result += (count)*first
result += (m-count)*second

print(result)
