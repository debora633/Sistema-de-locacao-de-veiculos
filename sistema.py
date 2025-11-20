import customtkinter as ctk



def usuario_existente(usuario_procurado):
    try:
        with open("funcionario.txt", "r", encoding="utf-8") as arq:
            for linha in arq:
                linha = linha.strip()
                if linha == "":  
                    continue

                partes = linha.split(";")
                if len(partes) != 4: 
                    continue

                nome, user, email, senha = partes
                if user == usuario_procurado:
                    return True
    except FileNotFoundError:
        return False  
    return False

def email_existente(email_procurado):
    try:
        with open("funcionario.txt", "r", encoding="utf-8") as arq:
            for linha in arq:
                linha = linha.strip()
                if linha == "":  
                    continue

                partes = linha.split(";")
                if len(partes) != 4: 
                    continue

                nome, user, email, senha = partes
                if email == email_procurado:
                    return True
    except FileNotFoundError:
        return False  
    return False


def salvar_cadastro_txt(nome, usuario, email, senha, confirmar):
    if usuario_existente(usuario):
        return "Usuário já existente! Escolha outro."
    
    if email_existente(email):
        return "O email já foi registrado."

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
                linha = linha.strip()

                
                if linha == "":
                    continue

                partes = linha.split(";")

                
                if len(partes) != 4:
                    continue

                nome, usuario, email, senha = partes

                if usuario_digitado == usuario and senha_digitada == senha:
                    resultado_login.configure(text="Login realizado!", text_color="green")
                    return

    except FileNotFoundError:
        resultado_login.configure(text="Nenhum funcionário cadastro ainda", text_color="red")
        return

    resultado_login.configure(text="Usuário e/ou senha incorretos", text_color="red")


#JANELA PRINCIPAL
ctk.set_appearance_mode("dark")
sistema = ctk.CTk()
sistema.title("Locação de veículos")
sistema.geometry("900x600")
sistema.resizable(False, False)

label_titulo = ctk.CTkLabel(sistema, text="Locadora de Veículos", font=("Arial", 30, "bold"))
label_titulo.pack(pady=20)

frame_login = ctk.CTkFrame(sistema)
frame_cadastro = ctk.CTkFrame(sistema)


label_usuario = ctk.CTkLabel(frame_login, text="Usuário")
label_usuario.pack(pady=10)
campo_usuario = ctk.CTkEntry(frame_login, placeholder_text="Digite seu usuário")
campo_usuario.pack(pady=5)

label_senha = ctk.CTkLabel(frame_login, text="Senha")
label_senha.pack()
campo_senha = ctk.CTkEntry(frame_login, placeholder_text="Digite sua senha", show="*")
campo_senha.pack(pady=5)

resultado_login = ctk.CTkLabel(frame_login, text="")
resultado_login.pack(pady=10)

#TELA DE LOGINN
def tentar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    resultado = validar_login(usuario, senha)
    if resultado == "Login realizado com sucesso!":
        resultado_login.configure(text=resultado, text_color="green")
    else:
        resultado_login.configure(text=resultado, text_color="red")

botao_login = ctk.CTkButton(frame_login, text="Login", command=tentar_login)
botao_login.pack(pady=10)



#TELA DE CADASTROOOO

def mostrar_cadastro():
    frame_login.pack_forget()
    frame_cadastro.pack(fill="both", expand=True)

botao_abrir_cadastro = ctk.CTkButton(frame_login, text="Cadastrar funcionário", command=mostrar_cadastro)
botao_abrir_cadastro.pack(pady=10)

frame_login.pack(fill="both", expand=True)

 
titulo_cadastro = ctk.CTkLabel(frame_cadastro, text="Cadastro de Funcionário", font=("Arial", 20, "bold"))
titulo_cadastro.pack(pady=20)

entry_nome = ctk.CTkEntry(frame_cadastro, placeholder_text="Nome completo", width=300)
entry_nome.pack(pady=10)

entry_usuario = ctk.CTkEntry(frame_cadastro, placeholder_text="Usuário", width=300)
entry_usuario.pack(pady=10)

entry_email = ctk.CTkEntry(frame_cadastro, placeholder_text="Email", width=300)
entry_email.pack(pady=10)

entry_senha = ctk.CTkEntry(frame_cadastro, placeholder_text="Senha", show="*", width=300)
entry_senha.pack(pady=10)

entry_confirmar = ctk.CTkEntry(frame_cadastro, placeholder_text="Confirmar senha", show="*", width=300)
entry_confirmar.pack(pady=10)

status = ctk.CTkLabel(frame_cadastro, text="", text_color="red")
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

botao_cadastrar_usuario = ctk.CTkButton(frame_cadastro, text="Cadastrar Usuário", command=clicar_cadastrar)
botao_cadastrar_usuario.pack(pady=20)

def voltar_login():
    frame_cadastro.pack_forget()
    frame_login.pack(fill="both", expand=True)

botao_voltar = ctk.CTkButton(frame_cadastro, text="Voltar para Login", command=voltar_login)
botao_voltar.pack(pady=10)


sistema.mainloop()
