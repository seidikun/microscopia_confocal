# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 16:34:02 2020

@author: seidi
"""

# a. Crie as variáveis necessárias para que o programa funcione corretamente
# b. Inicialize as variáveis com valores padrão adequados.
import math

# Formating varibales
messageRest          = "[---- No todo planned for this day ----]"
maxWidthInCharacters = 96
underLineRep         = '_'*maxWidthInCharacters
midLineRep           = '-'*36
centerSpacement      = round((maxWidthInCharacters - len(messageRest))/2)


tipo_celula    = ''
taxa_aquisicao = 0 # pontos por mm


# c. Crie uma pequena mensagem de apresentação do programa para realizar uma interface
#com o usuário. Ex.: “Esse programa tem como objetivo receber dados para ...”

msg = 'Este programa apresenta uma interação '
print(msg)

# d. Solicite algumas informações necessárias para a configuração de um microscópio dessa
#natureza. Buscar pelo menos 10 itens para essas informações de entrada. Ex.: resolução
#da imagem desejada, tipo de célula a ser escaneada, faixa de iluminação necessária.

# e. Para cada informação digitada, apresente na tela a seguinte mensagem: “Houve
#alteração na variável inserida? ”. Após a mensagem, apresentar verdadeiro ou falso com
#base no que foi digitado pelo usuário e o que estava armazenado na variável. Obs.: Não
#deve ser utilizado if aqui.

msg = 'Houve alteração na variável digitada?'
new_tipo_celula = input('Digite o tipo de célula: ')
print(msg, tipo_celula != new_tipo_celula)


new_taxa_aquisicao = input('\nDigite a taxa de aquisição: ')
print(msg, new_taxa_aquisicao != taxa_aquisicao)





# f. Retorne ao usuário de forma organizada as informações que foram digitadas. Ex.: “As
#informações de configurações setadas pelo usuário são: ...”

print(underLineRep)
msg = "As informações de configurações setadas pelo usuário são:"
print(msg)

print('Tipo de célula: ', new_tipo_celula)
print('Taxa de aquisição: ', new_tipo_celula)


# g. Após setada as configurações iniciais o usuário deve utilizar dois caracteres para a
#calibração do equipamento no sentido horizontal. Para isso, ele deve apertar a tecla
#correspondente à primeira letra do seu nome 10x e à última letra do seu nome 10x.

print(underLineRep)
msg = 'Seção de calibração do equipamento no sentido vertical'
print(msg)

# h. Imediatamente após apertar a tecla o programa deve apresentar na tela que a informação
#foi corretamente digitada e mostrar o caractere pressionado.

count = 1
stepX = input('Por favor, digite S: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite S: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite S: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite S: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite S: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite S: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite S: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite S: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite S: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite S: ')
print('você digitou (', count, '/10): ' , stepX)

count = 1
stepX = input('Por favor, digite I: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite I: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite I: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite I: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite I: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite I: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite I: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite I: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite I: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite I: ')
print('você digitou (', count, '/10): ' , stepX)


# i. Na sequência o usuário deve utilizar dois caracteres para a calibração do equipamento
#no sentido vertical. Para isso, ele deve apertar a tecla correspondente à segunda letra do
#seu nome 10x e à penúltima letra do seu nome 10x.


print(underLineRep)
msg = 'Seção de calibração do equipamento no sentido vertical'
print(msg)


# j. Imediatamente após apertar a tecla o programa deve apresentar na tela que a informação
#foi corretamente digitada e mostrar o caractere pressionado.


count = 1
stepX = input('Por favor, digite E: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite E: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite E: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite E: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite E: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite E: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite E: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite E: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite E: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite E: ')
print('você digitou (', count, '/10): ' , stepX)

count = 1
stepX = input('Por favor, digite D: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite D: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite D: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite D: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite D: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite D: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite D: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite D: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite D: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite D: ')
print('você digitou (', count, '/10): ' , stepX)


# k. Finalmente, o programa deverá apresentar na tela que houve o término da calibração do
#sistema.

print(underLineRep)
msg = "O sistema está devidamente calibrado!"
print(msg)



# l. Para verificar que o programa está funcionando corretamente, execute-o colocando um
#breakpoint na linha 15. Tire um print da tela mostrando a linha parada e as informações
#armazenadas nas variáveis até então.