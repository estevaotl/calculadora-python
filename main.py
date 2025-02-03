
from tkinter import *
from tkinter import ttk
from calculadora import calcular_expressao
import config

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=config.COR_PRETA)

frame_tela = Frame(janela, width=235, height=50, bg=config.COR_AZUL)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

todos_valores = ""

def entrar_valores(event):
    global todos_valores
    todos_valores += str(event)
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores

    if "%" in todos_valores:
        try:
            partes = todos_valores.split("%")
            if partes[0] != "":
                valor = float(partes[0])
                resultado = valor * 0.01
                valor_texto.set(str(resultado))
            else:
                valor_texto.set("Erro: Entrada inválida")
        except Exception as e:
            valor_texto.set(f"Erro: {e}")

    else:
        try:
            if todos_valores == "" or todos_valores[-1] in "+-*/%":
                valor_texto.set("Erro: Expressão inválida")
            else:
                resultado = calcular_expressao(todos_valores)
                valor_texto.set(str(resultado))
        except Exception as e:
            valor_texto.set(f"Erro: {e}")

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

valor_texto = StringVar()
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Yvy 18'), bg=config.COR_AZUL, fg=config.COR_BRANCA)
app_label.place(x=0, y=0)

botoes = [
    ("C", 0, 0, 11, 2, config.COR_CINZA, config.COR_PRETA, limpar_tela), 
    ("% ", 118, 0, 5, 2, config.COR_CINZA, config.COR_PRETA, lambda: entrar_valores("%")), 
    ("/", 177, 0, 5, 2, config.COR_LARANJA, config.COR_BRANCA, lambda: entrar_valores("/")),
    ("7", 0, 52, 5, 2, config.COR_CINZA, config.COR_PRETA, lambda: entrar_valores("7")), 
    ("8", 59, 52, 5, 2, config.COR_CINZA, config.COR_PRETA, lambda: entrar_valores("8")), 
    ("9", 118, 52, 5, 2, config.COR_CINZA, config.COR_PRETA, lambda: entrar_valores("9")), 
    ("*", 177, 52, 5, 2, config.COR_LARANJA, config.COR_BRANCA, lambda: entrar_valores("*")),
    ("4", 0, 104, 5, 2, config.COR_CINZA, config.COR_PRETA, lambda: entrar_valores("4")), 
    ("5", 59, 104, 5, 2, config.COR_CINZA, config.COR_PRETA, lambda: entrar_valores("5")), 
    ("6", 118, 104, 5, 2, config.COR_CINZA, config.COR_PRETA, lambda: entrar_valores("6")), 
    ("-", 177, 104, 5, 2, config.COR_LARANJA, config.COR_BRANCA, lambda: entrar_valores("-")),
    ("1", 0, 156, 5, 2, config.COR_CINZA, config.COR_PRETA, lambda: entrar_valores("1")), 
    ("2", 59, 156, 5, 2, config.COR_CINZA, config.COR_PRETA, lambda: entrar_valores("2")), 
    ("3", 118, 156, 5, 2, config.COR_CINZA, config.COR_PRETA, lambda: entrar_valores("3")), 
    ("+", 177, 156, 5, 2, config.COR_LARANJA, config.COR_BRANCA, lambda: entrar_valores("+")),
    ("0", 0, 208, 11, 2, config.COR_CINZA, config.COR_PRETA, lambda: entrar_valores("0")), 
    (".", 118, 208, 5, 2, config.COR_CINZA, config.COR_PRETA, lambda: entrar_valores(".")), 
    ("=", 177, 208, 5, 2, config.COR_LARANJA, config.COR_BRANCA, calcular)
]

for texto, x, y, width, height, cor_fundo_botao, cor_letra, comando in botoes:
    Button(frame_corpo, text=texto, width=width, height=height, bg=cor_fundo_botao, fg=cor_letra, font=('Yvy 13 bold'), relief=RAISED, overrelief=RIDGE, command=comando).place(x=x, y=y)

janela.mainloop()