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
                    mostrar_menu(frame_menu)
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
frame_menu = ctk.CTkFrame(sistema)
frame_listar_veiculos = ctk.CTkFrame(sistema)

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
    validar_login(usuario, senha)

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

#TELA DE MENU PRINCIPAL
def mostrar_menu(frame):
    frame_login.pack_forget()
    frame_cadastro.pack_forget()
    frame_menu.pack_forget()
    frame.pack(fill="both", expand=True)


label_titulo = ctk.CTkLabel(frame_menu, text="MENU PRINCIPAL", font=("Arial", 30, "bold"))
label_titulo.pack(pady=20)

# Botão que chama a tela Gerenciar Veículos
botao1 = ctk.CTkButton(frame_menu,text="Gerenciar Veículos",command=lambda:gerenciar_veiculos())
botao1.pack(pady=10)

botao2 = ctk.CTkButton(frame_menu, text="Gerenciar Locações")
botao2.pack(pady=10)

botao3 = ctk.CTkButton(frame_menu, text="Sair do sistema")
botao3.pack(pady=10)


def salvar_veiculo_txt(marca, modelo, ano, placa, preco):
    try:
        with open("veiculos.txt", "a", encoding="utf-8") as arq:
            arq.write(f"{marca};{modelo};{ano};{placa};{preco}\n")
        return "Veículo cadastrado com sucesso!"
    except:
        return "Erro ao salvar veículo."


def gerenciar_veiculos():
    
    frame_veiculos = ctk.CTkFrame(sistema)

    
    frame_login.pack_forget()
    frame_cadastro.pack_forget()
    frame_menu.pack_forget()

    # Mostra esta tela
    frame_veiculos.pack(fill="both", expand=True)

    titulo_veiculos = ctk.CTkLabel(frame_veiculos,text="Gerenciar Veículos",font=("Arial", 25, "bold"))
    titulo_veiculos.pack(pady=20)

    # Botões de gerenciamento
    ctk.CTkButton(frame_veiculos, text="Listar Veículos", width=200, command=lambda: tela_listar_veiculos(frame_veiculos)).pack(pady=10)
    ctk.CTkButton(frame_veiculos,text="Cadastrar Veículo",width=200,command=lambda: cadastrar_veiculo(frame_veiculos)).pack(pady=10)
    ctk.CTkButton(frame_veiculos, text="Editar Veículo", width=200).pack(pady=10)
    ctk.CTkButton(frame_veiculos, text="Excluir Veículo", width=200).pack(pady=10)

    
    botao_voltar = ctk.CTkButton(frame_veiculos, text="Voltar ao Menu", width=200, fg_color="#444",command=lambda: voltar_para_menu(frame_veiculos))
    botao_voltar.pack(pady=20)


def voltar_para_menu(frame_veiculos):
    frame_veiculos.pack_forget()
    mostrar_menu(frame_menu)      


def cadastrar_veiculo(frame_anterior):
    frame_cadastro_veiculo = ctk.CTkFrame(sistema)


    frame_anterior.pack_forget()


    frame_cadastro_veiculo.pack(fill="both", expand=True)

    titulo = ctk.CTkLabel(frame_cadastro_veiculo, text="Cadastrar Veículo", font=("Arial", 25, "bold"))
    titulo.pack(pady=20)

    entry_marca = ctk.CTkEntry(frame_cadastro_veiculo, placeholder_text="Marca", width=300)
    entry_marca.pack(pady=10)

    entry_modelo = ctk.CTkEntry(frame_cadastro_veiculo, placeholder_text="Modelo", width=300)
    entry_modelo.pack(pady=10)

    entry_ano = ctk.CTkEntry(frame_cadastro_veiculo, placeholder_text="Ano", width=300)
    entry_ano.pack(pady=10)

    entry_placa = ctk.CTkEntry(frame_cadastro_veiculo, placeholder_text="Placa", width=300)
    entry_placa.pack(pady=10)

    entry_preco = ctk.CTkEntry(frame_cadastro_veiculo, placeholder_text="Preço por dia (R$)", width=300)
    entry_preco.pack(pady=10)

    resultado = ctk.CTkLabel(frame_cadastro_veiculo, text="")
    resultado.pack(pady=10)

    def clicar_salvar_veiculo():
        marca = entry_marca.get()
        modelo = entry_modelo.get()
        ano = entry_ano.get()
        placa = entry_placa.get()
        preco = entry_preco.get()

        msg = salvar_veiculo_txt(marca, modelo, ano, placa, preco)
        resultado.configure(text=msg, text_color="green" if "sucesso" in msg else "red")

    ctk.CTkButton(frame_cadastro_veiculo, text="Cadastrar", width=200, command=clicar_salvar_veiculo).pack(pady=20)

    botao_voltar = ctk.CTkButton(frame_cadastro_veiculo,text="Voltar", width=200,fg_color="#444",command=lambda: [frame_cadastro_veiculo.pack_forget(),gerenciar_veiculos()]).pack(pady=10)
    botao_voltar.pack(pady=20)
    

#Tela de listar veículos
def tela_listar_veiculos(frame_veiculos):

    for widget in frame_veiculos.winfo_children():
        widget.destroy()

    #CABEÇALHO DA TABELA DE VEÍCULOS
    frame_header = ctk.CTkFrame(frame_veiculos)
    frame_header.pack(pady=10)

    colunas=["Marca","Modelo","Ano","Placa","Preço por dia (R$)"]

    for coluna in colunas:
        label = ctk.CTkLabel(frame_header,text=coluna,width=150,font=("Arial",12,"bold"))
        label.pack(side="left", padx=5)

    frame_lista = ctk.CTkFrame(frame_veiculos)
    frame_lista.pack(pady=10)

    try:
        with open ("veiculos.txt", "r", encoding=("utf-8") )as arq:
            for linha in arq:
                linha=linha.strip()
                if linha=="":
                    continue

                partes=linha.split(";")
                if len(partes)!=5:   #vai ter que mudar pra 6 quando adicionar o status
                    continue
                marca,modelo,ano,placa,preco=partes
                frame_linha=ctk.CTkFrame(frame_lista)
                frame_linha.pack(pady=5)

                for item in [marca, modelo, ano, placa, preco]:
                    label_item=ctk.CTkLabel(frame_linha,text=item,width=150)
                    label_item.pack(side="left", padx=5)
    except FileNotFoundError:
        label_erro=ctk.CTkLabel(frame_veiculos,text="Nenhum veículo cadastrado ainda.",text_color="red")
        label_erro.pack(pady=20)

    #Botão de voltar
    botao_voltar = ctk.CTkButton(frame_veiculos, text="Voltar", width=200, fg_color="#444", command=lambda: [frame_listar_veiculos.pack_forget(), gerenciar_veiculos()])
    botao_voltar.pack(pady=20)

sistema.mainloop()
