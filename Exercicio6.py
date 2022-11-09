from random import randint


def main():
    # Ambas as pessoas serão acordadas sobre o
    # chaves públicas G e P
    # Um número primo P é obtido
    P = 23

    # Uma raiz primitiva para P, G é obtida
    G = 9

    print('The Value of P is :%d' % (P))
    print('The Value of G is :%d' % (G))

    # Alice irá escolher a chave privada
    a = 4
    print('The Private Key a for Alice is :%d' % (a))

    # obtém a chave gerada
    x = int(pow(G, a, P))

    # Bob will choose the private key b
    b = 3
    print('The Private Key b for Bob is :%d' % (b))

    # obtém a chave gerada
    y = int(pow(G, b, P))

    # Chave secreta para Alice
    ka = int(pow(y, a, P))

    # Chave secreta para Bob
    kb = int(pow(x, b, P))

    print('Secret key for the Alice is : %d' % (ka))
    print('Secret Key for the Bob is : %d' % (kb))


if __name__ == "__main__":
    main()


# Etapa 1: Alice e Bob obtêm números públicos P = 23, G = 9

# Passo 2: Alice selecionou uma chave privada a = 4 e
#         Bob selecionou uma chave privada b = 3

# Etapa 3: Alice e Bob calculam valores públicos
# Alice: x =(9^4 mod 23) = (6561 mod 23) = 6
#         Bob: y = (9^3 mod 23) = (729 mod 23) = 16

# Etapa 4: Alice e Bob trocam números públicos

# Passo 5: Alice recebe a chave pública y = 16 e
#         Bob recebe a chave pública x = 6

# Etapa 6: Alice e Bob calculam chaves simétricas
#         Alice: ka = y^a mod p = 65536 mod 23 = 9
#         Bob: kb = x^b mod p = 216 mod 23 = 9

# Etapa 7: 9 é o segredo compartilhado.
