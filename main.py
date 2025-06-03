from view import *

def main():
    """Função principal que controla o fluxo do programa"""
    while True:
        mostrar_menu()
        opcao = input("Opção: ")

        if opcao == "1":
            interface_adicionar()
        elif opcao == "2":
            interface_remover()
        elif opcao == "3":
            interface_atualizar()
        elif opcao == "4":
            interface_listar()
        elif opcao == "5":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()