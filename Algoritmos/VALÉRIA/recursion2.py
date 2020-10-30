def rec(n):
  if len(n) == 0 or len(n) == 1:
    return True
  elif n[0] != n[-1]:
    return False
  else:
    return rec(n[1:-1])

# while True:
#   print(rec(input()))