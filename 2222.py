import customtkinter as ctk

# Configuração geral
ctk.set_appearance_mode("dark")        # "dark" ou "light"
ctk.set_default_color_theme("blue")    # "blue", "green" ou "dark-blue"

# Criar janela
app = ctk.CTk()
app.title("Sistema de Locadora de Veículos")
app.geometry("900x600")
app.resizable(False, False)  # para não distorcer

# === MENU LATERAL ===
menu_frame = ctk.CTkFrame(app, width=200, corner_radius=0)
menu_frame.pack(side="left", fill="y")

titulo_menu = ctk.CTkLabel(menu_frame, text="MENU", font=("Arial", 20, "bold"))
titulo_menu.pack(pady=20)

btn1 = ctk.CTkButton(menu_frame, text="Funcionários")
btn1.pack(pady=10)

btn2 = ctk.CTkButton(menu_frame, text="Veículos")
btn2.pack(pady=10)

btn3 = ctk.CTkButton(menu_frame, text="Locações")
btn3.pack(pady=10)

# === ÁREA PRINCIPAL ===
main_frame = ctk.CTkFrame(app)
main_frame.pack(side="right", fill="both", expand=True)

titulo = ctk.CTkLabel(main_frame, text="Bem-vindo ao Sistema", font=("Arial", 24, "bold"))
titulo.pack(pady=40)

app.mainloop()