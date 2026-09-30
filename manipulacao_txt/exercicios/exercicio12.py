def classificar_alunos(nome_arquivo):
  with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
      dados = linha.strip().split(";")
      nome = dados[0]
      nota = float(dados[1])

      if nota >= 6.0:
        status = "Aprovado"
      elif nota >= 4.0:
        status = "Recuperação"
      else:
        status = "Reprovado"

      print(f"{nome} - {nota} - {status}")



classificar_alunos("alunos.txt")