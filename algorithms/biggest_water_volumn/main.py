def get_max_area(height):
  biggest = 0

  for n in range(len(height)):
    for x in range(n + 1, len(height)):
      before_y = height[n]
      y = height[x]

      size = before_y * abs(n - x) if y > before_y else y * abs(n - x)

      if size > biggest:
        biggest = size
      before_y = y
  return biggest

m = get_max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(m)