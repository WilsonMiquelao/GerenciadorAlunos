from controller import *

def mostrar_menu():
    """Exibe o menu principal"""
    print("\n=== Gerenciamento de Alunos ===")
    print("1. Adicionar aluno")
    print("2. Remover aluno")
    print("3. Atualizar aluno")
    print("4. Ver alunos cadastrados")
    print("5. Sair")

def interface_adicionar():
    """Interface para adicionar aluno"""
    matricula = int(input("Número de matrícula: "))
    nome = input("Nome do aluno: ")
    sucesso, mensagem = adicionar_aluno(matricula, nome)
    print(mensagem)

def interface_remover():
    """Interface para remover aluno"""
    matricula = int(input("Matrícula a remover: "))
    sucesso, mensagem = remover_aluno(matricula)
    print(mensagem)

def interface_atualizar():
    """Interface para atualizar aluno"""
    matricula = int(input("Matrícula a atualizar: "))
    novo_nome = input("Novo nome: ")
    sucesso, mensagem = atualizar_aluno(matricula, novo_nome)
    print(mensagem)

def interface_listar():
    """Exibe todos os alunos cadastrados"""
    alunos = buscar_alunos()
    if alunos:
        print("\n=== ALUNOS CADASTRADOS ===")
        for matricula, dados in alunos.items():
            print(f"Matrícula: {matricula} | Nome: {dados['nome']}")
    else:
        print("Nenhum aluno cadastrado.")