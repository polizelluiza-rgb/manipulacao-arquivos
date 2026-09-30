def gerenciar_notas(nome_arquivo):
  with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
      dados = linha.strip().split(";")
      nome = dados[0]
      notas = [float(n) for n in dados[1:]]
      media = sum(notas) / len(notas)
      status = "Aprovado" if media >= 6 else "Reprovado"
      print(f"{nome} - Média: {media:.2f} - {status}")



gerenciar_notas("notas2.txt")