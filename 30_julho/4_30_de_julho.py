def listaprimos(inicio,fim):
  lista_primos =[]
  lista_compostos= []
  for i in range (inicio, fim):
      n = i
      total= 0
      for i in range(1, n+1): 
        if n %i ==0:
          total += 1
      if total ==2:
          lista_primos.append(n)
          #print(n, "É primo!")
      else:
          #print(n, "É composto!")
          lista_compostos.append(n)
  print("A lista de números primos no intervado de:", inicio, "a", fim, "=", lista_primos)
  print("A lista de números primos no compostos de:", inicio, "a", fim, "=", lista_compostos)
