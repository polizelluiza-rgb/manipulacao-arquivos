def sistema_alunos():
  alunos = []
  try:
    with open("alunos.txt", "r", encoding="utf-8") as f:
      for linha in f:
        partes = linha.strip().split(";")
        if len(partes) == 4:
          alunos.append({
              "id": int(partes[0]),
              "nome": partes[1],
              "idade": int(partes[2]),
              "curso": partes[3],
          })
  except FileNotFoundError:
    pass

  def salvar():
    with open("alunos.txt", "w", encoding="utf-8") as f:
      for a in alunos:
        f.write(f"{a['id']};{a['nome']};{a['idade']};{a['curso']}\n")

  while True:
    print("\n===== SISTEMA DE ALUNOS =====")
    print("1 - Listar alunos")
    print("2 - Buscar aluno")
    print("3 - Cadastrar aluno")
    print("4 - Remover aluno")
    print("5 - Alterar aluno")
    print("6 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
      print("\n1 - Listar alunos")
      for a in alunos:
        print(f"{a['id']} - {a['nome']} - {a['idade']} anos")
    elif opcao == "2":
      try:
        id_busca = int(input("Digite o ID: "))
        encontrado = next((a for a in alunos if a["id"] == id_busca), None)
        if encontrado:
          print("\nAluno encontrado:")
          print(encontrado["nome"])
          print(f"{encontrado['idade']} anos")
          print(encontrado["curso"])
        else:
          print("\nAluno não encontrado!")
      except ValueError:
        print("ID inválido.")
    elif opcao == "3":
      print("\n3 - Cadastrar aluno")
      novo_id = max([a["id"] for a in alunos], default=0) + 1
      nome = input("Nome: ")
      try:
        idade = int(input("Idade: "))
        curso = input("Curso: ")
        alunos.append({
            "id": novo_id,
            "nome": nome,
            "idade": idade,
            "curso": curso,
        })
        salvar()
        print("\nAluno cadastrado com sucesso!")
      except ValueError:
        print("Dados inválidos.")
    elif opcao == "4":
      try:
        id_rem = int(input("Digite o ID do aluno a remover: "))
        tamanho_antes = len(alunos)
        alunos = [a for a in alunos if a["id"] != id_rem]
        if len(alunos) < tamanho_antes:
          salvar()
          print("Aluno removido com sucesso!")
        else:
          print("Aluno não encontrado.")
      except ValueError:
        print("ID inválido.")
    elif opcao == "5":
      try:
        id_alt = int(input("Digite o ID do aluno a alterar: "))
        encontrado = next((a for a in alunos if a["id"] == id_alt), None)
        if encontrado:
          encontrado["nome"] = (
              input(f"Novo nome [{encontrado['nome']}]: ") or encontrado["nome"]
          )
          idade_str = input(f"Nova idade [{encontrado['idade']}]: ")
          if idade_str:
            encontrado["idade"] = int(idade_str)
          encontrado["curso"] = (
              input(f"Novo curso [{encontrado['curso']}]: ")
              or encontrado["curso"]
          )
          salvar()
          print("Dados alterados com sucesso!")
        else:
          print("Aluno não encontrado.")
      except ValueError:
        print("Dados inválidos.")
    elif opcao == "6":
      print("Sistema encerrado.")
      break
    else:
      print("\nOpção inválida!")



sistema_alunos()