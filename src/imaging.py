#Elaborado por: 
#Vitor Fonseca
#Alexandre Pinto
#LEI

import Image,copy,random
#Funcao de abrir a imagem, em que  cria um ficheiro novo com o nome escolhido,(colocado com ou sem terminacao '.ppm').
#Leitura de algumas constantes(codificacao,quem fez,etc)
def abrir_imagem():
	ficheiro=''
	try:	
		while ficheiro=='':
			ficheiro=raw_input('Enter file name: ')
		if ficheiro[-4:]!='.ppm':
			imagem=open(ficheiro+'.ppm','r')
		else:
			imagem=open(ficheiro, 'r')
	except:
		print '\nFile does not exist.\n'
		return menu()
	codificacao=imagem.readline()
	programa=imagem.readline()
	tamanho=imagem.readline()
	profundidade=imagem.readline()
	tamanho=(str(tamanho)).split()
	global num_colunas, num_linhas, ori_colunas, ori_linhas, existe_imagem, matriz_da_imagem, matriz
	num_colunas=ori_colunas=int(tamanho[0])     #As variaveis comecadas por ori servem para termos os valores originais aquando da reposicao da imagem
	num_linhas=ori_linhas=int(tamanho[1])
	existe_imagem=True     #Booleano que verifica se esta alguma imagem carregada 
	#Definicao da matriz da imagem(3 dimensoes)
	matriz=[]
	for linha in range(num_linhas):
		matriz.append([])
		for coluna in range(num_colunas):
			matriz[linha].append([])
			for cor in range(3):
				matriz[linha][coluna].append([])
				matriz[linha][coluna][cor]=int(imagem.readline())
	matriz_da_imagem=copy.deepcopy(matriz)
	imagem.close()
	print '\n Image loaded correctly.\n'
	menu()
	
#Definicao que volta repor os valores originais na matriz que usamos durante todo o programa
def repor_imagem():	
	global matriz_da_imagem, matriz, num_colunas, num_linhas, ori_colunas, ori_linhas
	matriz_da_imagem=copy.deepcopy(matriz)
	num_colunas, num_linhas= ori_colunas, ori_linhas
	print '\n Original image replaced\n'
	mostra_imagem()
	
#Definicao que cria a imagem com o modulo Image e mostra a imagem
def mostra_imagem():
	imagem_apre=Image.new("RGB",(num_colunas,num_linhas))
	for linha in range(num_linhas):
		for coluna in range(num_colunas):
       			imagem_apre.putpixel((coluna,linha),(tuple(matriz_da_imagem[linha][coluna])))
	imagem_apre.show()
	menu()

#Definicao que permite a alteracao da cor de acordo com a escolha do utilizador
def altera_cor():
	cor=raw_input('Choose color: Red, Green or Blue? ')
	percen=-1
	while percen<0 or percen>200:
		percen=input('Knowing that 0% eliminates the specified color, 100% keeps it and 200% makes it double: \nChoose a percentage value (0-200): ')
	try:
		if cor=='Vermelho' or cor=='vermelho' or cor=='VERMELHO' or cor=='Red' or cor=='red':
			cor_alterar=0
		elif cor=='Verde' or cor=='verde' or cor=='VERDE' or cor=='Green' or cor=='green':
			cor_alterar=1
		elif cor=='Azul' or cor=='azul' or cor=='AZUL' or cor=='Blue' or cor=='blue':
			cor_alterar=2
	except:
		print '\n Invalid color.\n'
		return menu()
	#Altera o valor da cor
	for linha in range(num_linhas):
		for coluna in range(num_colunas):
			matriz_da_imagem[linha][coluna][cor_alterar]=int(matriz_da_imagem[linha][coluna][cor_alterar]*percen/100.0)
	print '\n Image was successfully changed.\n'	
	mostra_imagem()
	
#Definicao que faz a media dos valores das cores de cada pixel e atribui esta media as tres cores do mesmo pixel
def passagem_cinza():
	for linha in range(num_linhas):
		for coluna in range(num_colunas):
			media_pixeis=[(int(matriz_da_imagem[linha][coluna][0])+int(matriz_da_imagem[linha][coluna][1])+int(matriz_da_imagem[linha][coluna][2]))/3]*3
			matriz_da_imagem[linha][coluna]=media_pixeis
	print '\n Image was successfully changed.\n'	
	mostra_imagem()
	
#Definicao que inverte a imagem horizontal ou verticalmente de acordo com a opcao escolhida pelo utilizador	
def cria_reflexao(sentido):
	if sentido==1:
		for linha in range(num_linhas):
			matriz_da_imagem[linha]=matriz_da_imagem[linha][::-1]
	if sentido==2:
		matriz_da_imagem[:]=matriz_da_imagem[::-1]
	print '\n Image was successfully changed.\n'
	mostra_imagem()

#Definicao que calcula o negativo de cada pixel e altera-o de acordo com esse valor 
def cria_negativo():
	for linha in range(num_linhas):
		for coluna in range(num_colunas):
			matriz_da_imagem[linha][coluna][0]=255-matriz_da_imagem[linha][coluna][0]
			matriz_da_imagem[linha][coluna][1]=255-matriz_da_imagem[linha][coluna][1]
			matriz_da_imagem[linha][coluna][2]=255-matriz_da_imagem[linha][coluna][2]
	print '\n Image was successfully changed.\n'
	mostra_imagem()

#Definicao que roda a imagem para a direita
def rodar_90_direita():
	global matriz_da_imagem, num_colunas, num_linhas
	matriz_da_imagem[:]=matriz_da_imagem[::-1]
	matriz_da_imagem=zip(*matriz_da_imagem)
	matriz_da_imagem=[list(col) for col in matriz_da_imagem]
	num_colunas, num_linhas= num_linhas, num_colunas	
	print '\n Image was successfully changed.\n'	
	mostra_imagem()

#Definicao que roda a imagem agora para a esquerda
def rodar_90_esquerda():
	global matriz_da_imagem, num_colunas, num_linhas
	matriz_da_imagem=zip(*matriz_da_imagem)
	matriz_da_imagem=[list(col) for col in matriz_da_imagem]
	matriz_da_imagem[:]=matriz_da_imagem[::-1]
	num_colunas, num_linhas= num_linhas, num_colunas	
	print '\n Image was successfully changed.\n'	
	mostra_imagem()

#Definicao que roda 180 graus a imagem	
def rodar_180():
	global matriz_da_imagem
	matriz_da_imagem[:]=matriz_da_imagem[::-1]
	for linha in range(num_linhas):
		matriz_da_imagem[linha]=matriz_da_imagem[linha][::-1]
	print '\n Image was successfully changed.\n'	
	mostra_imagem()

#Definicao que cria uma moldura com a largura pretendida pelo utilizador
def moldura():
	global matriz_da_imagem, num_colunas, num_linhas
	try:
		tam=abs(int(input('Choose the width for the desired frame: ')))
	except:
		print '\n Invalid width! \n'
		return menu()
	nova_matriz=[]
	for linha in range(num_linhas+2*tam):
		nova_matriz.append([])
		for coluna in range(num_colunas+2*tam):
			nova_matriz[linha].append([])
			if (linha>=tam and linha<num_linhas+tam) and (coluna>=tam and coluna<num_colunas+tam):
				nova_matriz[linha][coluna]=matriz_da_imagem[(linha-tam)][(coluna-tam)]
		
			else:
				nova_matriz[linha][coluna]=[0,0,0]
	num_colunas, num_linhas= num_colunas+2*tam, num_linhas+2*tam
	matriz_da_imagem=copy.deepcopy(nova_matriz)
	nova_matriz=None
	print '\n Image was successfully changed.\n'
	mostra_imagem()

#Definicao que cria a nova imagem cortada de acordo com os limites escolhidos pelo utilizador
def cortar():
	try:
		global num_linhas, num_colunas, matriz_da_imagem
		print '\n Knowing that (0,0) is the upper left corner,'
		print ' The image has %d columns and %d lines' %(num_colunas, num_linhas)
		sup_esq=input(' Enter the new upper left corner coordinates (x,y): ')
		inf_dir=input(' Enter the new lower right corner coordinates (x,y): ')
		x_sup, y_sup=map(int, sup_esq)
		x_inf, y_inf=map(int, inf_dir)
	except:
		print'\n Invalid coordinates! \n'
		return menu()
	
	if x_sup<0 or y_sup<0 or x_inf<0 or y_inf < 0:
		print '\n Only non-negative values are allowed! \n'
		return menu()
	elif x_sup>num_colunas or y_sup>num_linhas or x_inf>num_colunas or y_inf>num_linhas:
		print '\n Coordinates bigger than image! \n'
		return menu()
	elif x_sup>x_inf or y_sup>y_inf:
		print '\n Wrong order given.\n (0,0) is the upper left corner!\n'
		return menu()
	num_linhas=y_inf-y_sup
	num_colunas=x_inf-x_sup
	matriz_cort=[]
	for linha in range(num_linhas+1):
		matriz_cort.append([])
		for coluna in range(num_colunas+1):
			matriz_cort[linha].append([])
			matriz_cort[linha][coluna]=matriz_da_imagem[y_sup+linha][x_sup+coluna]
	matriz_da_imagem=copy.deepcopy(matriz_cort)
        matriz_cort=None
	print '\n Image was successfully changed.\n'
	mostra_imagem()

#Definicao que guarda a imagem no ficheiro escolhido pelo utilizador
def guardar_imagem():
	ficheiro=''	
	while ficheiro=='':
		ficheiro=raw_input('Enter new file name: ')				
	
	if ficheiro[-4:]!='.ppm':
		imagem_final=open(ficheiro+'.ppm','w')
	else:
		imagem_final=open(ficheiro, 'w')

	imagem_final.write('P3\n')
	imagem_final.write('# Vitor e Alexandre\n')
	imagem_final.write(str(num_colunas)+' '+str(num_linhas)+'\n')
	imagem_final.write('255\n')
	for linha in range(num_linhas):
		for coluna in range(num_colunas):
			for cor in range(3):
				imagem_final.write(str(matriz_da_imagem[linha][coluna][cor])+'\n')
	imagem_final.close()
	print '\n Image was successfully saved.\n'	
	menu()

#Definicao para passar os numeros de RGB para binario, que como vai ate 255 precisamos de 8 bits
def binario(decimal):
	binario=''
	if decimal==0:
		return '0'*8
	while decimal!=0:
		bit=decimal%2
		binario=str(bit)+binario
		decimal=decimal/2
	if len(binario)<8:
		binario='0'*(8-len(binario))+binario
	return binario

#Definicao que passa o texto para binario
def texto_bin():
	texto=raw_input(' Enter text:\n ')
	#Isto indica o inicio e o fim do texto, e importante para quando estivermos a ler sabermos se existe texto, e onde este acaba.
	texto=chr(2)+texto+chr(3)
	if len(texto)>(num_linhas*num_colunas*3/8):
		print '\n Text is too long.\n'
		return menu()
	texto_binario=''
	for elem in texto:
		texto_binario=texto_binario+binario(ord(elem))
	esconde_texto(texto_binario)

#Definicao que atraves de uma mensagem previamente traduzida em ascii (valores binarios) armazena sequencialmente essa informacao nos pixeis da imagem
def esconde_texto(texto):
	global matriz_da_imagem
	for linha in range(num_linhas):
		for coluna in range(num_colunas):
			for cor in range(3):
				if texto!='':
					rgb_binario=binario(matriz_da_imagem[linha][coluna][cor])
					rgb_binario=rgb_binario[:-1]+texto[0]
					texto=texto[1:]
					matriz_da_imagem[linha][coluna][cor]=int(rgb_binario,2)
	print '\n Text was successfully hidden in the image.\n'	
	menu()

# Definicao que verifica se existe alguma mensagem escondida na imagem e que le a mensagem caso exista
def mostra_texto():
	global matriz_da_imagem
	ord_chr_binario=''
	texto_final=''
	existe_texto=False
	for linha in range(num_linhas):
		for coluna in range(num_colunas):
			for cor in range(3):
				rgb_binario=binario(matriz_da_imagem[linha][coluna][cor])
				ord_chr_binario=ord_chr_binario+rgb_binario[-1]
				rgb_binario=rgb_binario[:-1]+str(random.randint(0,1))  #Isto serve para que a mensagem que estava escondida desapareca
				matriz_da_imagem[linha][coluna][cor]=int(rgb_binario,2)
				if len(ord_chr_binario)==8:
					ord_chr_decimal=int(ord_chr_binario,2)
					caracter=chr(ord_chr_decimal)
					if caracter==chr(3):
						print '\n',texto_final,'\n','\n (Message was deleted, save it if you want to permanently delete it.)\n'					
						return menu()
					elif existe_texto==True:
						texto_final=texto_final+caracter
						ord_chr_binario=''										
					elif caracter==chr(2):
						existe_texto=True
						ord_chr_binario=''
					else:
						print'\n There is no hidden message on this image.\n'
						return menu()	

#Definicao que encripta a imagem em funcao da password introduzida pelo utilizador
def encriptar():
	global matriz_da_imagem
	password=raw_input('Ente password: ')
	password2=raw_input('Renter password: ')
	if password!=password2:
		print '\n Error: Different passwords.\n'
		return menu()
	val_password=0
	for caracter in password:
		val_password=val_password+ord(caracter)
	random.seed(val_password)
	lista_colunas_nova=range(num_colunas)
	serie=random.shuffle(lista_colunas_nova)
	matriz_provisoria=[]
	for linha in range(num_linhas):
		matriz_provisoria.append([])
		for coluna in range(num_colunas):
			matriz_provisoria[linha].append([])
			matriz_provisoria[linha][coluna]=matriz_da_imagem[linha][lista_colunas_nova[coluna]]
	matriz_da_imagem=copy.deepcopy(matriz_provisoria)
	matriz_provisoria=None
	print '\n Image was encrypted\n'
	mostra_imagem()

#Definicao que vai desencriptar a imagem atraves da password
def desencriptar():
	global matriz_da_imagem
	password=raw_input('Enter password: ')
	val_password=0
	for caracter in password:
		val_password=val_password+ord(caracter)
	random.seed(val_password)
	lista_colunas_2=range(num_colunas)
	serie=random.shuffle(lista_colunas_2)
	matriz_provisoria=copy.deepcopy(matriz_da_imagem)
	for linha in range(num_linhas):
		for coluna in range(num_colunas):
			matriz_da_imagem[linha][lista_colunas_2[coluna]]=matriz_provisoria[linha][coluna]
	matriz_provisoria=None
	print '\n Image was decrypted according to the given password.\n'
	mostra_imagem()
	
#Definicao que mostra o menu e verifica as opcoes escolhidas 
def menu():
	print '\nWhat do you want to do?\n 1. Open image\n 2. Show image\n 3. Save image\n 4. Replace original image\n 5. Grey tones\n 6. Change color \n 7. Horizontal reflection \n 8. Vertical reflection \n 9. Negative image\n 10. Rotate 90 degrees to the left\n 11. Rotate 90 degrees to the right\n 12. Rotate 180 degrees\n 13. Frame\n 14. Cut\n 15. Hide a messsage in the image\n 16. Read an hidden messsage in the image\n 17. Encrypt image\n 18. Decrypt image\n 19. Exit\n'

	try:
		opcao=0
		while opcao not in range(1,20):
			opcao=input('Choose option: ')
		if opcao==19:
			print('\nBye\n')
			return
		elif opcao==1:
			abrir_imagem()
		elif existe_imagem and opcao==2:
			mostra_imagem()
		elif existe_imagem and opcao==3:
			guardar_imagem()
		elif existe_imagem and opcao==4:
			repor_imagem()
		elif existe_imagem and opcao==5:
			passagem_cinza()
		elif existe_imagem and opcao==6:
			altera_cor()		
		elif existe_imagem and opcao==7:
			cria_reflexao(1)
		elif existe_imagem and opcao==8:
			cria_reflexao(2)
		elif existe_imagem and opcao==9:
			cria_negativo()
		elif existe_imagem and opcao==10:
			rodar_90_esquerda()
		elif existe_imagem and opcao==11:
			rodar_90_direita()
		elif existe_imagem and opcao==12:
			rodar_180()
		elif existe_imagem and opcao==13:
			moldura()
		elif existe_imagem and opcao==14:
			cortar()
		elif existe_imagem and opcao==15:
			texto_bin()
		elif existe_imagem and opcao==16:
			mostra_texto()
		elif existe_imagem and opcao==17:
			encriptar()
		elif existe_imagem and opcao==18:
			desencriptar()
		elif not existe_imagem:
			print '\nNo image was loaded!\n'
			menu()
	except:
		print '\nInvalid Option!\n'
		return menu()

if __name__ == '__main__':

	print '\n      Welcome!'
	global existe_imagem
	existe_imagem=False
	menu()
