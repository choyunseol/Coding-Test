n,m = map(int, input().split())

while True :
  print(n,"X",m,"배열을 입력하세요")
  arr = [list(map(int, input().split())) for _ in range(n)]
  if (len(arr)==n) : # 정확히 입력된걸 확인하고 싶음. array.size 해야하나
    break; 
  print("다시 입력하세요.")

data = [] #for문 안에서 선언 못하나

for i in range (n) :
  data.append(min(arr[i]))

print("정답 :", max(data))

#예시 정답 중 뭐가 더 좋은거..? 이중반복문도 결국 for쓰지않나
