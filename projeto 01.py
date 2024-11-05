import random as r  

def gerar(escolha, T):
    senha = ""
    for i in range(T):
        senha += r.choice(escolha)
    return senha

# Código principal
print("Escolha qual nivel de complexidade voce quer:")
nivel = input("(B)basico, (M)medio, (C)complexo? ").upper()

if nivel == "B":
    escolha = "0123456789"
    T = 8  # Tamanho da senha
    senha = gerar(escolha, T)
    print("Senha gerada:", senha)

elif nivel == "M":
    escolha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    T = 10
    senha = gerar(escolha, T)
    print("Senha gerada:", senha)

elif nivel == "C":
    escolha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz*/-+.,-"
    T = 12
    senha = gerar(escolha, T)
    print("Senha gerada:", senha)

else:
    print("Por favor, escolha entre: (B)basico, (M)medio, (C)complexo")
