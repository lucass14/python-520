

def receber_inteiro(mensagem):
 	valor = input(mensagem)
 	if valor.isnumeric():
 		return valor 
 	print('numero invalido')
 	exit()

def receber_inteiro2(mensagem):
 	valor = input(mensagem)
 	while not valor.isnumeric():
 		print('numero invalido')
 		valor = input(mensagem)
 	return valor

usuario = {
        'nome' : input('digite seu nome:'),
        'idade': receber_inteiro2('digite sua idade:'),
        'peso': receber_inteiro2('digite seu peso:')
}		
