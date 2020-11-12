def populacao(n):
  if n == 0 or n == 1:
    return 1
  else:
    return populacao(n-1) + populacao(n-2)
