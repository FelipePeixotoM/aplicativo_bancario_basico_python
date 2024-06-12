saldo_conta = 0
LIMITE_SAQUES = 500
extrato = []
numero_de_saques = 0
NUMERO_LIMITE_DE_SAQUES = 3

menu_intro = 'Bem-vindo ao sistema bancario: Digite uma gas seguintes opções para seguir:'
menu_opcoes = '[D]epositar, [S]aque, [E]xtrato, [Q] para sair: '


while(True):
    print(menu_intro)
    opcao_cliente = input(menu_opcoes).lower()
    
    if opcao_cliente == 'd':
        quantidade_do_deposito = input("Quanto estara depositando: ")
        quantidade_do_deposito_float = float(quantidade_do_deposito)
        if quantidade_do_deposito_float > 0:
            extrato.append(f'+ R${quantidade_do_deposito_float:.2f}')
            saldo_conta += quantidade_do_deposito_float
            print('Deposito concluido, voltando ao inicio')
        else:
            print('O deposito não é valido, por favor realize novalmente o deposito.')
            continue
    
    elif opcao_cliente == 's':
        quantidade_do_saque = input('Quanto gostaria de sacar: ')
        quantidade_do_saque_float = float(quantidade_do_saque)

        excedeu_saldo = quantidade_do_saque_float > saldo_conta
        excedeu_numero_de_saques = numero_de_saques == NUMERO_LIMITE_DE_SAQUES
        excedeu_limite = quantidade_do_saque_float > LIMITE_SAQUES
        
        if excedeu_saldo:
            print('O saque é maior que seu saldo no momento')
        elif excedeu_numero_de_saques:
            print(f'Numero de saques permitidos {numero_de_saques} foi excedido, volte amanha ou entre em contato com sua agencia.')
        elif excedeu_limite:
            print('O saque excedeu o limite de saque')
        elif quantidade_do_saque_float > 0:
            extrato.append(f'- R${quantidade_do_saque_float:.2f}')
            saldo_conta -= quantidade_do_saque_float
            numero_de_saques += 1
            print('Saque concluido, voltando ao inicio')
        else:
            print('O saque não é valido ou valor insuficiente no saldo, por favor realize novalmente o saque.')
            continue
    
    elif opcao_cliente == 'e':
        print((25 * '=') + 'Extrato' + (25 * '='))
        if len(extrato) == 0:
            print('não foram realizadas movimentações')
            print(57 * '=')
            continue
        for i in range(len(extrato)):
            print(extrato[i])
        print(f'Seu total é R${saldo_conta:.2f}')
        print(57 * '=')

    elif opcao_cliente == 'q':
        print('Saindo do sistema bancario, obrigado por usalo.')
        break
    
    else:
        print('Comando invalido, por favor selecione uma das opções validas')

        

