import tkinter as tk
from tkinter import filedialog
import fdb
import main
import xml.etree.ElementTree as ET

# Cria a janela principal
janela = tk.Tk()

# Define o tamanho da janela
janela.geometry("700x100")

# Define o título da janela
janela.title("Minha Janela")

# Define a função que será chamada ao clicar no botão de seleção do banco de dados
def selecionar_bd(campo_bd):
    caminho_bd = filedialog.askopenfilename(filetypes=[("Banco de Dados", "*.fdb")])
    campo_bd.delete(0, tk.END)  # Limpa o conteúdo do campo de texto
    campo_bd.insert(0, caminho_bd)  # Insere o caminho do arquivo selecionado no campo de texto
    return caminho_bd

# Define a função que será chamada ao clicar no botão de seleção do arquivo XML
def selecionar_xml(campo_xml):
    caminho_xml = filedialog.askopenfilename(filetypes=[("Arquivo XML", "*.xml")])
    campo_xml.delete(0, tk.END)  # Limpa o conteúdo do campo de texto
    campo_xml.insert(0, caminho_xml)  # Insere o caminho do arquivo selecionado no campo de texto
    return caminho_xml

def confirmar(campo_bd, campo_xml):
    caminho_bd = campo_bd.get()
    caminho_xml = campo_xml.get()
    
    # Define a string de conexão com o banco de dados com o caminho obtido da interface
    conexao_destino = fdb.connect(dsn=f"{caminho_bd}", user='FSCSCPI8', password='scpi',
                              port=3050, charset='WIN1252', fb_library_name='C:\\Program Files\\Firebird\\Firebird_2_5\\bin\\fbclient.dll')
    
    def commit():
        conexao_destino.commit()
    
    # Chama a função de leitura do arquivo XML do módulo main
    tree = ET.parse(caminho_xml)
    root = tree.getroot()
    main.ler_xml(root)

# Cria o campo para o caminho do banco de dados
frame_bd = tk.Frame(janela)
frame_bd.pack(fill=tk.X, padx=10, pady=10)

label_bd = tk.Label(frame_bd, text="Caminho do Banco de Dados:")
label_bd.pack(side=tk.LEFT)

campo_bd = tk.Entry(frame_bd, width=30)
campo_bd.pack(side=tk.LEFT)

botao_bd = tk.Button(frame_bd, text="Selecionar", command=lambda: selecionar_bd(campo_bd))
botao_bd.pack(side=tk.LEFT)

# Cria o campo para o caminho do arquivo XML
frame_xml = tk.Frame(janela)
frame_xml.pack(fill=tk.X, padx=10, pady=10)

label_xml = tk.Label(frame_xml, text="Caminho do Arquivo XML:")
label_xml.pack(side=tk.LEFT)

campo_xml = tk.Entry(frame_xml, width=30)
campo_xml.pack(side=tk.LEFT)

botao_xml = tk.Button(frame_xml, text="Selecionar", command=lambda: selecionar_xml(campo_xml))
botao_xml.pack(side=tk.LEFT)
# Inicia o loop principal da janela
janela.mainloop()