import os
menu = ""

def bemvindo(menu):
	os.system('cls')
	print("Bem Vindo a Agenda")
	print("Selecione uma Opcao:")
	print("1 - Adicionar um novo contato")
	print("2 - Remover um contato")
	print("3 - Buscar por um contato")
	print("4 - Listar todos os contatos")
	print("0 - Para sair")
	menu = input("Opção: ")
	return menu

def buscar():
	os.system('cls')
	print("Busca um contato")
	nome = input("Digite o nome ou telefone do contato que deseja visualizar: ")
	agenda = open("agendatelefonica.csv", 'r')
	count = 0
	for linha in agenda:
		linha.rstrip()
		if nome in linha:
			print(linha)
			count += 1
	print("Foram encontrados",count,"contatos.")
	agenda.close()
	voltar()
	
	
#Função pra adicionar novos contatos na agenda
def adicionar():
	os.system('cls')
	print("Adicionar um registro")
	agenda = open("agendatelefonica.csv",'a')
	nome = input("Nome do Contato:")
	telefone = input("Digite o telefone:")
	print("Contato salvo com nome:",nome,"e numero",telefone)
	agenda.write(nome)
	agenda.write(" - ")
	agenda.write(telefone)
	agenda.write(",")
	agenda.write("\n")
	agenda.close()
	voltar()	
	
def listar():
	count = 0
	os.system('cls')
	print("Lista de Contatos:")
	agenda = open("agendatelefonica.csv", "r")
	for i, linha in enumerate(agenda):
		linha = linha.rstrip()
		print (str(i)+".",linha)
		count += 1
	agenda.close()
	print("\n"+str(count)+" contatos encontrados.")	
	voltar()

def falha():
	print("Opcao Inválida!")

def voltar():
	print("\n")
	opcao = input("Deseja voltar ao menu? s/n : ")
	if(opcao == "s"):
		os.system('cls')
		return 0
	elif(opcao == "n"):
		print("Obrigado por utilizar nosso sistema!")
		exit()
	else:
		falha()
		voltar()
