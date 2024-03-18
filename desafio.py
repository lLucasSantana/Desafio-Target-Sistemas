def calcular_soma_ate(numero):
    return (numero * (numero + 1)) // 2

def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num

def inverter_string(s):
    return s[::-1]

soma = calcular_soma_ate(13)
print("1) A soma dos números de 1 a 13 é:", soma)


numero = int(input("2) Informe um número para verificar se pertence à sequência de Fibonacci: "))
if is_fibonacci(numero):
    print(numero, "pertence à sequência de Fibonacci.")
else:
    print(numero, "não pertence à sequência de Fibonacci.")


padroes_numericos = [
    [1, 3, 5, 7],              
    [2, 4, 8, 16, 32, 64],     
    [0, 1, 4, 9, 16, 25, 36],  
    [4, 16, 36, 64],           
    [],                        
    [2, 10, 12, 16, 17, 18, 19]
]
print("4) Para resolver o problema dos interruptores, siga as instruções fornecidas.")

string_original = input("5) Digite uma string para ser invertida: ")
print("String original:", string_original)
print("String invertida:", inverter_string(string_original))
