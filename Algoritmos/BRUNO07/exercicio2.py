def inverter(vetor):
  menor = vetor[0]
  if len(vetor) == 1:
    return menor
  else:
    return inverter(vetor[1::]) + menor
