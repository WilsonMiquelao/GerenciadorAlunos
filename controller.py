from model import alunos, criar_aluno

def adicionar_aluno(matricula, nome):
    """Adiciona um novo aluno ao sistema"""
    if matricula not in alunos:
        alunos[matricula] = criar_aluno(nome)
        return True, "Aluno cadastrado com sucesso!"
    return False, "Matrícula já cadastrada."

def remover_aluno(matricula):
    """Remove um aluno existente"""
    if matricula in alunos:
        del alunos[matricula]
        return True, "Aluno removido com sucesso!"
    return False, "Matrícula não encontrada!"

def atualizar_aluno(matricula, novo_nome):
    """Atualiza os dados de um aluno"""
    if matricula in alunos:
        alunos[matricula]["nome"] = novo_nome
        return True, "Nome do aluno atualizado com sucesso!"
    return False, "Matrícula não encontrada!"

def buscar_alunos():
    """Retorna todos os alunos cadastrados"""
    return alunos