def adicionar_tarefa(tarefas, nome_tarefa):
    """Adiciona uma nova tarefa com status pendente à lista."""
    tarefa = {"tarefa": nome_tarefa, "completada": False} # como estamos inserindo, sempre é falso
    tarefas.append(tarefa) #Poderia escrever a linha de cima aqui(), sem criar a variavel
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return #não faz diferença aqui, mas é importante manter

def ver_tarefas(tarefas):
    print("\nLista de tarefas: ")
    for indice, tarefa in enumerate(tarefas, start=1): #start=1 para começar por 1 e não 0
        status = "✔️  " if tarefa["completada"] else " " #facilitando entendimento do usuário
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
        #aqui não pode haver return, porque precisa continuar adicionando tarefas

def atualizar_tarefa(tarefa, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = indice_tarefa - 1 #para pegar corretamente a tarefa, que muda o indice por conta do start=1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else:
        print("Número da tarefa inválido, tente novamente.")
    return

def completar_tarefa(tarefas, indice_tarefa):
     indice_tarefa_ajustado = indice_tarefa - 1
     tarefas[indice_tarefa_ajustado]["completada"] = True
     print(f"\nTarefa {indice_tarefa} completada com sucesso!")
     return

def deletar_tarefas_completadas(tarefas):
     for tarefa in tarefas:
          if tarefa["completada"]: #ou == True: também da certo
               tarefas.remove(tarefa)
     print("As tarefas completadas foram deletadas!")
     return

tarefas = []
while True:
    print("\nMeu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")
    if escolha == "1":
        nome_tarefa = input("Digite o nome da nova tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)

    elif escolha == "2":
        ver_tarefas(tarefas)

    elif escolha == "3":
            ver_tarefas(tarefas)
            indice_tarefa = int(input("Digite o número da tarefa que deseja atualizar: "))
            novo_nome = input("Digite o novo nome da tarefa: ")
            atualizar_tarefa(tarefas, indice_tarefa, novo_nome)

    elif escolha == "4":
            ver_tarefas(tarefas)
            indice_tarefa = int(input("Digite o número da tarefa que deseja completar: "))
            completar_tarefa(tarefas, indice_tarefa)

    elif escolha == "5":
         deletar_tarefas_completadas(tarefas)
         ver_tarefas(tarefas)

    elif escolha == "6":
        break

print("Sessão finalizada!")
