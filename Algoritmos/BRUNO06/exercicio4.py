def torre_hanoi(n, torre_origem, torre_destino):
  if n == 1:
    pm(torre_origem,torre_destino)
  else:
    torre_intermediaria = 6 - (torre_origem + torre_destino)
    torre_hanoi(n-1, torre_origem, torre_intermediaria)
    pm(torre_origem,torre_destino)
    torre_hanoi(n-1, torre_intermediaria, torre_destino)

def pm(s,e):
  print(f"\nTorre {s} -> Torre {e}")
