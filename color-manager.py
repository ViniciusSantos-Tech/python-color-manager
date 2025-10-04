print("Aperte 1 para adicionar tarefa")
print("Aperte 2 para ver tarefas")
print("Aperte 3 para sair")
Lista = ["Azul", "Verde", "Amarelo"]
Sistema = True
while Sistema == True:
    Escolha = int(input("Escola a opçao: "))
    if Escolha == 1:
       Novo_item = input("Adicione uma cor: ")
       Lista.append(Novo_item)
       print(f"{Novo_item} adicionado")
    elif Escolha == 2:
       print(f" Aqui esta a lista {Lista}")
       print("Obrigado por ver a lista")
    elif Escolha == 3:
       print("Voce saiu")
       Sistema = False
    else:
       print("Escolha apenas 1, 2 ou 3")
    

#Sistema de Gerenciamento de cores!!
# Meu terceiro projeto na vida
#Feito por Vinicius Santos.
