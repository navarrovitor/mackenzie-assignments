def rec(n):
  if n == 0:
    return 0
  else:
    return rec(n-1) + ((n**2)+1)/(n+3)
  
for i in range(4):
  print(rec(i))