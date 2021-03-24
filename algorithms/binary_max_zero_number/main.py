def solution(N):
  binary_N = bin(N).replace('0b', '')

  count = 0
  biggest = 0
  for i in binary_N:
    if i == '1':
      if count > biggest:
        biggest = count
      count = 0
    if i == '0':
      count += 1
  return biggest  

solution(529)

# 파이썬 내장모듈 bin() 을 통해 값을 이진수로 변경한 뒤
# 1과 0 으로 구성된 부분만 남긴다
# 0의 개수가 가장 큰 파트를 biggest 에 저장하고 마지막에 biggest 를 리턴