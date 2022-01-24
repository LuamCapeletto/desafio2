numero1 = int(input("Digite o primeiro número: "))

numero2 = int(input("\nDigite o segundo número: "))

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
