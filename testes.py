from funcoes import aguardar, limparTela

while True:
    limparTela()
    print("(0) Sair")
    print("(1) incluir aluno")
    print("(2) Mostrar lista")

    opcao = input()
    if opcao == "0":
        break
    elif opcao == "1":
        nome = input("Nome:")
        email = input("Email :")
        print('Aluno incluido!')
        aguardar(2)
        arquivo = open("bd.atitus","w") # w write # r read #
        arquivo.write(nome+" + "+email+"\n")
        arquivo.close()

    elif opcao == "2":
        try:
            arquivo = open("bd.atitus","r")
            dados = arquivo.read()
            print(dados)
            arquivo.close()
            aguardar(5)
        except:
            print('banco de dados não localizado eitaaaaa')
            arquivo = open('bd.atitus')
            arquivo.close()


    else:
        print("inválido!")
        aguardar(2)
    