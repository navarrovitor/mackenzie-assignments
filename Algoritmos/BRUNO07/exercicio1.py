def serie1(n):
  if n == 1:
    return 1
  else:
    return serie1(n-1) + (2 * n - 1)
