print("Digite o primeiro número:")

numero1 = int(input())

print("\nDigite o segundo número:")

numero2 = int(input())

soma = numero1 + numero2

subtracao = numero1 - numero2

divisao = numero1 / numero2

multiplicacao = numero1 * numero2

print("\nA soma é ",soma)

print("\nA subtração é ",subtracao)

print("\nA divisão é ",divisao)

print("\nA multiplicação é ",multiplicacao)

print("\n1) O primeiro número inserido pelo usuário é diferente do segundo?", numero1!=numero2)

print("\n2) A soma dos números é menor que a multiplicação dos números?",soma < multiplicacao)

print("\n3) A subtração dos números é menor que a divisão dos números?", subtracao < divisao)

print("\n3) 4) A soma dos números é igual à multiplicação dos números?", soma == multiplicacao)
