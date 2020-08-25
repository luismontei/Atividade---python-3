print('faça o cadrasto')
usuario = str(input('Informe o nome de usuário: '))
senha = str(input('Informe a senha: '))
while usuario==senha:
    print('Tente Novamente!')
    usuario = str(input('Informe o nome de usuário: '))
    senha = str(input('Informe a senha: '))
else:
     print('Cadrasto efetuado!')
