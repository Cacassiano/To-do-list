#bibliotecas
import time 
#obs: time.sleep() == espera(numero de segundos)
import os 
#obs: os.system("cls") == limpa telinha do terminal
def finalizar():
    print("*finalizou*")
def atualizarTarefas(todasAsTarefas):
    os.system("cls")
    while True:
            if not todasAsTarefas:
                print("A lista está vazia")
                saida = input("Pressione Enter para voltar ao painel principal...")
                break
            try:
                print("\n\tTODAS AS TAREFAS")
                for t in range(len(todasAsTarefas)):
                    print("tarefa %d - %s"% (t+1,todasAsTarefas[t]["titulo"]))
                interaçao= int(input("\nSe quiser atualizar/mudarr os elemntos de alguma das tarefas acima\nDigite o numero correspondente a Tarefa desejada.\nCaso queira voltar painel principal digite 0\nInsira aqui: "))
                os.system("cls")
                if interaçao == 0:
                    while True:
                        try:
                            confirmação = str(input("Tem certeza que que deseja sair?(s/n) "))
                            os.system("cls")
                            if confirmação == 'n':
                                break
                            elif confirmação == 's':
                                print("Certo. Voltando ao panel principal", end="")
                                x = 0
                                while x <= 3:
                                    print(".", end="")
                                    time.sleep(1)
                                    x += 1
                                os.system("cls")
                                break
                        except ValueError:
                            print("Você escreveu caracteres invalidos. Lembre-se só é permitido os caracteres 's' 'n'.\nAgora tente novamente.")
                            continue
                        except:
                            print("ocorreu um erro. Tente novamente.")
                            continue
                        break
                    if confirmação == 'n':
                        continue
                elif interaçao != 0:
                    os.system("cls")
                    mudei = False
                    while True:
                        try:
                            print("1- Titulo: %s\n2- Status da tarefa: %s\n3- Data limite para tarefa: %s\n4- Descrissão: %s\n"% (todasAsTarefas[interaçao-1]['titulo'],todasAsTarefas[interaçao-1]['status'],todasAsTarefas[interaçao-1]['datalimite'],todasAsTarefas[interaçao-1]['descrissao']))    
                            try:    
                                atualizaçao = input("Digite o numero correspondente ao elemento que quer mudar\nOu o numero 0 para voltar ao menu\nDigite aqui: ")
                                if int(atualizaçao) == 0:
                                    os.system('cls')
                                    break
                                confirmaçãoDeAtualizaçao = input("Deseja mesmo fazer uma atualização no elemento selecionado(s/n)? ")
                                if confirmaçãoDeAtualizaçao == 'n':
                                    os.system('cls')
                                    print("Certo. voltando ao começo")
                                    time.sleep(2)
                                    continue
                                elif confirmaçãoDeAtualizaçao == 's':
                                    print("Certo. Agora prossiga.")
                                    time.sleep(2)
                                os.system("cls")
                                if int(atualizaçao) == 1:
                                    os.system('cls')
                                    mudança = str(input("Digite aqui a substituição: "))
                                    os.system('cls')
                                    print("Titulo: \"%s\" foi substituido com sucesso por Titulo: \"%s\""% (todasAsTarefas[interaçao-1]['titulo'],mudança))
                                    todasAsTarefas[interaçao-1]['titulo'] = mudança
                                    saida = input("Pressione Enter para voltar ao painel principal...")
                                    mudei = True
                                    break
                                elif int(atualizaçao) == 2:
                                    os.system('cls')
                                    while True:
                                        try:
                                            mudança = str(input("digite 'p' para marcar tarefa como pendente, ou digite 'f' para marcar tarefa como feita: "))
                                            if mudança == 'p':
                                                mudança = "Pendente"
                                                todasAsTarefas[interaçao-1]['status'] = mudança
                                                os.system('cls')
                                                print("Status \"%s\" foi substituido com sucesso por Status \"%s\""% (todasAsTarefas[interaçao-1]['titulo'],mudança))
                                                saida
                                                mudei = True
                                                break
                                            elif mudança == 'f':
                                                mudança = "Feita"
                                                todasAsTarefas[interaçao-1]['status'] = mudança
                                                print("Status \"%s\" foi substituido com sucesso por Status \"%s\""% (todasAsTarefas[interaçao-1]['titulo'],mudança))
                                                saida = input("Pressione Enter para voltar ao painel principal...") 
                                                mudei = True
                                                os.system('cls')
                                                break
                                            else:
                                                os.system("cls")
                                                print("Você só pode escrever ou 'p' ou 'f'. Agora tente novamente.")
                                                continue
                                        except:
                                            os.system('cls')
                                            print("ocorreu um erro. Tente novamente.")
                                            continue
                                elif int(atualizaçao) == 3:
                                    os.system('cls')
                                    mudança = str(input("Digite aqui a substituição: "))
                                    os.system('cls')
                                    print("Data limite: \"%s\" foi substituido com sucesso por Data limite: \"%s\""% (todasAsTarefas[interaçao-1]['titulo'],atualizaçao))
                                    todasAsTarefas[interaçao-1]['datalimite'] = mudança
                                    saida = input("Pressione Enter para voltar ao painel principal...")
                                    mudei = True
                                    break
                                elif int(atualizaçao) == 4:
                                    os.system('cls')
                                    mudança = str(input("Digite aqui a substituição: "))
                                    os.system('cls')
                                    print("Descrissao: \"%s\" foi substituido com sucesso por descrissao: \"%s\""% (todasAsTarefas[interaçao-1]['titulo'],mudança))
                                    todasAsTarefas[interaçao-1]['descrissao'] = mudança
                                    saida = input("Pressione Enter para voltar ao painel principal...")
                                    mudei = True
                                    break
                                if mudei == True:
                                    os.system('cls')
                                    break
                                else:
                                    os.system('cls')
                                    continue
                            except:
                                os.system("cls")
                                print("Escreva apenas numeros.")
                                time.sleep(2)
                                continue        
                        except IndexError:
                            print("\nEste elemento não existe. Tente novamente.")
                            time.sleep(1)
                            break
                    if atualizaçao == 0:
                        os.system('cls')
                        break
            except ValueError:
                print("\nSó é possivel escrever números. Tente novemente.")
                time.sleep(1)
                continue
            
            break
def removerTarefas(todasAsTarefas):
    os.system("cls")
    while True:
            if not todasAsTarefas:
                print("A lista está vazia")
                saida = input("Pressione Enter para voltar ao painel principal...")
                break
            try:
                print("\n\tTODAS AS TAREFAS")
                for t in range(len(todasAsTarefas)):
                    print("tarefa %d - %s"% (t+1,todasAsTarefas[t]["titulo"]))
                interaçao= int(input("\nSe quiser deletar alguma das tarefas acima\nDigite o numero correspondente a Tarefa desejada.\nCaso queira voltar painel principal digite 0\nInsira aqui: "))
                os.system("cls")
                if interaçao == 0:
                    while True:
                        try:
                            confirmação = str(input("Tem certeza que que deseja sair?(s/n) "))
                            os.system("cls")
                            if confirmação == 'n':
                                break
                            elif confirmação == 's':
                                print("Certo. Voltando ao panel principal", end="")
                                x = 0
                                while x <= 3:
                                    print(".", end="")
                                    time.sleep(1)
                                    x += 1
                                os.system("cls")
                                break
                        except ValueError:
                            print("Você escreveu caracteres invalidos. Lembre-se só é permitido os caracteres 's' 'n'.\nAgora tente novamente.")
                            continue
                        except:
                            print("ocorreu um erro. Tente novamente.")
                            continue
                        break
                    if confirmação == 'n':
                        continue
                elif interaçao != 0:
                    os.system("cls")
                    try:
                        print("\t%s\nStatus da tarefa: %s\nData limite para tarefa: %s\nDescrissão: %s\n"% (todasAsTarefas[interaçao-1]['titulo'],todasAsTarefas[interaçao-1]['status'],todasAsTarefas[interaçao-1]['datalimite'],todasAsTarefas[interaçao-1]['descrissao']))
                        while True:
                            confirmaçãoDeDeleçao = input("Deseja mesmo deletar esta tarefa(s/n)? ")
                            if confirmaçãoDeDeleçao == 'n':
                                os.system('cls')
                                print("Certo. voltando ao começo")
                                time.sleep(2)
                                break
                            elif confirmaçãoDeDeleçao == 's':
                                print("Tarefa deletada.")
                                del todasAsTarefas[interaçao-1]
                                pausa = input("Pressione enter para voltar ao começo")
                                break
                        os.system("cls")
                        continue
                    except:
                        print("\nEste elemento não existe. Tente novamente.")
                        time.sleep(1)
                        continue
            except ValueError:
                print("\nSó é possivel escrever números. Tente novemente.")
                time.sleep(1)
                continue
            except: 
                print("Erro. Por favor, tente novamente.")
                time.sleep(1)
                continue
            break
def adicionarTarefa(todasAsTarefas):
    os.system("cls")
    while True:
        try:
            interaçao = int(input("Para adicionar uma tarefa, digite 1\nCaso queira voltar ao painel principal,digite 0\nDigite aqui: "))
            os.system('cls')
            if interaçao == 0:
                while True:
                    try:
                        confirmaçao = str(input("Tem certeza que que deseja voltar ao menu principal?(s/n) "))
                        if confirmaçao == 'n':
                            print("ok. Tente novamente.")
                            break      
                        elif confirmaçao != 's':
                            print("Escreva apenas os carateres 's' ou 'n'.") 
                            continue
                        else:
                            print("Certo. Voltando ao panel principal", end="")
                            x = 0
                            while x <= 3:
                                print(".", end="")
                                time.sleep(1)
                                x += 1
                            os.system("cls")
                            break   
                    except ValueError:
                        print("Escreva apenas os carateres 's' ou 'n'.")
                        continue
                    except:
                        print("Ocorreu um erro. Refazendo confirmação.")
                        continue
                if confirmaçao == 'n':
                    continue
            elif interaçao == 1:
                while True:
                    titulo = input("Digite aqui o titulo desta tarefa: ")
                    os.system('cls')
                    while True:
                        try:
                            status = input("digite 'p' para marcar tarefa como pendente, ou digite 'f' para marcar tarefa como feita: ")
                            if status == 'p':
                                status = "Pendente"
                                break
                            elif status == 'f':
                                status = "Feita"
                                break
                            else:
                                os.system("cls")
                                print("Você só pode escrever ou 'p' ou 'f'. Agora tente novamente.")
                                continue
                            os.system('cls')
                        except:
                            print("ocorreu um erro. Tente novamente.")
                            continue
                    dataLimite = input("Digite aqui a data limite para a finalização desta tarefa(caso seja algo rotineiro apenas escreva \"Rotina\"): ")
                    os.system('cls')
                    descrissao = input("Digite aqui uma breve descrissão desta tarefa: ")
                    os.system('cls')
                    print("titulo: %s,  status: %s, data limite: %s, descrissao: %s "% (titulo,status,dataLimite,descrissao))
                    confirmaçao = input("Tem certeza de que deseja adicionar uma tarefa com a informações acima(s/n)? ")
                    os.system('cls')
                    if confirmaçao == 'n':
                        print("Ok. Preencha os campos novamente")
                        continue
                    elif confirmaçao == 's':
                        os.system("cls")
                        print("Certo. Criando tarefa.", end="")
                        todasAsTarefas.append(dict(titulo = titulo,status = status,datalimite = dataLimite,descrissao = descrissao))
                        for e in range(3):
                            time.sleep(1)
                            print(".", end="")
                        print("Pronto! Sua tarefa foi criada.")
                        espera = input("Pressione enter para voltar ao painel principal: ")
                        break
            else:
                print("Você inseriu caracteres invalidos.")
                time.sleep(3)
                os.system('cls')
                print("Lembre-se: use ou '0' ou '1'")
                continue
        except ValueError:
            os.system('cls')
            print("Só aceitamos os numeros 1 e 0 como resposta. Tente novamente.")
            continue
        except:
            os.system('cls')
            print("Aconteceu um erro. Tente novamente.")
            continue
        break
def listandoTodas(Tarefas,especificaçao:str):
    vazia = 1
    os.system("cls")
    while True:
        try:
            print("\n\tTODAS AS TAREFAS %s"% especificaçao)
            X = 1
            for t in range(len(Tarefas)):
                if especificaçao == "PENDENTES" and Tarefas[t]['status'] == "Pendente":
                    print("tarefa %d - %s"% (X,Tarefas[t]["titulo"]))
                    vazia = 0
                    X += 1
                elif especificaçao == "FEITAS" and Tarefas[t]['status'] == "Feita":
                    print("tarefa %d - %s"% (X,Tarefas[t]["titulo"]))
                    vazia = 0
                    X += 1
                elif especificaçao == "":
                    print("tarefa %d - %s"% (t+1,Tarefas[t]["titulo"]))
                    vazia = 0
            if vazia == 1:
                print("A lista está vazia")
                saida = input("Pressione Enter para voltar ao painel principal...")
                break
            interaçao= int(input("\nSe quiser ver mais detalhes sobre alguma das tarefas acima\nDigite o numero correspondente a Tarefa desejada.\nCaso queira voltar painel principal digite 0\nInsira aqui: "))
            os.system("cls")
            if interaçao == 0:
                while True:
                    try:
                        confirmação = str(input("Tem certeza que que deseja sair?(s/n) "))
                        os.system("cls")
                        if confirmação == 'n':
                            break
                        elif confirmação == 's':
                            print("Certo. Voltando ao panel principal", end="")
                            x = 0
                            while x <= 3:
                                print(".", end="")
                                time.sleep(1)
                                x += 1
                            os.system("cls")
                            break
                    except ValueError:
                        print("Você escreveu caracteres invalidos. Lembre-se só é permitido os caracteres 's' 'n'.\nAgora tente novamente.")
                        continue
                    except:
                        print("ocorreu um erro. Tente novamente.")
                        continue
                    break
                if confirmação == 'n':
                    continue
            elif interaçao != 0:
                os.system("cls")
                try:
                    print("\t%s\nStatus da tarefa: %s\nData limite para tarefa: %s\nDescrissão: %s\n"% (Tarefas[interaçao-1]['titulo'],Tarefas[interaçao-1]['status'],Tarefas[interaçao-1]['datalimite'],Tarefas[interaçao-1]['descrissao']))
                    pausa = input("Pressione enter para voltar.")
                    os.system("cls")
                    continue
                except:
                    print("\nEste elemento não existe. Tente novamente.")
                    time.sleep(1)
                    continue
        except ValueError:
            os.system('cls')
            print("\nSó é possivel escrever números. Tente novemente.")
            time.sleep(1)
            continue
        except: 
            print("Erro. Por favor, tente novamente.")
            time.sleep(1)
            continue
        break
def painelPrincipal(Nome:str,todasAsTarefas):
    os.system("cls")
    print("\n\tLISTA DE AFAZERES")
    print("Seja bem vindo(a), %s. Como posso ajudar?" % Nome)
    while True:
        try:    
            interaçao = int(input("0-Sair do programa\n1-Ver todas as tarefas\n2-Ver apenas tarefas pendentes\n3-Ver apenas tarefas feitas\n4-adicionar nova tarefa\n5-Remover tarefa\n6-atualizar uma tarefa\nDigite aqui o numero correspondente à ação desejada: "))
            os.system("cls")
            if interaçao == 0:
                finalizar()
                break
            elif interaçao == 1:
                especificaçao = ""
                listandoTodas(todasAsTarefas,especificaçao)
            elif interaçao == 2:
                especificaçao = "PENDENTES"
                listandoTodas(todasAsTarefas,especificaçao)
            elif interaçao == 3:
                especificaçao = "FEITAS"
                listandoTodas(todasAsTarefas,especificaçao)
            elif interaçao == 4:
                adicionarTarefa(todasAsTarefas)
            elif interaçao == 5:
                removerTarefas(todasAsTarefas)
            elif interaçao == 6:
                atualizarTarefas(todasAsTarefas)
            else:
                os.system("cls")
                print("Ocorreu um erro. Por favor, tente novamente.")
                time.sleep(1)
                continue
        except ValueError:
            os.system("cls")
            print("Só é possivel escrever numeros neste campo. Por favor, tente novamente")
            time.sleep(1)  
            continue  
        os.system("cls")
        print("\nO que mais posso fazer por você?\n")
def inicializarPrograma():
    todasAsTarefas = []
    while True:
        nomeDeUsuario = input("Insira seu nome: ")
        os.system("cls")
        if not nomeDeUsuario:
            print("Nome invalido. Tente novamente")
            continue
        confirmaçao = input("Para confirmar que deseja ser chamado(a) pelo nome %s, digite \"s\".\nCaso contrario digite \"n\": " % nomeDeUsuario)
        if confirmaçao == 'n':
            print("Certo. Agora tente novamente.") 
            continue
        elif confirmaçao != 's':
            print("Erro ao realizar a confirmação. Recomeçando programa.")
            continue
        else:
            os.system("cls")
            painelPrincipal(nomeDeUsuario,todasAsTarefas)
            break
# chama a função e começa o programa
inicializarPrograma()