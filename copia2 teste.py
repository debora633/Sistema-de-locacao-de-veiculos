import customtkinter as ctk



def usuario_existente(usuario_procurado):  #verifica se tem algum usuario no banco igual ao digitado
    usuario_encontrado=False
    with open("funcionario.txt", "r") as arq:
        for linha in arq:
            usuario= linha.strip().split(";")
            if usuario[1]==usuario_procurado:
                usuario_encontrado=True
                break
    return usuario_encontrado


def cadastro_funcionario():
    nome=input("Nome completo: ")
    usuario=input("Usuário: ")
    email=input("Email: ")
    senha=input("Senha: ")
    confirmar=input("Confirmar senha: ")

    if usuario_existente(usuario):
        print("Usuário já existente! Escolha outro")
        return

    if ("@" not in email) or (".com" not in email and ".br" not in email):  #verificação de email válido
        print("Email invalido")
        return

    if confirmar==senha:
        with open("funcionario.txt", "a") as arq:
            arq.write(f"{nome};{usuario};{email};{senha}\n")
        print("Cadastrado com sucesso!")
    else:
        print("Senha incorreta")

def login():
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    try:
        with open("funcionario.txt", "r") as arq:
            for linha in arq:
                nome, user, email, senha_salva = linha.strip().split(";")
                if usuario == user and senha == senha_salva:
                    print("Login realizado com sucesso!")
                    return True
    except FileNotFoundError:
        print("Nenhum funcionário cadastrado ainda.")
        return False

    print("Usuário ou senha incorretos.")
    return False


#Janela
ctk.set_appearance_mode("dark")
sistema=ctk.CTk()
sistema.title("Locação de veículos")
sistema.geometry("900x600")
sistema.resizable(False, False)

label_titulo= ctk.CTkLabel(sistema, text="Locadora de Veículos", font=("Arial", 30, "bold"))
label_titulo.pack(pady=20)


label_usuario= ctk.CTkLabel(sistema, text="Usuário")
label_usuario.pack(pady=10)

campo_usuario=ctk.CTkEntry(sistema, placeholder_text="Digite seu usuário")
campo_usuario.pack(pady=5)

label_senha= ctk.CTkLabel(sistema, text="Senha")
label_senha.pack()

campo_usuario=ctk.CTkEntry(sistema, placeholder_text="Digite sua senha")
campo_usuario.pack()

botao=ctk.CTkButton(sistema,text="Login")
botao.pack(pady=10)

#TELA DE CADASTROOOOO

def tela_cadastro():
    cadastro = ctk.CTkToplevel()
    cadastro.title("Cadastro de Funcionário")
    cadastro.geometry("900x600")
    cadastro.resizable(False, False)

    
    titulo = ctk.CTkLabel(cadastro, text="Cadastro de Funcionário", font=("Arial", 20, "bold"))
    titulo.pack(pady=20)

    
    entry_nome = ctk.CTkEntry(cadastro, placeholder_text="Nome completo", width=300)
    entry_nome.pack(pady=10)

    entry_usuario = ctk.CTkEntry(cadastro, placeholder_text="Usuário", width=300)
    entry_usuario.pack(pady=10)

    entry_email = ctk.CTkEntry(cadastro, placeholder_text="Email", width=300)
    entry_email.pack(pady=10)

    entry_senha = ctk.CTkEntry(cadastro, placeholder_text="Senha", show="*", width=300)
    entry_senha.pack(pady=10)

    entry_confirmar = ctk.CTkEntry(cadastro, placeholder_text="Confirmar senha", show="*", width=300)
    entry_confirmar.pack(pady=10)

    status = ctk.CTkLabel(cadastro, text="", text_color="red")
    status.pack(pady=10)

botao_cadastro = ctk.CTkButton(sistema, text="Cadastrar funcionário", command=tela_cadastro)
botao_cadastro.pack(pady=10)


sistema.mainloop()
