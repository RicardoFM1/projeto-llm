# exercicio 1:

idades = [15, 22, 34, 42, 27, 19, 30, 18, 25, 40]

mediaIdade = sum(idades) / len(idades)

print(f"A média das idades é: {mediaIdade}")
print(f"A maior idade é: {max(idades)}")
print(f"A menor idade é: {min(idades)}")


# exercicio 2: 


senha = input("Digite a senha: ")

temDigito = False
temNumero = False
temLetra = False

for caractere in senha:
    if caractere.isdigit():
        temDigito = True
    if caractere.isalpha():
        temLetra = True

if len(senha) >= 8 and temDigito and temLetra:
    print("Senha válida!")
else:
    print("Senha inválida!")