import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import functions
import os

global saida
global entrada
global base_file

saida = ""
entrada = ""
base_file = ""

def selecionar_arquivo():
    global entrada
    # Abrir uma janela de seleção de arquivo
    arquivo = filedialog.askopenfilename(initialdir="/", title="Selecione um arquivo")

    # Atualizar o texto da label com o caminho do arquivo selecionado
    label_arquivo["text"] = arquivo
    entrada = arquivo

def selecionar_diretorio_saida():
    global saida
    # Abrir uma janela de seleção de diretório
    diretorio_saida = filedialog.askdirectory(initialdir=os.getcwd(), title="Selecione um diretório de saída")

    # Atualizar o texto da label com o caminho do diretório de saída selecionado
    label_diretorio_saida["text"] = diretorio_saida
    saida = diretorio_saida

def selecionar_arquivo_base():
    global base_file
    # Abrir uma janela de seleção de arquivo
    arquivo_base = filedialog.askopenfilename(initialdir=os.getcwd(), title="Selecione um arquivo base")

    # Atualizar o texto da label com o caminho do arquivo base selecionado
    label_arquivo_base["text"] = arquivo_base
    base_file = arquivo_base

def funcao_executar():
    global entrada
    global saida
    global base_file
    functions.do_replacement(entrada, saida, base_file)

# Criar uma instância da janela
janela = tk.Tk()
janela.title("Selecionar Arquivo e Diretório de Saída")

# Definir tamanho da janela
largura_janela = 400
altura_janela = 400

# Obter a largura e altura da tela do dispositivo
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

# Calcular a posição x e y para centralizar a janela
posicao_x = (largura_tela - largura_janela) // 2
posicao_y = (altura_tela - altura_janela) // 2

# Definir tamanho e posição da janela
janela.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

# Carregar o arquivo de estilo
janela.style = ttk.Style()
janela.style.theme_use("default")

# Criar um estilo personalizado para os botões
janela.style.configure("TButton", padding=6, relief="flat", foreground="white", borderwidth=1, bordercolor="white")
janela.style.map("Custom.TButton", background=[("active", "#6F42C1"), ("pressed", "#6F42C1"), ("!active", "#6F42C1")])

# Criar um estilo para o botão azul
janela.style.configure("Blue.TButton", padding=6, relief="flat", foreground="white", borderwidth=1, bordercolor="white")
janela.style.map("Blue.TButton", background=[("active", "#007BFF"), ("pressed", "#007BFF"), ("!active", "#007BFF")])

# Criar um estilo para as labels
janela.style.configure("TLabel", background="white", foreground="#6F42C1")

# Criar um frame para organizar os widgets
frame = ttk.Frame(janela, padding="20")
frame.grid(row=0, column=0)

# Labels
label_arquivo_texto = ttk.Label(frame, text="Certificado de modelo(.pptx)", style="TLabel")
label_arquivo_texto.grid(row=0, column=0, padx=5, pady=5, sticky="w")
label_diretorio_saida_texto = ttk.Label(frame, text="Diretório de saída", style="TLabel")
label_diretorio_saida_texto.grid(row=1, column=0, padx=5, pady=5, sticky="w")
label_arquivo_base_texto = ttk.Label(frame, text="Lista de pessoas(.csv)", style="TLabel")
label_arquivo_base_texto.grid(row=2, column=0, padx=5, pady=5, sticky="w")

# Botões
botao_selecionar_arquivo = ttk.Button(frame, text="Selecionar Arquivo", command=selecionar_arquivo, style="Custom.TButton")
botao_selecionar_arquivo.grid(row=0, column=1, padx=5, pady=5)
botao_selecionar_diretorio_saida = ttk.Button(frame, text="Selecionar Arquivo", command=selecionar_diretorio_saida, style="Custom.TButton")
botao_selecionar_diretorio_saida.grid(row=1, column=1, padx=5, pady=5)
botao_selecionar_arquivo_base = ttk.Button(frame, text="Selecionar Arquivo", command=selecionar_arquivo_base, style="Custom.TButton")
botao_selecionar_arquivo_base.grid(row=2, column=1, padx=5, pady=5)
botao_executar = ttk.Button(frame, text="Executar Função", command=funcao_executar, style="Blue.TButton")
botao_executar.grid(row=3, column=1, padx=5, pady=5)

# Labels com o caminho selecionado
label_arquivo = ttk.Label(frame, text="", wraplength=400, style="TLabel")
label_arquivo.grid(row=0, column=2, padx=5, pady=5)
label_diretorio_saida = ttk.Label(frame, text="", wraplength=400, style="TLabel")
label_diretorio_saida.grid(row=1, column=2, padx=5, pady=5)
label_arquivo_base = ttk.Label(frame, text="", wraplength=400, style="TLabel")
label_arquivo_base.grid(row=2, column=2, padx=5, pady=5)

# Loop principal para manter a janela aberta
janela.mainloop()
