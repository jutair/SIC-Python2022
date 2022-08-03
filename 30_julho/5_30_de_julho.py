def e_armstrong(valor):
    entrada = str(valor)
    pot = int(len(entrada))
    add_pot = []
    soma_cubo = 0
    lista_valor = []
    final = "="
    for i in range (pot):
        lista_valor.append(entrada[i])
        for k in range (pot):
            entrada_int = int(entrada[i])
        add_pot.append(entrada_int**pot)
    soma_cubo = sum(add_pot)
    if soma_cubo == valor:
        print("O valor inserido foi de:",valor)
        print("A o cubo de", lista_valor, "é de:", add_pot)
        print("A soma de", add_pot, "é de:", soma_cubo)
        print("Portanto é um número armstrong!")
    else:
        print("O valor inserido foi de:", valor)
        print("A o cubo de", lista_valor, "é", add_pot)
        print("A soma de:", add_pot, "é de:", soma_cubo)
        print("Portanto não é um número armstrong!")
    return final*50
def gera_armstrong(inicio,fim):
    lista_armstrong = []
    for i in range (inicio,fim):
        valor = i
        entrada = str(valor)
        pot = int(len(entrada))
        add_pot = []
        soma_cubo = 0
        lista_valor = []
        for j in range (pot):
            lista_valor.append(entrada[j])
            for k in range (pot):
                entrada_int = int(entrada[j])
            add_pot.append(entrada_int**pot)
        soma_cubo = sum(add_pot)
        if soma_cubo == valor:
            lista_armstrong.append(soma_cubo)
    print("Lista de numeros armstrondo do intervalo de", inicio, "a", fim)
    return lista_armstrong
#Exemplos:
if __name__ == '__main__':
    print(e_armstrong(153))
    print(gera_armstrong(1,10000))