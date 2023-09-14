if __name__ == '__main__' :

    produtosDisponiveis = ['Leite', 'Maçã', 'Nescal', 'Café', 'Presunto', 'Queijo', 'Pão']
    listaProdutos = []
    produto = None

    
    print('Produtos disponíveis.')
    print(sorted(produtosDisponiveis))

    while True:
        produto = input(f'Digite o produto que dseja: (Digite 0 para finalizar)')
        
        if produto == '0':
            break

        if produto in produtosDisponiveis:
            listaProdutos.append(produto)
        else: 
            print(f'O produto {produto} não está disponível.')


    print('Produtos comprados.')
    print(listaProdutos)