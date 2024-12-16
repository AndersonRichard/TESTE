# 1 - Armazene o nome de uma pessoa em uma variável e apresente uma 
# mensagem a essa pessoa. Sua mensagem deve ser simples.

nome = input("Digite o seu nome: ")
mensagem = "seja bem vindo"

print(f'Olá {nome}, {mensagem}!')


# 2 - Armazene o nome de uma pessoa em uma variável e então apresente o 
# nome dessa pessoa em letras minúsculas, em letras maiúsculas e somente 
# com a primeira letra maiúscula.

nome2 = input("Por favor digite seu nome: ")
nome_minusculo = nome2.lower()
nome_maisculo = nome2.upper()
nome_normal = nome2.title()

print(f'Seu nome em minusculo {nome_minusculo}, nome em maisculo {nome_maisculo} e seu nome de forma normal {nome_normal}')


# 3 - Armazena seu nome completo em uma variável com espaços em branco. 
# Remova os espaços em branco e exiba o nome sem os espaços.

nome3 = input("Por favor digite o seu nome: ")
nome_sem_espaco = nome3.strip()
nome_sem_espaco2 = nome3.lstrip()
nome_sem_espaco3 = nome3.rstrip()
nome_sem_espaco4 = nome3.replace(" ", "")

print(f'Seu nome sem espaços: {nome_sem_espaco}, {nome_sem_espaco2}, {nome_sem_espaco3}, {nome_sem_espaco4}')


# 4 -Escreva as 4 operações básicas recebendo dois valores como parâmetros e 
# exiba os resultados.

print("Por favor digite dois números para realizar as operações: ")
valor1 =float(input("Digite o primeiro valor: "))
valor2 =float(input("Digite o segundo valor: "))

adicao = (valor1 + valor2)
subtracao = (valor1 - valor2)
multiplicacao = (valor1 * valor2)
divisao = (valor1 / valor2)


print(f'O resultado da adição é: {adicao}')
print(f'O resultado da subtração é: {subtracao}')
print(f'O resultado da multiplicação: {multiplicacao}')
print(f'O resultado da divisão é: {divisao}')

# 5 - Calcule a média dos valores de uma lista de 0 a 999
numeros = list(range(0,999))

soma = sum(numeros)

media = soma/len(numeros)

print(f'O valor da média é: {media}')


# 6 - Escreva um programa que receba uma frase do usuário e conte quantas 
# palavras ela possui. Em seguida, inverta a ordem das palavras na frase.

frase = input("Digite a sua frase: ")
frase_separada = frase.split()
frase_contada = len(frase_separada)
print(f'O número de palavras na frase é: {frase_contada}')

frase_separada.reverse()

frase_invertida = ' '.join(frase_separada)

print(f'A frase invertida é: {frase_invertida}')




# 7 - Implemente um programa que utilize estruturas de decisões (if, else, elif) para 
#determinar se um número inserido pelo usuário é positivo, negativo ou zero. 
#Utilize também loops para pedir novos números até que o usuário insira zero.

while True:
    numero = float(input("Digite um número (digite 0 para sair): "))

    if numero > 0:
        print(f'O número {numero} é positivo.')
    elif numero < 0:
        print(f'O número {numero} é negativo')
    elif numero == 0:
        print(f'O número inserido é 0')
        print("Encerrando programa")
        break

# 8 - Desenvolva uma solução que trabalhe com listas e sets para armazenar 
# nomes de alunos em uma turma. Realize operações como adição, remoção e 
# verificação de existência de um nome na lista.
        
   