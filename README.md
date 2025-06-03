# Gerenciador de Alunos

Projeto simples de gerenciamento de alunos utilizando Python com arquitetura baseada no padrão MVC (Model-View-Controller).

## 📚 Descrição

Este sistema permite o cadastro, listagem, atualização e remoção de alunos, simulando um pequeno sistema CRUD. O objetivo é demonstrar a separação de responsabilidades entre camadas: dados (Model), lógica (Controller) e interface (View).

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**: Linguagem principal do projeto
- **Padrão MVC**: Organização do código em camadas
- **Terminal/CLI**: Interação por linha de comando

---

## 🧠 Lógica e Arquitetura

O projeto é dividido em três partes principais:

### 1. `model.py` (Model)
Responsável por armazenar e gerenciar os dados dos alunos. Pode conter uma lista em memória com operações como adicionar, atualizar, buscar e excluir alunos.

### 2. `view.py` (View)
Faz a interface com o usuário — imprime menus, solicita entradas e exibe resultados. A comunicação é feita toda pelo terminal (CLI).

### 3. `controller.py` (Controller)
Coordena a lógica do programa: recebe ações da `view`, manipula os dados usando o `model` e retorna as respostas apropriadas.

### 4. `main.py`
É o ponto de entrada da aplicação. Inicializa os componentes e inicia o loop principal de interação com o usuário.

---
