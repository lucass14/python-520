string = 'lucas'
inteiro = 21
flutuante = 150000.92
booleando = True

# estrutura de dados 

tupla =(1,2,3,4)
lista = [1,2,3,4]
dicionario ={ 
'nome':'lucas', 'idade' : 21
}
 # nome = input ('digite seu nome ')

  # ex1 : criar uma estrutura  que armazena :
  # - nome ,idade,email,sexo,altura,peso

usuario = {}

nome = input ('digite seu nome ')
idade = input ('digite sua idade')
email = input('digite seu email')
sexo = input ('digites seu sexo')
altura = input ('digite sua altura')
peso = input ('digite seu peso')

usuario= {
	'nome': nome,
	'idade':idade,
	'email':email,
	'sexo':sexo,
	'altura':altura,
	'peso':peso


}
print(usuario)

 # ex2 : imprimir no terminal somente 
 # o nome e a idade digitadas 

nome = usuario['nome']
idade = usuario['idade']
print(nome + ' ' + idade)
