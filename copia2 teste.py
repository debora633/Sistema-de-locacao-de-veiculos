import customtkinter as ctk

#Janela
ctk.set_appearance_mode("dark")
sistema=ctk.CTk()
sistema.title("Locação de veículos")
sistema.geometry("900x600")
sistema.resizable(False, False)

label_titulo= ctk.CTkLabel(sistema, text="Locadora de Veículos", font=("Arial", 30, "bold"))
label_titulo.pack(pady=20)

#Label
label_usuario= ctk.CTkLabel(sistema, text="Usuário")
label_usuario.pack(pady=10)
#Entry
campo_usuario=ctk.CTkEntry(sistema, placeholder_text="Digite seu usuário")
campo_usuario.pack(pady=5)
#Label
label_senha= ctk.CTkLabel(sistema, text="Senha")
label_senha.pack()
#Entry
campo_usuario=ctk.CTkEntry(sistema, placeholder_text="Digite sua senha")
campo_usuario.pack()
#Button
botao=ctk.CTkButton(sistema,text="Login")
botao.pack(pady=10)


sistema.mainloop()

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
