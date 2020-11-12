def serie2(n):
  if n == 0: 
    return 0
  else:
    return n + serie2(n-1)
