

# 1. Fibonacci
def is_fibonacci(n):
    # Função para verificar se um número é quadrado perfeito
    def is_perfect_square(x):
        return int(x**0.5)**2 == x

    # Um número faz parte da sequência de Fibonacci se e somente se um ou ambos
    # de (5*n^2 + 4) ou (5*n^2 - 4) são quadrados perfeitos.
    def is_fibonacci_number(n):
        return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

    if is_fibonacci_number(n):
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."



# 2. Contagem de 'a'
def contar_a(string):
    # Conta a ocorrência de 'a' ou 'A' na string
    count_a = string.lower().count('a')
    return f"A letra 'a' aparece {count_a} vez(es) na string."

# Teste
string = "Abracadabra"  # Altere a string conforme necessário
print(contar_a(string))


# 3. Soma
INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)


# 4. Sequências lógicas
sequencias_code = '''# a) 1, 3, 5, 7, __9_
print(9)

# b) 2, 4, 8, 16, 32, 64, __128__
print(128)

# c) 0, 1, 4, 9, 16, 25, 36, ___49_
print(49)

# d) 4, 16, 36, 64, ___100_
print(100)

# e) 1, 1, 2, 3, 5, 8, ___13_
print(13)

# f) 2, 10, 12, 16, 17, 18, 19, 20


# 5. Interruptores e lâmpadas
interruptores_code = '''# Solução dos interruptores:
# 1. Ligue o primeiro interruptor e deixe ligado por alguns minutos, depois desligue.
# 2. Ligue o segundo interruptor e vá até a sala.
# - Lâmpada acesa = segundo interruptor;
# - Lâmpada apagada e quente = primeiro interruptor;
# - Lâmpada apagada e fria = terceiro interruptor.

