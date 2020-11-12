def serie1(n):
  if n == 0:
    return 1
  else:
    return 2 + serie1(n-1)
