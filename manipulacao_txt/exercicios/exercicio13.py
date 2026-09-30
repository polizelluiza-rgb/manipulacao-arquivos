def menu_arquivo():
  while True:
    print("\n1 - Ler arquivo")
    print("2 - Adicionar texto")
    print("3 - Sobrescrever arquivo")
    print("4 - Sair")
    escolha = input("Escolha: ")

    if escolha == "1":
      try:
        with open("notas.txt", "r", encoding="utf-8") as f:
          print(f.read())
      except FileNotFoundError:
        print("O arquivo ainda não existe.")
    elif escolha == "2":
      texto = input("Digite o texto para adicionar: ")
      with open("notas.txt", "a", encoding="utf-8") as f:
        f.write(texto + "\n")
    elif escolha == "3":
      texto = input("Digite o texto para sobrescrever: ")
      with open("notas.txt", "w", encoding="utf-8") as f:
        f.write(texto + "\n")
    elif escolha == "4":
      print("Programa encerrado.")
      break
    else:
      print("Opção inválida!")


menu_arquivo()