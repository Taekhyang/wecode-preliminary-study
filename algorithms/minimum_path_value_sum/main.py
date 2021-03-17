def min_path_sum(grid):
  x = len(grid[0])
  y = len(grid)

  for i in range(1, x):
    grid[0][i] += grid[0][i - 1]
  for i in range(1, y):
    grid[i][0] += grid[i - 1][0]
  
  for i in range(1, x):
    for j in range(1, y):
      grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
  return grid[-1][-1]

min_path_sum([
   [1,3,1],
   [1,5,1],
   [4,2,1]
])

# 첫 줄 세로와 첫 줄 가로에서는 각 그리드의 최솟값이 1개로 정해져 있기 때문에
# 각 그리드에 그 그리드 까지 가기까지의 최솟값을 모두 더한다.
# 그 다음부터 x, y 값의 최대값을 range 로 이중 for 문을 돌면서
# 왼쪽이나 위 그리드 값 중 더 작은 그리드 값을 더한다.
# 맨 오른쪽 아래 그리드 grid[-1][-1] 의 값이 목적지까지 경로 요소 합의 최솟값이 된다.
