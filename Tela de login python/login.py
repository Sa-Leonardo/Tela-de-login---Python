import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("600x350")


# Função de Clique

def clique ():
    print("Fazer login")

texto = customtkinter.CTkLabel(janela, text='Fazer login')

email = customtkinter.CTkEntry(janela, placeholder_text="email")

senha = customtkinter.CTkEntry(janela, placeholder_text=('senha'), show="*" )

botao = customtkinter.CTkButton(janela, text='login', command=clique)

texto.pack(padx=20, pady=20)
email.pack(padx=20, pady=20)
senha.pack(padx=20, pady=20)
botao.pack(padx=20, pady=20)

janela .mainloop()


