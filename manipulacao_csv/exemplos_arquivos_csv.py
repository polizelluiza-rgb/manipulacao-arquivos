import csv

def criar_csv():
    with open("alunos.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(["Nome", "Idade", "Curso"])

        escritor.writerow(["Luiza", "16", "Python"])
        escritor.writerow(["Camila", "17", "Python"])
        escritor.writerow(["Manu", "17", "Python"])
        escritor.writerow(["Maria", "18", "Python"])


#criar_csv()


def salvar_alunos():
    alunos = [
        ["Luiza", "16", "Python"],
        ["Camila", "17", "Python"],
        ["Maria", "18", "Python"],
        ["Manu", "17", "Python"],
        ["Sarah", "18", "Python"],
        ["Niki", "20", "Python"],
        ["Tata", "14", "Python"]

    ]
    with open("novos_alunos.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(["Nome", "Idade", "Curso"])

        escritor.writerows(alunos)
#salvar_alunos()


def ler_csv():
    with open("novos_alunos.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        next(leitor)

        for linha in leitor:
            print(linha[0])

#ler_csv()


def exibir_alunos():
    with open("novos_alunos.csv", "r", encoding="utf-8") as arquivo:
        alunos = csv.DictReader(arquivo)

        for aluno in alunos:
            print(aluno)

#exibir_alunos()


def cadastrar_aluno():
    with open("novos_alunos.csv", "a+", newline="", encoding="utf-8") as arquivo:
        arquivo.seek(0,2)
        nome = input("digite o nome do aluno: ")
        idade = input("digite a idade do aluno: ")
        curso = input("digite o curso do aluno: ")

        escritor = csv.writer(arquivo)

        escritor.writerow([nome, idade, curso])

#cadastrar_aluno()


def deletar_aluno():

    with open("novos_alunos.csv", "r", newline="",  encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        alunos = list(leitor)

    with open("novos_alunos.csv", "w", newline="",  encoding="utf-8") as arquivo:
        cabecalho = ['Nome', 'Idade', 'Curso']
        escritor = csv.DictWriter(arquivo, fieldnames=cabecalho)

        escritor.writeheader()

        aluno_apagar = input("digite o nome do aluno que dejesa apagar: ")
        
        for aluno in alunos:
            if aluno["nome"] != aluno_apagar:
                escritor.writerow(aluno)
























