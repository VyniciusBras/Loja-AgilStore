import uuid

def gerar_id_unico():
    return str(uuid.uuid4())

def adicionar_produto(inventario):
    print("\nAdicionando um novo produto ao inventário...")

    nome = input("Nome do Produto: ")
    categoria = input("Categoria: ")
    
    while True:
        try:
            quantidade = int(input("Quantidade em Estoque: "))
            if quantidade < 0:
                raise ValueError("A quantidade deve ser um número positivo.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}")

    while True:
        try:
            preco = float(input("Preço: "))
            if preco < 0:
                raise ValueError("O preço deve ser um número positivo.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}")

    id_produto = gerar_id_unico()

    produto = {
        "id": id_produto,
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "preco": preco
    }

    inventario.append(produto)
    print(f"Produto '{nome}' adicionado com sucesso! ID: {id_produto}\n")

def listar_produtos(inventario):
    #Mostra todos os produtos cadastrados.
    if not inventario:
        print("\nO inventário está vazio.\n")
        return

    print("\nInventário de Produtos:")
    print(f"{'ID':<36} {'Nome':<20} {'Categoria':<15} {'Quantidade':<10} {'Preço':<10}")
    print("-" * 85)
    for produto in inventario:
        print(f"{produto['id']:<36} {produto['nome']:<20} {produto['categoria']:<15} {produto['quantidade']:<10} {produto['preco']:<10.2f}")

def atualizar_produto(inventario):
    #Função criada para atualizar o produto.
    if not inventario:
        print("\nO inventário está vazio. Não há produtos para atualizar.\n")
        return

    id_produto = input("\nInforme o ID do produto que deseja atualizar: ")
    produto = next((p for p in inventario if p["id"] == id_produto), None)

    if not produto:
        print("Produto não encontrado. Verifique o ID informado.\n")
        return

    print("\nProduto encontrado. Escolha os campos para atualizar:")
    if input("Deseja atualizar o Nome? (s/n): ").lower() == 's':
        produto["nome"] = input("Novo Nome: ")
    if input("Deseja atualizar a Categoria? (s/n): ").lower() == 's':
        produto["categoria"] = input("Nova Categoria: ")
    if input("Deseja atualizar a Quantidade? (s/n): ").lower() == 's':
        while True:
            try:
                quantidade = int(input("Nova Quantidade: "))
                if quantidade < 0:
                    raise ValueError("A quantidade deve ser um número positivo.")
                produto["quantidade"] = quantidade
                break
            except ValueError as e:
                print(f"Entrada inválida: {e}")
    if input("Deseja atualizar o Preço? (s/n): ").lower() == 's':
        while True:
            try:
                preco = float(input("Novo Preço: "))
                if preco < 0:
                    raise ValueError("O preço deve ser um número positivo.")
                produto["preco"] = preco
                break
            except ValueError as e:
                print(f"Entrada inválida: {e}")

    print("\nProduto atualizado com sucesso!\n")

def excluir_produto(inventario):
    #Remove um produto do inventário pelo ID.
    if not inventario:
        print("\nO inventário está vazio. Não há produtos para excluir.\n")
        return

    id_produto = input("\nInforme o ID do produto que deseja excluir: ")
    produto = next((p for p in inventario if p["id"] == id_produto), None)

    if not produto:
        print("Produto não encontrado. Verifique o ID informado.\n")
        return

    confirmar = input(f"Tem certeza que deseja excluir o produto '{produto['nome']}'? (s/n): ").lower()
    if confirmar == 's':
        inventario.remove(produto)
        print("\nProduto excluído com sucesso!\n")
    else:
        print("\nAção de exclusão cancelada.\n")
        listar_produtos(inventario)

def buscar_produto(inventario):
    #Mostra os detalhes de um produto pelo ID ou parte do nome.
    if not inventario:
        print("\nO inventário está vazio. Não há produtos para buscar.\n")
        return

    criterio = input("\nDeseja buscar por ID ou Nome? (id/nome): ").lower()
    if criterio == "id":
        id_produto = input("Informe o ID do produto: ")
        produto = next((p for p in inventario if p["id"] == id_produto), None)
    elif criterio == "nome":
        nome_produto = input("Informe parte do nome do produto: ").lower()
        produto = next((p for p in inventario if nome_produto in p["nome"].lower()), None)
    else:
        print("Critério inválido. Escolha 'id' ou 'nome'.\n")
        return

    if produto:
        print("\nProduto encontrado:")
        print(f"ID: {produto['id']}\nNome: {produto['nome']}\nCategoria: {produto['categoria']}\nQuantidade: {produto['quantidade']}\n Preço: {produto['preco']:.2f}\n")
    else:
        print("\nProduto não encontrado.\n")

# Inicia o inventário vazio.
inventario = []


adicionar_produto(inventario)
adicionar_produto(inventario)
adicionar_produto(inventario)
listar_produtos(inventario)
atualizar_produto(inventario)
excluir_produto(inventario)
buscar_produto(inventario)
listar_produtos(inventario)