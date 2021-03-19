def factorial(n):
  if n == 0:
    return 1
  if n == 1:
    return n

  return factorial(n - 1) * n 

factorial(5)

# f(5) -> f(4) -> f(3) ... f(1)
# f(1) = 1, 1 * 2, 2 * 3, 6 * 4, 24 * 5
# 24 * 5 = 120
