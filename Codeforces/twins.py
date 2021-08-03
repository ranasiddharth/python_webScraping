n = int(input())
sum = 0
arr = list(map(int, input().split()))
for i in arr:
  sum+=i
arr.sort(reverse=True)
coin_sum = 0
coin_count = 0
for i in arr:
  coin_sum+=i
  coin_count+=1
  if(coin_sum>sum/2):
    break
print(coin_count)