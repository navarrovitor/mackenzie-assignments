def contador(N, K):
  x = str(N)
  if not x:
    return 0
  elif K == x[0]:
    return 1 + contador(x[1:],K)
  else:
    return 0 + contador(x[1:],K)
