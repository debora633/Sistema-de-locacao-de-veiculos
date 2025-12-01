import customtkinter as ctk
import re
from datetime import datetime
from tkinter import messagebox
        
#salvar dados da locação
def registrar_locacao_txt(nome, cpf, telefone, email, endereco, placa, retirada, prevista):
    try:
        with open("locacao.txt", "a", encoding="utf-8") as arq:
            linha = f"{nome};{cpf};{telefone};{email};{endereco};{placa};{retirada};{prevista};ATIVA\n"
            arq.write(linha)
        return "Cadastrado com sucesso!"
    except:
        return "Erro ao salvar no banco de dados."


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




def pegar_preco_por_placa(placa_busca):
    try:
        with open("veiculos.txt", "r", encoding="utf-8") as arq:
            for linha in arq:
                campos = linha.strip().split(";")
                if len(campos) != 6:
                    continue
                
                marca, modelo, ano, placa, status, preco = campos
                
                if placa == placa_busca:
                    return float(preco)
    except:
        return None

    return None





def ler_veiculo_por_placa(placa_procurada):
    try:
        with open("veiculos.txt", "r", encoding="utf-8") as arq:
            for linha in arq:
                partes = linha.strip().split(";")
                if len(partes) != 6:
                    continue
                marca, modelo, ano, placa, status, preco = partes
                if placa == placa_procurada:
                    return {
                        "marca": marca,
                        "modelo": modelo,
                        "ano": ano,
                        "placa": placa
                    }
    except FileNotFoundError:
        return None
    return None


def buscar_locacao_por_cpf(cpf):
    try:
        with open("locacao.txt", "r", encoding="utf-8") as arq:
            for linha in arq:
                dados = linha.strip().split(";")

                if len(dados) != 9:
                    continue  

                nome, cpf_reg, tel, email, end, placa, retirada, prevista, status = dados

                if cpf_reg == cpf and status == "ATIVA":
                    veiculo = ler_veiculo_por_placa(placa)
                    return {
                        "nome": nome,
                        "cpf": cpf_reg,
                        "telefone": tel,
                        "email": email,
                        "endereco": end,
                        "placa": placa,
                        "retirada": retirada,
                        "prevista": prevista,
                        "status": status,
                        "marca": veiculo.get("marca") if veiculo else "",
                        "modelo": veiculo.get("modelo") if veiculo else "",
                        "ano": veiculo.get("ano") if veiculo else "",
                    }
        return None
    except FileNotFoundError:
        return None




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
                    mostrar_frame(frame_menu)
                    return

    except FileNotFoundError:
        resultado_login.configure(text="Nenhum funcionário cadastro ainda", text_color="red")
        return

    resultado_login.configure(text="Usuário e/ou senha incorretos", text_color="red")


def limpar_campos_devolucao(entrada_cpf, label_erro, label_info, dias_atraso, valor_total):
    entrada_cpf.delete(0, "end")
    label_erro.configure(text="")
    label_info.configure(text="")
    dias_atraso.set("0")
    valor_total.set("0.00")





#JANELA PRINCIPAL
ctk.set_appearance_mode("dark")
sistema = ctk.CTk()
sistema.title("Locação de veículos")
sistema.geometry("900x600")
sistema.resizable(False, False)

label_titulo = ctk.CTkLabel(sistema, text="Locadora de Veículos", font=("Arial", 30, "bold"))
label_titulo.pack(pady=20)

#FRAMES PRINCIPAIS
frame_login = ctk.CTkFrame(sistema)
frame_cadastro = ctk.CTkFrame(sistema)
frame_menu = ctk.CTkFrame(sistema)
frame_gerenciar_veiculos = ctk.CTkFrame(sistema)
frame_cadastro_veiculo = ctk.CTkFrame(sistema)
frame_listar_veiculos = ctk.CTkFrame(sistema)
frame_editar_veiculo = ctk.CTkFrame(sistema)
frame_gerenciar_locacoes = ctk.CTkFrame(sistema)
frame_registrar_locacao = ctk.CTkFrame(sistema)
frame_devolucao_locacao = ctk.CTkFrame(sistema)


def mostrar_frame(frame:ctk.CTkFrame):
    frame_login.pack_forget()
    frame_cadastro.pack_forget()
    frame_menu.pack_forget()
    frame_cadastro_veiculo.pack_forget()
    frame_gerenciar_veiculos.pack_forget()
    frame_listar_veiculos.pack_forget() 
    frame_editar_veiculo.pack_forget()
    frame_gerenciar_locacoes.pack_forget()
    frame_registrar_locacao.pack_forget()
    frame_devolucao_locacao.pack_forget()
    frame.pack(fill="both", expand=True)

#TELA DE LOGINN

label_usuario = ctk.CTkLabel(frame_login, text="Usuário")
label_usuario.pack(pady=10)
campo_usuario = ctk.CTkEntry(frame_login, placeholder_text="Digite seu usuário")
campo_usuario.pack(pady=5)

label_senha = ctk.CTkLabel(frame_login, text="Senha")
label_senha.pack()
campo_senha = ctk.CTkEntry(frame_login, placeholder_text="Digite sua senha", show="*")
campo_senha.pack(pady=5)

checkbox=ctk.CTkCheckBox(frame_login, 
                         text="Mostrar senha", 
                         command=lambda:campo_senha.configure(show="" if checkbox.get()else "*"),
                         bg_color="transparent", 
                         text_color="white")
checkbox.pack(pady=5)

resultado_login = ctk.CTkLabel(frame_login, text="")
resultado_login.pack(pady=10)

botao_login = ctk.CTkButton(frame_login, text="Login", command=lambda: validar_login(campo_usuario.get(), campo_senha.get()))
botao_login.pack(pady=10)


botao_abrir_cadastro = ctk.CTkButton(frame_login, text="Cadastrar funcionário", command=lambda: mostrar_frame(frame_cadastro))
botao_abrir_cadastro.pack(pady=10)

frame_login.pack(fill="both", expand=True)

#TELA DE CADASTROOOO

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

def limpar_campos_cadastro_funcionario():
    entry_nome.delete(0, "end")
    entry_usuario.delete(0, "end")
    entry_email.delete(0, "end")
    entry_senha.delete(0, "end")
    entry_confirmar.delete(0, "end")
    status.configure(text="")



botao_cadastrar_usuario = ctk.CTkButton(frame_cadastro, text="Cadastrar Usuário", command=clicar_cadastrar)
botao_cadastrar_usuario.pack(pady=20)

botao_voltar = ctk.CTkButton(
    frame_cadastro,
    text="Voltar para Login",
    command=lambda: [limpar_campos_cadastro_funcionario(), mostrar_frame(frame_login)]
).pack(pady=10)


#TELA DE MENU PRINCIPAL

label_titulo = ctk.CTkLabel(frame_menu, text="MENU PRINCIPAL", font=("Arial", 30, "bold"))
label_titulo.pack(pady=20)

# Botão que chama a tela Gerenciar Veículos
ctk.CTkButton(frame_menu,text="Gerenciar Veículos",command=lambda: mostrar_frame(frame_gerenciar_veiculos)).pack(pady=10)
ctk.CTkButton(frame_menu, text="Gerenciar Locações", command=lambda: mostrar_frame(frame_gerenciar_locacoes)).pack(pady=10)
ctk.CTkButton(frame_menu, text="Sair do sistema", command=lambda:sair_sistema()).pack(pady=10)

def sair_sistema():
    sistema.destroy()

def salvar_veiculo_txt(marca, modelo, ano, placa, status, preco):
    
    if not marca or not modelo or not ano or not placa or not preco:
        return "Preencha todos os campos!"

    if not ano.isdigit():
        return "Ano inválido. Digite apenas números."
        
    if not re.fullmatch(r"[A-Z]{3}[0-9][A-Z][0-9]{2}", placa.upper()):
        return "Placa no padrão MERCOSUL inválida! Ex.: ABC1D23"
    
    try:
        float(preco)
    except:
        return "Preço inválido. Digite um valor numérico."

    try:
        with open("veiculos.txt", "a", encoding="utf-8") as arq:
            arq.write(f"{marca};{modelo};{ano};{placa};{status};{preco}\n")
        return "Veículo cadastrado com sucesso!"
    except:
        return "Erro ao salvar veículo."


#Tela de gerenciar veículos

titulo_veiculos = ctk.CTkLabel(frame_gerenciar_veiculos,text="Gerenciar Veículos",font=("Arial", 25, "bold"))
titulo_veiculos.pack(pady=20)

# Botões de gerenciamento
ctk.CTkButton(frame_gerenciar_veiculos, text="Listar Veículos", width=200, command=lambda:[carregar_veiculos(), mostrar_frame(frame_listar_veiculos)]).pack(pady=10)
ctk.CTkButton(frame_gerenciar_veiculos,text="Cadastrar Veículo",width=200,command=lambda: mostrar_frame(frame_cadastro_veiculo)).pack(pady=10)
ctk.CTkButton(frame_gerenciar_veiculos, text="Editar/Excluir Veículo", width=200,command=lambda: mostrar_frame(frame_editar_veiculo)).pack(pady=10)
ctk.CTkButton(frame_gerenciar_veiculos, text="Voltar ao Menu", width=200, fg_color="#444",command=lambda: mostrar_frame(frame_menu)).pack(pady=20)

def gerenciar_veiculos():
    mostrar_frame(frame_gerenciar_veiculos)


def editar_veiculo_txt(placa_procurar, nova_marca, novo_modelo, novo_ano, nova_placa):
    try:
        linhas_novas = []
        encontrado = False

        with open("veiculos.txt", "r", encoding="utf-8") as arq:
            for linha in arq:
                partes = linha.strip().split(";")
                if len(partes) != 6:
                    continue

                marca, modelo, ano, placa, status, preco = partes

                if placa == placa_procurar:
                    linhas_novas.append(f"{nova_marca};{novo_modelo};{novo_ano};{nova_placa};{status};{preco}\n")
                    encontrado = True
                else:
                    linhas_novas.append(linha)

        if not encontrado:
            return "Veículo não encontrado."

        if not re.fullmatch(r"[A-Z]{3}[0-9][A-Z][0-9]{2}", placa.upper()):
            return "Placa no padrão MERCOSUL inválida! Ex.: ABC1D23"

        with open("veiculos.txt", "w", encoding="utf-8") as arq:
            arq.writelines(linhas_novas)

        return "Veículo atualizado com sucesso!"

    except:
        return "Erro ao editar veículo."
    


def excluir_veiculo_txt(placa_procurar):
    try:
        linhas_novas = []
        encontrado = False

        with open("veiculos.txt", "r", encoding="utf-8") as arq:
            for linha in arq:
                partes = linha.strip().split(";")
                if len(partes) != 6:
                    continue

                marca, modelo, ano, placa, status, preco = partes

                if placa == placa_procurar:
                    encontrado = True
                else:
                    linhas_novas.append(linha)

        if not encontrado:
            return "Veículo não encontrado."

        with open("veiculos.txt", "w", encoding="utf-8") as arq:
            arq.writelines(linhas_novas)

        return "Veículo excluído com sucesso!"

    except:
        return "Erro ao excluir veículo."



#TELA DE CADASTRO DE VEÍCULOS

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
    status = "Disponível"
    preco = entry_preco.get()

    msg = salvar_veiculo_txt(marca, modelo, ano, placa, status, preco)
    resultado.configure(text=msg, text_color="green" if "sucesso" in msg else "red")

ctk.CTkButton(frame_cadastro_veiculo, text="Cadastrar", width=200, command=clicar_salvar_veiculo).pack(pady=20)
ctk.CTkButton(
    frame_cadastro_veiculo,
    text="Voltar",
    width=200,
    fg_color="#444",
    command=lambda: [limpar_cadastro_veiculo(), mostrar_frame(frame_gerenciar_veiculos)]
).pack(pady=20)


def limpar_cadastro_veiculo():
    entry_marca.delete(0, "end")
    entry_modelo.delete(0, "end")
    entry_ano.delete(0, "end")
    entry_placa.delete(0, "end")
    entry_preco.delete(0, "end")
    resultado.configure(text="")


def cadastrar_veiculo():
    limpar_cadastro_veiculo()
    mostrar_frame(frame_cadastro_veiculo)

def carregar_veiculos():
    #Limpar frame antes de carregar
    for widget in frame_listar_veiculos.winfo_children():
        widget.destroy()
    
    mostrar_frame(frame_listar_veiculos)

    #TELA DE LISTAR VEÍCULOS
    frame_header = ctk.CTkFrame(frame_listar_veiculos) #CABEÇALHO DA TABELA DE VEÍCULOS
    frame_header.pack(pady=10)

    colunas=["Marca","Modelo","Ano","Placa","status","Preço/dia (R$)"]

    for coluna in colunas:
        label = ctk.CTkLabel(frame_header,text=coluna,width=150,font=("Arial",12,"bold"))
        label.pack(side="left", padx=5)

    frame_lista = ctk.CTkFrame(frame_listar_veiculos)
    frame_lista.pack(pady=10)

    try:
        with open ("veiculos.txt", "r", encoding=("utf-8") )as arq:
            for linha in arq:
                linha=linha.strip()
                if linha=="":
                    continue
                partes=linha.split(";")
                if len(partes)!=6:   
                    continue
                marca,modelo,ano,placa,status,preco=partes
                frame_linha=ctk.CTkFrame(frame_lista)
                frame_linha.pack(pady=5)

                for item in [marca, modelo, ano, placa, status, preco]:
                    label_item=ctk.CTkLabel(frame_linha,text=item,width=150)
                    label_item.pack(side="left", padx=5)
    except FileNotFoundError:
        label_erro=ctk.CTkLabel(frame_listar_veiculos,text="Nenhum veículo cadastrado ainda.",text_color="red")
        label_erro.pack(pady=20)

    
    ctk.CTkButton(frame_listar_veiculos, text="Voltar", width=200, fg_color="#444", command=lambda: mostrar_frame(frame_gerenciar_veiculos)).pack(pady=20)

    

# TELA DE EDITAR VEÍCULOS

titulo_edit = ctk.CTkLabel(frame_editar_veiculo, text="Editar / Excluir Veículo", font=("Arial", 25, "bold"))
titulo_edit.pack(pady=20)

entry_edit_marca = ctk.CTkEntry(frame_editar_veiculo, placeholder_text="Nova Marca", width=300)
entry_edit_marca.pack(pady=10)

entry_edit_modelo = ctk.CTkEntry(frame_editar_veiculo, placeholder_text="Novo Modelo", width=300)
entry_edit_modelo.pack(pady=10)

entry_edit_ano = ctk.CTkEntry(frame_editar_veiculo, placeholder_text="Novo Ano", width=300)
entry_edit_ano.pack(pady=10)

entry_edit_placa = ctk.CTkEntry(frame_editar_veiculo, placeholder_text="Placa do veículo a alterar", width=300)
entry_edit_placa.pack(pady=10)

resultado_edit = ctk.CTkLabel(frame_editar_veiculo, text="")
resultado_edit.pack(pady=10)


def clicar_editar():
    placa = entry_edit_placa.get()
    marca = entry_edit_marca.get()
    modelo = entry_edit_modelo.get()
    ano = entry_edit_ano.get()

    if not marca or not modelo or not ano or not placa:
        resultado_edit.configure(text="Preencha todos os campos", text_color="red")
        return

    msg = editar_veiculo_txt(placa, marca, modelo, ano, placa)
    resultado_edit.configure(text=msg, text_color="green" if "sucesso" in msg else "red")

def clicar_excluir():
    placa = entry_edit_placa.get()

    if not placa:
        resultado_edit.configure(text="Digite a placa para excluir.", text_color="red")
        return

    msg = excluir_veiculo_txt(placa)
    resultado_edit.configure(text=msg, text_color="green" if "sucesso" in msg else "red")


def limpar_campos_editar_veiculo():
    entry_edit_marca.delete(0, "end")
    entry_edit_modelo.delete(0, "end")
    entry_edit_ano.delete(0, "end")
    entry_edit_placa.delete(0, "end")
    resultado_edit.configure(text="")



ctk.CTkButton(frame_editar_veiculo, text="Editar", width=200, command=clicar_editar).pack(pady=10)
ctk.CTkButton(frame_editar_veiculo, text="Excluir", width=200, fg_color="red", command=clicar_excluir).pack(pady=10)
ctk.CTkButton(frame_editar_veiculo, text="Voltar", width=200, fg_color="#444", command=lambda:  [limpar_campos_editar_veiculo(), mostrar_frame(frame_gerenciar_veiculos)]).pack(pady=20)

#TELA GERENCIAR LOCAÇÕES

ctk.CTkLabel(frame_gerenciar_locacoes, text="Gerenciar Locações", font=("Arial", 25, "bold")).pack(pady=20)
ctk.CTkButton(frame_gerenciar_locacoes, text="Registrar locação", width=200, command=lambda:mostrar_frame(frame_registrar_locacao)).pack(pady=10)

ctk.CTkButton(
    frame_gerenciar_locacoes,
    text="Devolução",
    width=200,
    command=lambda: [montar_frame_devolucao(), mostrar_frame(frame_devolucao_locacao)]
).pack(pady=10)
ctk.CTkButton(frame_gerenciar_locacoes, text="Voltar", width=200, fg_color="#444", command = lambda:mostrar_frame(frame_menu)).pack(pady=10)

def gerenciar_locacoes():
    mostrar_frame(frame_gerenciar_locacoes)

#TELA REGISTRAR LOCAÇÃO

def placas_comebox():
    placas=[]
    with open("veiculos.txt","r",encoding="utf-8") as arq:
        for linha in arq:
            linha=linha.strip().split(";")
            placa=linha[3]
            placas.append(placa)
    return placas

lista=placas_comebox()       

scroll_frame = ctk.CTkScrollableFrame(frame_registrar_locacao, width=600, height=500)
scroll_frame.pack(padx=20, pady=20, fill="both", expand=True)

ctk.CTkLabel(scroll_frame, text="Registrar Locações", font=("Arial", 25, "bold")).pack(pady=20)

#dados do veículo
ctk.CTkLabel(scroll_frame , text="Dados do veículo", font=("Arial", 15, "bold")).pack(pady=10)
combobox=ctk.CTkComboBox(scroll_frame , values=lista, width=200)
combobox.set("----Selecione a placa----")
combobox.pack(pady=10)

label_marca=ctk.CTkLabel(scroll_frame , text="Marca: -", font=("Arial", 15, "bold"))
label_marca.pack(anchor="w", padx=20, pady=3)

label_modelo=ctk.CTkLabel(scroll_frame , text="Modelo: -", font=("Arial", 15, "bold"))
label_modelo.pack(anchor="w", padx=20, pady=3)

label_ano=ctk.CTkLabel(scroll_frame , text="Ano: -", font=("Arial", 15, "bold"))
label_ano.pack(anchor="w", padx=20, pady=3)

label_placa=ctk.CTkLabel(scroll_frame , text="Placa: -", font=("Arial", 15, "bold"))
label_placa.pack(anchor="w", padx=20, pady=3)

label_status=ctk.CTkLabel(scroll_frame , text="Status: -", font=("Arial", 15, "bold"))
label_status.pack(anchor="w", padx=20, pady=3)

label_preco=ctk.CTkLabel(scroll_frame , text="Preço por dia(R$): -", font=("Arial", 15, "bold"))
label_preco.pack(anchor="w", padx=20, pady=3)


def exibir_dados_veiculo(placa):
    try:
        with open("veiculos.txt","r",encoding="utf-8") as arq:
            for linha in arq:
                linha=linha.strip().split(";")
                if linha[3]==placa:
                    marca,modelo,ano,placa,status,preco=linha
                    label_marca.configure(text=f"Marca: {marca}")
                    label_modelo.configure(text=f"Modelo: {modelo}")
                    label_ano.configure(text=f"Ano: {ano}")
                    label_placa.configure(text=f"Placa: {placa}")
                    label_status.configure(text=f"Status: {status}")
                    label_preco.configure(text=f"Preço por dia(R$): {preco}")
                    return
    except FileNotFoundError:
        pass

combobox.configure(command=exibir_dados_veiculo)

#datas
ctk.CTkLabel(scroll_frame , text="Dados da locação", font=("Arial", 15, "bold")).pack(pady=10)

# permite usar as datas em qualquer parte do cod
global entrada_retirada, entrada_prevista

entrada_retirada = ctk.CTkEntry(scroll_frame, placeholder_text="Data de retirada (DD/MM/AA)", width=250)
entrada_retirada.pack(pady=10)

entrada_prevista = ctk.CTkEntry(scroll_frame, placeholder_text="Data prevista de devolução (DD/MM/AA)", width=250)
entrada_prevista.pack(pady=10)

#cliente
ctk.CTkLabel(scroll_frame , text="Dados do cliente", font=("Arial", 15, "bold")).pack(pady=10)

entrada_nome=ctk.CTkEntry(scroll_frame , placeholder_text="Nome completo", width=300)
entrada_nome.pack(pady=10)

entrada_cpf=ctk.CTkEntry(scroll_frame , placeholder_text="CPF", width=300)
entrada_cpf.pack(pady=10)

entrada_telefone=ctk.CTkEntry(scroll_frame , placeholder_text="Telefone", width=300)
entrada_telefone.pack(pady=10) 

entrada_email=ctk.CTkEntry(scroll_frame , placeholder_text="Email", width=300)
entrada_email.pack(pady=10)

entrada_endereco=ctk.CTkEntry(scroll_frame , placeholder_text="Endereço", width=300)
entrada_endereco.pack(pady=10)

situacao = ctk.CTkLabel(scroll_frame, text="", text_color="red")
situacao.pack(pady=10)

def limpar_campos_registrar_locacao():
    entrada_nome.delete(0, "end")
    entrada_cpf.delete(0, "end")
    entrada_telefone.delete(0, "end")
    entrada_email.delete(0, "end")
    entrada_endereco.delete(0, "end")
    entrada_retirada.delete(0, "end")
    entrada_prevista.delete(0, "end")
    combobox.set("----Selecione a placa----")
    label_marca.configure(text="Marca: -")
    label_modelo.configure(text="Modelo: -")
    label_ano.configure(text="Ano: -")
    label_placa.configure(text="Placa: -")
    label_status.configure(text="Status: -")
    label_preco.configure(text="Preço por dia (R$): -")
    situacao.configure(text="")




#salvar dados da locação
def registrar_locacao_txt(nome, cpf, telefone, email, endereco, placa, retirada, prevista):
    try:
        with open("locacao.txt", "a", encoding="utf-8") as arq:
            arq.write(f"{nome};{cpf};{telefone};{email};{endereco};{placa};{retirada};{prevista};ATIVA\n")
        return "Cadastrado com sucesso!"
    except:
        return "Erro ao salvar no banco de dados."

#LEMBRAR DE COLOCAR AS RESGRIÇÕES
def clicar_cadastrar_locacao():
    nome = entrada_nome.get()
    cpf = entrada_cpf.get()
    telefone = entrada_telefone.get()
    email = entrada_email.get()
    endereco = entrada_endereco.get()
    placa = combobox.get()

    retirada = entrada_retirada.get().strip()
    prevista = entrada_prevista.get().strip()

    resultado = registrar_locacao_txt(
        nome, cpf, telefone, email, endereco, placa, retirada, prevista
    )

    if resultado == "Cadastrado com sucesso!":
        situacao.configure(text=resultado, text_color="green")
    else:
        situacao.configure(text=resultado, text_color="red")


#botões
ctk.CTkButton(scroll_frame , text="Registrar Locação", width=200, command=clicar_cadastrar_locacao).pack(pady=20)
ctk.CTkButton(scroll_frame , text="Voltar", width=200, fg_color="#444", command=lambda: [limpar_campos_registrar_locacao(), mostrar_frame(frame_gerenciar_locacoes)]).pack(pady=20)
def registrar_locacao():
    mostrar_frame(frame_registrar_locacao)


def registrar_devolucao(cpf):
    linhas_novas = []
    try:
        with open("locacao.txt", "r", encoding="utf-8") as arq:
            for linha in arq:
                dados = linha.strip().split(";")
                if len(dados) < 9:
                    linhas_novas.append(linha) 
                    continue
                nome, cpf_reg, tel, email, end, placa, retirada, prevista, status = dados
                
                if cpf == cpf_reg and status == "ATIVA":
                    nova_linha = f"{nome};{cpf_reg};{tel};{email};{end};{placa};{retirada};{prevista};DEVOLVIDA\n"
                    linhas_novas.append(nova_linha)
                else:
                    linhas_novas.append(linha)
        
        with open("locacao.txt", "w", encoding="utf-8") as arq:
            arq.writelines(linhas_novas)
        return True
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao atualizar registro: {e}")
        return False




def montar_frame_devolucao():
    
    for widget in frame_devolucao_locacao.winfo_children():
        widget.destroy()

    
    ctk.CTkLabel(
        frame_devolucao_locacao,
        text="Devolução de Veículo",
        font=("Arial", 22, "bold")
    ).pack(pady=20)

    
    ctk.CTkLabel(
        frame_devolucao_locacao,
        text="Digite o CPF do Cliente:"
    ).pack()

    entrada_cpf_dev = ctk.CTkEntry(frame_devolucao_locacao, width=250)
    entrada_cpf_dev.pack(pady=10)

    label_erro_dev = ctk.CTkLabel(frame_devolucao_locacao, text="", text_color="red")
    label_erro_dev.pack(pady=5)

    label_info = ctk.CTkLabel(frame_devolucao_locacao, text="", justify="left")
    label_info.pack(pady=10)

    
    
    label_info = ctk.CTkLabel(
        frame_devolucao_locacao,
        text="",
        justify="left",
        font=("Arial", 14)
    )
    label_info.pack(pady=10)

    
    valor_total = ctk.StringVar(value="0.00")
    dias_atraso = ctk.StringVar(value="0")

    limpar_campos_devolucao(entrada_cpf_dev, label_erro_dev, label_info, dias_atraso, valor_total)

    def buscar_devolucao():
        cpf = entrada_cpf_dev.get().strip()

    # Limpa mensagens anteriores
        label_erro_dev.configure(text="")
        label_info.configure(text="")

    # Verifica CPF vazio
        if not cpf:
            label_erro_dev.configure(text="Digite um CPF")
            return

    # Busca locação
        dados = buscar_locacao_por_cpf(cpf)

        if dados is None:
            label_erro_dev.configure(text="Nenhuma locação ativa encontrada.")
            return

    
        retirada = datetime.strptime(dados["retirada"], "%d/%m/%Y").date()
        prevista = datetime.strptime(dados["prevista"], "%d/%m/%Y").date()

        dias_utilizados = (prevista - retirada).days

        if dias_utilizados < 1:
            dias_utilizados = 1  # mínimo 1 dia

    #Pegar o preço do carro
        preco_dia = pegar_preco_por_placa(dados["placa"])

        if preco_dia is None:
            label_erro_dev.configure(text="Erro: preço do veículo não encontrado.")
            return

        #Calcular o total
        preco_final = dias_utilizados * preco_dia
        valor_total.set(f"{preco_final:.2f}")

    
        texto = (
            f"Cliente: {dados['nome']}\n"
            f"Veículo: {dados['marca']}/{dados['modelo']}/{dados['ano']}/{dados['placa']}\n"
            f"Retirada: {dados['retirada']}\n"
            f"Devolução prevista: {dados['prevista']}\n\n"
            f"Resumo:\n"
            f"Dias utilizados: {dias_utilizados}\n"
            f"Total: R$ {valor_total.get()}"
        )

        label_info.configure(text=texto)

       

    ctk.CTkButton(frame_devolucao_locacao, text="Buscar", command=buscar_devolucao).pack(pady=10)

    
    def confirmar_devolucao():
        cpf = entrada_cpf_dev.get().strip()
        registrar_devolucao(cpf)
        messagebox.showinfo("Sucesso", "Devolução registrada!")
        entrada_cpf_dev.delete(0, "end")
        label_info.configure(text="")

    ctk.CTkButton(frame_devolucao_locacao, text="Confirmar", fg_color="green",
                  command=confirmar_devolucao).pack(pady=10)

    
    def cancelar_devolucao():
        entrada_cpf_dev.delete(0, "end")
        label_info.configure(text="")

    ctk.CTkButton(frame_devolucao_locacao, text="Cancelar", fg_color="red",
                  command=cancelar_devolucao).pack(pady=10)

    
    ctk.CTkButton(
    frame_devolucao_locacao,
    text="Voltar",
    command=lambda: [
        limpar_campos_devolucao(entrada_cpf_dev, label_erro_dev, label_info, dias_atraso, valor_total),
        mostrar_frame(frame_gerenciar_locacoes)
    ]
).pack(pady=10)



sistema.mainloop()
