def maxProfit(prices):
  min_price = min(prices)
  min_index = prices.index(min_price)

  max_price = max(prices[min_index:])
  max_index = prices.index(max_price)

  if min_index > max_index:
    return 0
  
  return max_price - min_price

m = maxProfit([7,1,5,3,6,4])

# 가장 작은 값과 그 인덱스를 구하고
# 그 인덱스 다음부터 가장 큰 값을 구한 뒤
# 가장 큰 값과 가장 작은 값을 빼면 됨