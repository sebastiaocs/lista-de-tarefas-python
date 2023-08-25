import redis

db = redis.Redis(host='localhost', decode_responses=True)

class ListaDeTarefas:
	
	def adicionarTarefa(self, descricao):		
		id = self.verificarEControlarChaves()	
		print(id)
		db.set(id, descricao)		
		
	def verificarEControlarChaves(self):
		chaves = db.keys()
		if not chaves:
			return 1
		else:
			proximoId = max(chaves, key=int)
			proximoId = int(proximoId)
			proximoId += 1
			return (str(proximoId))
			
	def listarTarefas(self):
		chaves = db.keys()
		if not chaves:
			print("\nNÃO HÁ TAREFAS NA LISTA!")
		else:
			chaves = list(map(int, chaves))		
			chaves = sorted(chaves)
			chaves = list(map(str, chaves))
			print("\nID ---- DESCRIÇÃO-------------\n")
			for i in range(len(chaves)):
				print(chaves[i]+"        "+ db.get(chaves[i]))	
		
	def removerTarefa(self, id):
		db.delete(id)

	def menu_principal(self):
	    print('\n----------MENU PRINCIPAL----------\n')
	    print('(1) Adicionar Tarefa')
	    print('(2) Listar Tarefas')
	    print('(3) Remover Tarefa')
	    print('(0) Sair')
		
	    