import customtkinter as ctk



def usuario_existente(usuario_procurado):
    try:
        with open("funcionario.txt", "r", encoding="utf-8") as arq:
            for linha in arq:
                nome, user, email, senha = linha.strip().split(";")
                if user == usuario_procurado:
                    return True
    except FileNotFoundError:
        return False  
    return False


def salvar_cadastro_txt(nome, usuario, email, senha, confirmar):
    if usuario_existente(usuario):
        return "Usuário já existente! Escolha outro."

    if ("@" not in email) or (".com" not in email and ".br" not in email):
        return "Email inválido."

    if senha != confirmar:
        return "As senhas não coincidem."

    try:
        with open("funcionario.txt", "a", encoding="utf-8") as arq:
            arq.write(f"{nome};{usuario};{email};{senha}\n")
        return "Cadastrado com sucesso!"
    except:
        return "Erro ao salvar no banco de dados."


def validar_login(usuario_digitado, senha_digitada):
    try:
        with open("funcionario.txt", "r", encoding="utf-8") as arq:
            for linha in arq:
                nome, usuario, email, senha = linha.strip().split(";")

                if usuario_digitado == usuario and senha_digitada == senha:
                    return "Login realizado com sucesso!"
    except FileNotFoundError:
        return "Nenhum funcionário cadastrado ainda."

    return "Usuário ou senha incorretos."




def cadastro_funcionario():
    nome=input("Nome completo: ")
    usuario=input("Usuário: ")
    email=input("Email: ")
    senha=input("Senha: ")
    confirmar=input("Confirmar senha: ")

    if usuario_existente(usuario):
        print("Usuário já existente! Escolha outro")
        return

    if ("@" not in email) or (".com" not in email and ".br" not in email): 
        print("Email invalido")
        return

    if confirmar==senha:
        with open("funcionario.txt", "a") as arq:
            arq.write(f"{nome};{usuario};{email};{senha}\n")
        print("Cadastrado com sucesso!")
    else:
        print("Senha incorreta")




#Janela Principal
ctk.set_appearance_mode("dark")
sistema=ctk.CTk()
sistema.title("Locação de veículos")
sistema.geometry("900x600")
sistema.resizable(False, False)

label_titulo= ctk.CTkLabel(sistema, text="Locadora de Veículos", font=("Arial", 30, "bold"))
label_titulo.pack(pady=20)

#Tela de Login
label_usuario= ctk.CTkLabel(sistema, text="Usuário")
label_usuario.pack(pady=10)

campo_usuario=ctk.CTkEntry(sistema, placeholder_text="Digite seu usuário")
campo_usuario.pack(pady=5)

label_senha= ctk.CTkLabel(sistema, text="Senha")
label_senha.pack()

campo_senha=ctk.CTkEntry(sistema, placeholder_text="Digite sua senha", show="*")
campo_senha.pack()

botao=ctk.CTkButton(sistema,text="Login", command=validar_login)
botao.pack(pady=10)

resultado_login=ctk.CTkLabel(sistema, text="")
resultado_login.pack(pady=10)

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

    
    def clicar_cadastrar():
        nome = entry_nome.get()
        usuario = entry_usuario.get()
        email = entry_email.get()
        senha = entry_senha.get()
        confirmar = entry_confirmar.get()

        resultado = salvar_cadastro_txt(nome, usuario, email, senha, confirmar)


        if resultado == "Cadastrado com sucesso!":
            status.configure(text=resultado, text_color="green")
        else:
            status.configure(text=resultado, text_color="red")

    # BOTÃO DENTRO DA TELA DE CADASTRO
    botao_cadastrar_usuario = ctk.CTkButton(
        cadastro,
        text="Cadastrar Usuário",
        command=clicar_cadastrar
    )
    botao_cadastrar_usuario.pack(pady=20)

botao_abrir_cadastro = ctk.CTkButton(sistema, text="Cadastrar funcionário", command=tela_cadastro) 
botao_abrir_cadastro.pack(pady=10)


sistema.mainloop()
