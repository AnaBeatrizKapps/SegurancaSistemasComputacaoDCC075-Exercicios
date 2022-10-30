import binascii

# Geração de chave de bits aleatórios
def rand_key(p):

    import random
    key1 = ""
    p = int(p)

    for i in range(p):
        temp = random.randint(0,1)
        temp = str(temp)
        key1 = key1 + temp
    return(key1)

# Função para implementar bit exor
def exor(a,b):
    temp = ""
    for i in range(n):
        if (a[i] == b[i]):
            temp += "0"
        else:
            temp += "1"
    return temp

# Definindo a função BinarytoDecimal()
def BinaryToDecimal(binary):
    # Usando a função int para converter para string
    string = int(binary, 2)
    return string

# Cifra de Feistel
PT = "teste"
print("Plain Text is:", PT)

# Convertendo o texto simples para ASCII
PT_Ascii = [ord(x) for x in PT]

# Convertendo o formato binário ASCII para 8 bits
PT_Bin = [format(y,'08b') for y in PT_Ascii]
PT_Bin = "".join(PT_Bin)
n = int(len(PT_Bin)//2)
L1 = PT_Bin[0:n]
R1 = PT_Bin[n::]
m = len(R1)

# Gera a chave K1 para o primeiro round
K1= rand_key(m)

# Gera a chave K2 para o primeiro round
K2= rand_key(m)

# primeira rodada do Feistel
f1 = exor(R1,K1)
R2 = exor(f1,L1)
L2 = R1

# segunda rodada do Feistel
f2 = exor(R2,K2)
R3 = exor(f2,L2)
L3 = R2

# Texto cifrado
bin_data = L3 + R3
str_data =' '

for i in range(0, len(bin_data), 7):
    # bin_data do intervalo de índice [0, 6] e armazenando em temp_data
    temp_data = bin_data[i:i + 7]
        
    # passando temp_data na função BinarytoDecimal() para obter o valor decimal do temp_data correspondente
    decimal_data = BinaryToDecimal(temp_data)
        
    # Decodificando o valor decimal retornado por
    # Função BinarytoDecimal(), usando chr()
    # função que retorna a string correspondente
    # caractere para determinado valor ASCII e armazene-o
    # em str_data
    str_data = str_data + chr(decimal_data)

print("Cipher Text:", str_data)

# Descriptografia
L4 = L3
R4 = R3
f3 = exor(L4,K2)
L5 = exor(R4,f3)
R5 = L4
f4 = exor(L5,K1)
L6 = exor(R5,f4)
R6 = L5
PT1 = L6+R6
PT1 = int(PT1, 2)
RPT = binascii.unhexlify( '%x'% PT1)
print("Retrieved Plain Text is: ", RPT)