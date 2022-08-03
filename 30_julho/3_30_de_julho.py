idade = int(input("Você é maior de idade? (digite 1 se sim, 0 se não)"))
relacionamento = int(input("Você é casado(a)? (digite 1 se sim, 0 se não):"))
if idade == 0:
    maioridade = "menor"
if idade == 1:
    maioridade = "maior"
if relacionamento == 0:
    status = "solteiro."
if relacionamento == 1:
    status = "casado."
print("Você é", maioridade,"de idade e", status)