from listaDeTarefas import *

lista = ListaDeTarefas()
x = 10

while 1:  	 
	lista.menu_principal()
	op = int(input("\nEscolha uma opção: "))
	if(op == 0):
		break
	elif(op == 1):
		lista.adicionarTarefa(input("Adicione uma descrição: "))
	elif(op == 2):
		lista.listarTarefas()
	elif(op == 3):
		id = input("Informe o ID: ")
		lista.removerTarefa(id)
	else:
		print("Opção inválida!")
