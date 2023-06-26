def procure_pela_chave(caixa_principal):
    pilha = main_box.crie_uma_pilha_para_busca()
    while pilha is not vazia:
        caixa = pilha.pegue_caixa()
        for item in caixa:
            if item.e_uma_caixa():
                pilha.append(item)
            elif item.e_uma_chave():
                print('Achei a chave!')

# Utilizando Recursão

def procure_pela_chave(caixa):
    for item in caixa:
        if item.e_uma_caixa():
            procure_pela_chave(item)  # a função chama a si mesma
        elif item.e_uma_chave():
            print('Achei a chave!')

# Caso-base e caso recursivo

    # A função recursiva deve informar quando a recursão deve parar (para não ficar infinito)

    # Toda função recursiva tem 2 partes: o caso-base (quando não chama a si mesma novamente),
                                        # o caso recursivo ( chama a si mesma)

    # Ex:

def regressiva(i):
    print (i)
    if i <= 1:  # caso-base
        return
    else:  # caso recursivo
        regressiva(i-1)

# Pilha de chamada

    # seta a variável nome na memoria, Função sauda - nome: Maggie
    # função sauda2 nome: Maggie, aloca mais uma caixa de memória para essa chamada

def sauda(nome):
    print('Olá' + nome +'!')
    sauda2(nome)
    print('preparando para dizer tchau...')
    tchau()

def sauda2(nome):
    print('Como vai ' + nome + '?')

def tchau():
    print('ok, tchau!')

# Pilha de chamada com recursão

def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x-1)