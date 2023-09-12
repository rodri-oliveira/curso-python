entrada = input('[E]ntrar ou [S]air')
senha_digitada = int(input('Digite sua senha: '))
senha_permitida = 123456

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Login correto. ')
else:
    print('Login invalido.')

