import random
from operacoesbd import *
from operacoesbd import criarConexao
from operacoesbd import listarBancoDados
from operacoesbd import insertNoBancoDados
from operacoesbd import atualizarBancoDados
from operacoesbd import encerrarBancoDados 

#Crio conexão com o Banco de Dados.
con = criarConexao('127.0.0.1','root','19253132Du','ouvidoria_py')
#faço uma consulta de todos os dados Inseridos
ListaManif = listarBancoDados(con, 'SELECT * FROM ouvidoria_py')
listaProtocolo = listarBancoDados(con, 'SELECT PROTOCOLO FROM ouvidoria_py')
VoltarMenu = 0
opcao = 0
tipoManifestacao = ["Reclamação", "Sugestão", "Elogio", "Denuncia"]

while opcao != 7:
    print(30 * "-=")
    print("Bem-vindo ao Sistema de Ouvidoria da UniPY\n")
    print("Menu:\n")
    print("1. Criar nova manifestação")
    print("2. Listar manifestações")
    print("3. Listar Manifestação por tipo")
    print("4. Exibir quantidade de manifestações")
    print("5. Pesquisar uma manifestação por código")
    print("6. Excluir uma manifestação pelo código")
    print("7. Sair")
    print(30 * "-=")

    opcao = input("\nEscolha uma opção: ")
    if opcao.isdigit():
        opcao = int(opcao)

    if opcao == 1:
        print("\n1 - Reclamação\n2 - Sugestão\n3 - Elogio\n4 - Denuncia\n5 - Voltar ao menu")
        while True:
            n = input("\nEscolha uma opção (1-4): ")
            if n.isdigit():
                n = int(n)
                if n >= 1 and n <= 5:
                    break
                else:
                    print("Por favor, insira um número válido entre 1 e 4.")
            else:
                print("Por favor, insira um número válido entre 1 e 4.")

        if n != 5:
            NovaManif = input(f"\nDigite sua {tipoManifestacao[n - 1]}: ")
            protocolo_valido = False
            while not protocolo_valido:
                protocolo = random.randint(100, 999)
                if protocolo not in listaProtocolo:
                    protocolo_valido = True
                    consultaInsert = 'INSERT INTO ouvidoria_py (PROTOCOLO, TIPO_MANIFESTAÇÃO, MANIFESTAÇÃO) VALUES(%s, %s, %s)'
                    dados = [protocolo, tipoManifestacao[n - 1], NovaManif]
                    insertNoBancoDados(con, consultaInsert, dados)
                    print(f"\nSua Manifestação foi salva com sucesso!!\nSeu número de protocolo: {protocolo}")
                    break
        VoltarMenu = 0
        while VoltarMenu != 1:
            VoltarMenu = int(input("Deseja voltar ao Menu? digite 1: "))

    elif opcao == 2:
        consultarDados = 'SELECT * FROM ouvidoria_py'
        Listar = listarBancoDados(con, consultarDados)
        if len(Listar) > 0:
            print("\nA seguir estão os protocolos e as manifestações\n")
            print(30 * '-/=', "\n")
            for i in Listar:
                print(f"Protocolo: {i[0]}\nTipo de Manifestação: {i[1]}\nManifestação: {i[2]}\n")
                print(30 * "-=")
        else:
            print("Não há nenhuma manifestação no sistema.")
        VoltarMenu = 0
        while VoltarMenu != 1:
            VoltarMenu = int(input("Deseja voltar ao Menu? digite 1: "))

    if opcao == 3:
        print("Escolha um tipo de manifestação que deseja listar:")
        print("\n1 - Reclamação\n2 - Sugestão\n3 - Elogio\n4 - Denuncia \n5 - Voltar ao menu")
        while True:
            op = int(input("\nEscolha uma opção (1-4): "))
            if op >=1 and op <=5:
                break
            else:
                print("Por favor, insira um número válido entre 1 e 4.")
        if op != 5:
            listTipo = listarBancoDados(con,'SELECT * FROM ouvidoria_py WHERE TIPO_MANIFESTAÇÃO =' + "'" + tipoManifestacao [op -1] + "'")
            if len(listTipo) > 0:
                for manifestacao in listTipo:
                    print(30 * "-=")
                    print("Protocolo:", manifestacao[0], "\nTipo de Manifestação:", manifestacao[1], "\nManifestacao: ",manifestacao[2])
            else:
                print(30 * "-=")
                print("Não há mais manifestações em aberto")
        VoltarMenu = 0
        while VoltarMenu != 1:
            VoltarMenu = int(input("Deseja voltar ao Menu? digite 1: "))

    elif opcao == 4:
        if len(ListaManif) > 0:
            print(f"Você tem {len(ListaManif)} manifestações no sistema.")
        else:
            print(f"Não há nenhuma manifestação no sistema.")
        VoltarMenu = 0
        while VoltarMenu != 1:
            VoltarMenu = int(input("Deseja voltar ao Menu? digite 1: "))

    elif opcao == 5:
        listar = "SELECT * FROM ouvidoria_py"
        ListaManif = listarBancoDados(con, listar)
        protocolo = int(input("Digite o protocolo da Manifestação desejada: "))
        protocolo_encontrado = False
        if len(ListaManif) != 0:
            for i in ListaManif:
                ListaManif = listarBancoDados(con, 'SELECT PROTOCOLO FROM ouvidoria_py')
                if protocolo == i[0]:
                    protocolo_encontrado = True
                    print(30 * "-=")
                    print(f"Manifestação Encontrada!!\n\nProtocolo: {i[0]}\nTipo: {i[1]}\nManifestação: {i[2]}")
                    break
            if not protocolo_encontrado:
                print("Protocolo Inexistente!!")
        else:
            print("Não existe nenhuma manifestação!!")
        VoltarMenu = 0
        while VoltarMenu != 1:
            VoltarMenu = int(input("Deseja voltar ao Menu? digite 1: "))

    elif opcao == 6:
        consultarDados = 'SELECT * FROM ouvidoria_py'
        Listar = listarBancoDados(con, consultarDados)
        if len(Listar) > 0:
            print("\nA seguir estão os protocolos e as manifestações\n")
            print(30 * '-=', "\n")
            for i in Listar:
                print(f"Protocolo: {i[0]}\nTipo de Manifestação: {i[1]}\nManifestação: {i[2]}\n")
                print(30 * "-=")
                
            protocolo = input("Digite o Protocolo da Manifestação que deseja Excluir: ")
            if protocolo.isdigit():
                protocolo = int(protocolo)
                protocolo_encontrado = False
                if len(ListaManif) > 0:
                    for i in ListaManif:
                        protocolo_encontrado = True
                        excluirBancoDados = 'DELETE FROM ouvidoria_py WHERE PROTOCOLO = (%s)'
                        dados = [protocolo]
                        atualizarBancoDados(con, excluirBancoDados, dados)
                        print(30 * "-=")
                        print(f"Manifestação de Número: {protocolo} Removida com Sucesso!!")
                        print(30 * "-=")
                        break
            else:
                print("Por Favor, digite um procotolo Valido!!")
        else:
            print("Não há nenhuma manifestação no sistema.")
        VoltarMenu = 0
        while VoltarMenu != 1:
            VoltarMenu = int(input("Deseja voltar ao Menu? digite 1: "))
            
    elif opcao != 7:
        print(f"{30 * '-='}\n")
        print("Opção invalida, tente novamente")

print(f"{30 * '-='}\n")
print(f"Saindo do sistema")
print(f"\nObrigado por usar Nossa Ouvidoria!!")

encerrarBancoDados(con)