# Dicionário global que armazenará todos os alunos
# Formato: {matricula: {"nome": "Nome do Aluno"}}
alunos = {}

# Função para criar um novo aluno (modelo de dados)
def criar_aluno(nome):
    """Retorna a estrutura de dados de um aluno"""
    return {
        "nome": nome  # Poderia ser expandido com mais campos depois
    }