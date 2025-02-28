from tkinter import * #Importa todos os mudulos do tkinter
from tkinter import messagebox # Importar o mudulo de widgets tematicos do tkinter
from Database import Database

# Criar a janela
jan = Tk()
jan.title("SL Systens - Painel de Acesso")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)

# COMANDO PARA DEIXAR A TELA TRANSPARENTE
jan.attributes("alpha", 0.9) # Define a transparência da janela (0.0 a 1.0)

# DEFINIR ÍCONE DA JANELA
jan.iconbitmap(default="icons/1LogoIcon.ico") # Define o ícone da janela

# CARREGAR IMAGEM
logo = PhotoImage(file="icons/LogoSergio.png") # Carrega a imagem do logo

# CRIAR FRAME
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise") # Cria um frame à esquerda
LeftFrame.pack(side=LEFT) # Posiciona o frame à esquerda

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise") # Cria um frame à direita
RightFrame.pack(side=RIGHT) # Posiciona o frame à direita

# ADICIONAR LOGO
LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE") # Cria um label para a imagem do logo
LogoLabel.place(x=50, y=100) # Posiciona o label no frame esquerdo

# ADICIONAR CAMPOS DE USUÁRIO E SENHA
UsuarioLabel = Label(RightFrame, text="Usuário:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
# Cria um label para o usuário
UsuarioLabel.place(x=5, y=100) # Posiciona o label no frame direito

UsuarioEntry = ttk.Entry(RightFrame, width=30) # Cria um campo de entrada para o usuário

UsuarioEntry.place(x=120, y=115) # Posiciona o campo de entrada

SenhaLabel = Label(RightFrame, text="Senha:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
# Cria um label para a senha
SenhaLabel.place(x=5, y=150) # Posiciona o label no frame direito

SenhaEntry = ttk.Entry(RightFrame, width=30, show="*")
#Cria um campo de entrada para a senha
SenhaEntry.place(x=120, y=165) # Posiciona o campo de entrada

# FUNÇÃO DE LOGIN
def Login():
    usuario = UsuarioEntry.get() # Obtém o valor do campo de entrada do usuário
    senha = SenhaEntry.get() # Obtém o valor do campo de entrada da senha

# Conectar ao banco de dados
db = Database() # Cria uma instância da classe Database
db.cursor.execute("""
SELECT * FROM usuario1
WHERE usuario = %s AND senha = %s""", (usuario, senha))
# Executa a consulta SQL para verificar o usuário e a senha
VerifyLogin = db.cursor.fetchone() # Obtém o resultado da consulta

# Verificar se o usuário foi encontrado
if VerifyLogin:
    messagebox.showinfo(title="INFO LOGIN", message="Acesso Confirmado. Bem Vindo!")
# Exibe mensagem de sucesso
else:
    messagebox.showinfo(title="INFO LOGIN", message="Acesso Negado. Verifique se está cadastrado no Sistema ") #Exibe mensagem de erro

# CRIANDO BOTÕES
LoginButton = ttk.Button(RightFrame, text="LOGIN", width=15, command=Login) # Cria um botão de login
LoginButton.place(x=150, y=225) # Posiciona o botão de login

# FUNÇÃO PARA REGISTRAR NOVO USUÁRIO

# REMOVENDO BOTÕES DE LOGIN
LoginButton.place(x=5000) # Move o botão de login para fora da tela
RegisterButton.place(x=5000) # Move o botão de registro para fora da tela

# INSERINDO WIDGETS DE CADASTRO
NomeLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
# Cria um label para o nome
NomeLabel.place(x=5, y=5) # Posiciona o label no frame direito

NomeEntry = ttk.Entry(RightFrame, width=30) # Cria um campo de entrada para o nome
NomeEntry.place(x=120, y=20) # Posiciona o campo de entrada

EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
# Cria um label para o email
EmailLabel.place(x=5, y=40) # Posiciona o label no frame direito

EmailEntry = ttk.Entry(RightFrame, width=30) # Cria um campo de entrada para o email
EmailEntry.place(x=120, y=55) # Posiciona o campo de entrada

# FUNÇÃO PARA REGISTRAR NO BANCO DE DADOS
def RegistrarNoBanco():
    nome = NomeEntry.get() # Obtém o valor do

