# Modo "r" - Abre o arquivo para leitura
# Modo "w" - Abre para a escrita e apaga o conteudo existente
# Modo "a" - Adiciona novo conteudo no final do arquivo
# Modo "x" - Cria um arquivo novo e gera erro se ele ja existir

def criar_arquivo():
    # O "with" fecha o arquivo automaticamente
    # 0 "open()" funçao para leitura ou escrita de arquivos
    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Luiza\n")
        arquivo.write("Maria\n")
        arquivo.write("Tata\n")

criar_arquivo()


def adicionar_aluno(nome):
    with open("teste.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(nome + "\n")


adicionar_aluno("Luiza")
adicionar_aluno("Maria")
adicionar_aluno("Tata")



def listar_alunos():
    with open("teste.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    print(f'o conteudo do arquivos alunos é:{conteudo}')

#listar_alunos()

def listar_alunos_individual():
    lista_alunos = []
    with open("teste.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
           lista_alunos.append(linha.strip())

    print(f'lista de alunos: {lista_alunos} ')

listar_alunos_individual()


def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = input("Digite a idade do aluno: ")

    with open("cadastro.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f' {nome}; {idade} \n')

    print("aluno cadastrado com sucesso")

#cadastrar_aluno()


def listar_cadastro():
    itens_cadastro = []
    with open("cadastro.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, idade = linha.strip().split(";")

            obj = {
                "Nome": nome,
                "Idade": idade
            }
            itens_cadastro.append(obj)
    print(f'itens cadastrados: {itens_cadastro}')

listar_cadastro()
















