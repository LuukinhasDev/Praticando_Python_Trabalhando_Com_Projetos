import random, string

def gerador_de_senha():
    caracteres = list(string.ascii_letters + string.digits + string.punctuation)

    senha = list(random.choice(string.ascii_lowercase) 
        + random.choice(string.ascii_uppercase) 
        + random.choice(string.digits) 
        + random.choice(string.punctuation)) 

    senha_completa = list(random.choices(caracteres, k=8) + senha)
    random.shuffle(senha_completa)

    return "".join(senha_completa)

print("=-"*15)
print(f"\nSenha gerada: {gerador_de_senha()}\n")
print("=-"*15)