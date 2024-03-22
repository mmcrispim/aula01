print("Hello World")

# crie um comando que o usuario digita uma string e retorna o tamanho dela

# print(len(input("digite aqui a string: ")))

# primeiro = int(input("Digite o primeiro número: "))
# segundo = int(input("Digite o segundo número: "))

# print(primeiro + segundo)

CONSTANTE_BONUS = 1000
nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))
bonus = float(input("Digite seu bônus: "))


valor_final = CONSTANTE_BONUS + (salario * bonus)

# print(valor_final)
print(f"O Usuário {nome} possui o Bônus {valor_final:.2f}")