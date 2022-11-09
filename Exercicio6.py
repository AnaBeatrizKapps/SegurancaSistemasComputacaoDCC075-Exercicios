from random import randint


def main():
    # Ambas as pessoas ser�o acordadas sobre o
    # chaves p�blicas G e P
    # Um n�mero primo P � obtido
    P = 23

    # Uma raiz primitiva para P, G � obtida
    G = 9

    print('The Value of P is :%d' % (P))
    print('The Value of G is :%d' % (G))

    # Alice ir� escolher a chave privada
    a = 4
    print('The Private Key a for Alice is :%d' % (a))

    # obt�m a chave gerada
    x = int(pow(G, a, P))

    # Bob will choose the private key b
    b = 3
    print('The Private Key b for Bob is :%d' % (b))

    # obt�m a chave gerada
    y = int(pow(G, b, P))

    # Chave secreta para Alice
    ka = int(pow(y, a, P))

    # Chave secreta para Bob
    kb = int(pow(x, b, P))

    print('Secret key for the Alice is : %d' % (ka))
    print('Secret Key for the Bob is : %d' % (kb))


if __name__ == "__main__":
    main()


# Etapa 1: Alice e Bob obt�m n�meros p�blicos P = 23, G = 9

# Passo 2: Alice selecionou uma chave privada a = 4 e
#         Bob selecionou uma chave privada b = 3

# Etapa 3: Alice e Bob calculam valores p�blicos
# Alice: x =(9^4 mod 23) = (6561 mod 23) = 6
#         Bob: y = (9^3 mod 23) = (729 mod 23) = 16

# Etapa 4: Alice e Bob trocam n�meros p�blicos

# Passo 5: Alice recebe a chave p�blica y = 16 e
#         Bob recebe a chave p�blica x = 6

# Etapa 6: Alice e Bob calculam chaves sim�tricas
#         Alice: ka = y^a mod p = 65536 mod 23 = 9
#         Bob: kb = x^b mod p = 216 mod 23 = 9

# Etapa 7: 9 � o segredo compartilhado.
