usuario = {
  'nome': 'belzebu',
  'email': 'bel@zebu',
  'idade': 5000
 }

condicao = 10 > 50
if condicao:
	print('verdade')
else:
	print ('falso')


# ex3 dado o usuario acima ,
# se a idade dele dividada pr 5 
# for maior do que 1200
#imprimir "voce e velho"

# ex4 se o email do usuario acima
#nao conter uma'@' imprimir email
# invalido

if (usuario['idade']/5)>1200:
	print('voce e velho')
else:
	print('voce e jovem')
