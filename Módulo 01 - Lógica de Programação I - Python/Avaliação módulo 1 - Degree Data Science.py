cadastro={}

menu = int(input("**** Cadastro de Fornecedor ****\n Digite (1) para exibir os fornecedores cadastrados: "
                     " \n Digite (2) para remover fornecedor: \n Digite (3) para cadastrar fornecedor:\n "))

def perguntas(menu):
    if menu == 1:
        while menu == 1:
            print("Os Fornecedores cadastrados são: \n", cadastro)
            menu = int(input("Digite:\n (1) para exibir os fornecedores cadastrados:"
                             "\n (2) para remover fornecedor \n (3) para cadastrar fornecedor:\n "))
            if menu != 1:
                perguntas(menu)

    elif menu == 2 and cadastro == {}:
        while menu == 2 and cadastro == {}:
            print("Impossível remover fornecedor! Não existem dados cadastrados")
            menu = int(input("Digite:\n (1) para exibir\n (2) para remover \n (3) para cadastrar fornecedor:\n "))
            if menu == 2 and cadastro != {}:
                perguntas(menu)

    if menu == 2 and cadastro != {}:
        remover = int(input("Digite o código do fornecedor que deseja remover"))
        removido = cadastro.pop(remover)
        print("Fornecedor removido com sucesso! \nO fornecedor removido foi:", removido)
        menu = int(input("Digite:\n (1) para exibir os fornecedores cadastrados:"
                         "\n (2) para remover fornecedor: \n (3) para cadastrar fornecedor:\n "))
        perguntas(menu)


    if menu == 3:
        codigo_fornecedor = int(input("Digite o Código do Fornecedor: "))
        nome_fornecedor = input("Digite o Nome do Fornecedor: ")
        telefone_fornecedor = input("Digite o telefone do Fornecedor: ")
        email_fornecedor = input("Digite o email do Fornecedor: ")

        cadastro[codigo_fornecedor] = nome_fornecedor,telefone_fornecedor, email_fornecedor

        novo_cadastro = input("Deseja realizar um novo cadastro, 'Sim' ou 'Não':")
        if novo_cadastro == "Não":
            menu = int(input("Digite:\n (1) para exibir os fornecedores cadastrados:"
                             "\n (2) para remover fornecedor: \n (3) para cadastrar fornecedor:\n "))
            perguntas(menu)

    while novo_cadastro == "Sim":
        codigo_fornecedor = int(input("Digite o Código do Fornecedor: "))
        nome_fornecedor = input("Digite o Nome do Fornecedor: ")
        telefone_fornecedor = input("Digite o telefone do Fornecedor: ")
        email_fornecedor = input("Digite o email do Fornecedor: ")

        cadastro[codigo_fornecedor] = nome_fornecedor,telefone_fornecedor, email_fornecedor

        novo_cadastro == "vazio"

        novo_cadastro = input("Deseja realizar um novo cadastro, 'Sim' ou 'Não':")

        menu = int(input("Digite:\n (1) para exibir os fornecedores cadastrados:"
                         "\n (2) para remover fornecedor: \n (3) para cadastrar fornecedor:\n "))
        perguntas(menu)

r1 = perguntas(menu)
print(r1)

