contatos = []

def adicionar_contato():
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    contato = {
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
        "email": email
    }
    contatos.append(contato)
    print("Contato adicionado com sucesso!")

def listar_contatos():
    if not contatos:
        print("Nenhum contato salvo.")
        return

    for i, contato in enumerate(contatos):
        print(f"\nContato {i + 1}")
        for chave, valor in contato.items():
            print(f"{chave.capitalize()}: {valor}")

def buscar_contato():
    termo = input("Digite o nome para buscar: ").lower()
    encontrados = [c for c in contatos if termo in c["nome"].lower()]
    
    if encontrados:
        print("\n--- Contatos encontrados ---")
        for contato in encontrados:
            for chave, valor in contato.items():
                print(f"{chave.capitalize()}: {valor}")
            print("-" * 20)
    else:
        print("Nenhum contato encontrado com esse nome.")

def editar_contato():
    listar_contatos()
    indice = int(input("Digite o número do contato que deseja editar: ")) - 1
    if 0 <= indice < len(contatos):
        print("Deixe em branco para manter o valor atual.")
        for chave in contatos[indice]:
            novo_valor = input(f"{chave.capitalize()} ({contatos[indice][chave]}): ")
            if novo_valor:
                contatos[indice][chave] = novo_valor
        print("Contato atualizado!")
    else:
        print("Contato inválido.")

def excluir_contato():
    listar_contatos()
    indice = int(input("Digite o número do contato que deseja excluir: ")) - 1
    if 0 <= indice < len(contatos):
        contatos.pop(indice)
        print("Contato excluído!")
    else:
        print("Contato inválido.")

def menu():
    while True:
        print("\n--- Menu Agenda ---")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Buscar contato por nome")  # Agora é a opção 3
        print("4. Editar contato")
        print("5. Excluir contato")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            buscar_contato()
        elif opcao == "4":
            editar_contato()
        elif opcao == "5":
            excluir_contato()
        elif opcao == "6":
            print("Encerrando agenda.")
            break
        else:
            print("Opção inválida.")

menu()
