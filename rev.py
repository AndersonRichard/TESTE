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

# Gerenciamento de alunos em uma turma

def main():
    # Inicializar lista e set para armazenar os nomes dos alunos
    lista_alunos = []
    set_alunos = set()

    while True:
        print("\n==== Menu de Opções ====")
        print("1. Adicionar aluno")
        print("2. Remover aluno")
        print("3. Verificar se um aluno está na turma")
        print("4. Exibir todos os alunos")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o nome do aluno a ser adicionado: ").strip()
            if nome in set_alunos:
                print(f"O aluno {nome} já está na turma.")
            else:
                lista_alunos.append(nome)
                set_alunos.add(nome)
                print(f"Aluno {nome} adicionado com sucesso.")

        elif escolha == "2":
            nome = input("Digite o nome do aluno a ser removido: ").strip()
            if nome in set_alunos:
                lista_alunos.remove(nome)
                set_alunos.remove(nome)
                print(f"Aluno {nome} removido com sucesso.")
            else:
                print(f"O aluno {nome} não está na turma.")

        elif escolha == "3":
            nome = input("Digite o nome do aluno para verificar: ").strip()
            if nome in set_alunos:
                print(f"O aluno {nome} está na turma.")
            else:
                print(f"O aluno {nome} não está na turma.")

        elif escolha == "4":
            print("\nLista de alunos na turma:")
            for aluno in lista_alunos:
                print(f"- {aluno}")

        elif escolha == "5":
            print("Saindo do programa. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

# Revisão
# 1 - Desenvolva um programa que altere em tempo de execução a palavra Java pela 
# palavra Python na frase Exercícios de Java. 

frase = "Exercicio de Java"

frase_alterada = frase.replace("Java", "Python")

print(f'A frase {frase} antes de ser alterada para {frase_alterada}')


# 2 - Desenvolva um programa que leia um número inteiro qualquer e que informe se 
# este número é par ou impar.

numero = int(input("Digite um número por favor: "))

if numero % 2 == 0:
    print(f'O número {numero} é par')
elif numero % 2 != 0:
    print(f'O número {numero} é impar')


# 3 - Desenvolva um programa que leia quatro notas e que apresente a média final. 

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
numero4 = int(input("Digite o quarto número: "))

somatorio = (numero1 + numero2 + numero3 + numero4)
media = somatorio / 4

print(f'A média da 4 notas é: {media}')


soma_notas = 0
quantidade_notas = 4

print("Por favor digite as 4 notas: ")

for i in range(1, quantidade_notas + 1):
    nota = float(input(f'Digite a nota {i}: '))
    soma_notas += nota


media_nota = soma_notas / quantidade_notas


print(f'A média da nota final é: {media_nota}')


# 4 - Desenvolva um programa que leia um número inteiro qualquer e que apresente 
# o número informado com duas casas decimais.

numero = int(input("Digite um número: "))
numero_transformado = float(numero)

print(f'O numero digitado {numero} transformado é: {numero_transformado: .2f}')

# 5 - Desenvolva um programa que leia um número inteiro qualquer e que apresete o 
# número informado, seguido do seu antecessor e do seu sucessor.

numero = int(input("Por favor digite um número: "))

antecessor = numero - 1
sucessor = numero + 1

print(f'O número digitado é: {numero} e o seu antecessor é: {antecessor} e o seu sucessor é: {sucessor}')


# 6 - Desenvolva um programa que armazene quatro notas em uma lista e que 
# apresente a média final. Caso a média seja igual ou superior a 7, apresentar a 
# mensagem "APROVADO", caso contrário, armazenar a nota da prova final e 
# recalcular a média. Caso a nova média seja igual superior a 5, apresentar a 
# mensagem "APROVADO", caso contrário, apresentar a mensagem 
# "REPROVADO".


quantidade_loop = 4 

soma_numeros = 0


for i in range(quantidade_loop):
    numero = float(input(f"Digite a {i+1}ª nota: "))
    soma_numeros += numero

media_nota = soma_numeros / quantidade_loop


if media_nota >= 7:
    print("APROVADO")
else:

    nota_final = float(input("Digite a nota da prova final: "))
    nova_media = (media_nota + nota_final) / 2
    

    if nova_media >= 5:
        print("APROVADO")
    else:
        print("REPROVADO")


# 7 -  Desenvolva um programa que armazene quatro notas em uma lista e que 
# apresente: a média final, a maior nota e a menor nota.

notas = []
for i in range(4):
    nota = float(input(f'Por digite a nota {i+1}:'))
    notas.append(nota)

media_notas = sum(notas)/len(notas)

menor_nota = min(notas)
maior_nota = max(notas)



print(f'A média da nota é: {media_notas}')
print(f'A maior nota é: {maior_nota}')
print(f'A menor nota é: {menor_nota}')

# 8 - Desenvolva um programa que tenha a entrada de um número pelo usuário. Após 
# entrar com um número, tenha uma função que verifique se um número inteiro 
# qualquer é par ou impar

def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "Número Par"
    else:
        return "Número Impar"

numero = int(input("Por favor digite um número: "))

resultado = verificar_par_impar(numero)

print(f'O número digitado {numero} é {resultado}')


# 9 - Considere o seguinte dicionário: {'m1': {'m2': 'Olá Mundo'}}. Carregue e 
# apresente a mensagem "Olá Mundo" contida no dicionário.

dicionario = {'m1': {'m2': 'Olá Mundo'}}

mensagem = dicionario['m1']['m2']

print(mensagem)


# 10 - Carregue a data atual do computador e apresente somente a data.

import datetime

data_atual = datetime.datetime.now()

print(data_atual.strftime("%d/%m/%y"))


# 11 - Carregue a data atual do computador e, com base na data atual, apresente a 
# data de dois dias no futuro

import datetime

data_atual = datetime.datetime.now()

dois_dias_futuro = data_atual + datetime.timedelta(days=2)

print(dois_dias_futuro.strftime("%d/%m/%y"))