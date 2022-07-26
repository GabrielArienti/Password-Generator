from tabnanny import check
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import string
import random
from tkinter import messagebox

# Cores
cor_branco = "#fafafa"
cor_preto = "#0d0d0d"
cor_amarelo = "#f2e200"
cor_vermelho = "#d10902"
cor_azul = "#010963"

# Janela
janela = Tk()
janela.title("Password Gen")
janela.geometry("295x370")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor_branco)
janela.attributes("-alpha", 0.95)

estilo = ttk.Style(janela)
estilo.theme_use('alt')

# Frames do app

frame_cima = Frame(janela, width=295, height=50,
                   bg=cor_branco, pady=0, padx=0, relief=FLAT)
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=320,
                    bg=cor_branco, pady=0, padx=0, relief=FLAT)
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# Frame cima

img = Image.open('iconpass.png')
img = img.resize((50, 50), Image.LANCZOS)
img = ImageTk.PhotoImage(img)

app_logo = Label(frame_cima, height=60, image=img,
                 compound=LEFT, padx=20, pady=20, relief=FLAT, anchor=NW, bg=cor_branco)
app_logo.grid(row=0, column=0, sticky=NSEW)

app_nome = Label(frame_cima, text="Password Generator",
                 font="Raleway 16 bold", compound=LEFT, padx=10, pady=15, relief=FLAT, anchor=NW, bg=cor_branco, fg=cor_preto)
app_nome.grid(row=0, column=1, sticky=NSEW)

app_linha = Label(frame_cima, text="", width=295, height=1,
                  font="1", relief=FLAT, bg=cor_azul)
app_linha.place(x=0, y=60)


# Estados checkbox
estado1 = StringVar()
estado1.set(FALSE)

estado2 = StringVar()
estado2.set(FALSE)

estado3 = StringVar()
estado3.set(FALSE)

estado4 = StringVar()
estado4.set(FALSE)


# Função gerar senha


def gerar():
    alfabeto_maior = string.ascii_uppercase
    alfabeto_menor = string.ascii_lowercase
    numeros = '123456789'
    simbolos = '!@#*&$%'
    vazio = ""

    global combinar
    combinar = vazio

    # condição maíscula
    if estado1.get() == alfabeto_maior:
        combinar = alfabeto_maior
    else:
        pass

     # condição minúscula
    if estado2.get() == alfabeto_menor:
        combinar = combinar + alfabeto_menor
    else:
        pass

    # condição número
    if estado3.get() == numeros:
        combinar = combinar + numeros
    else:
        pass

    # condição símbolos
    if estado4.get() == simbolos:
        combinar = combinar + simbolos
    else:
        pass

    comprimento = int(spin.get())
    senha = "".join(random.sample(combinar, comprimento))
    app_senha['text'] = senha

    def copiar():
        info = senha
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)
        messagebox.showinfo('Concluído', 'Senha copiada')
    botao_copiar = Button(frame_baixo, text="Copiar", font="Raleway 10 bold",
                          width=6, height=1, padx=10, pady=12, relief=FLAT, overrelief=RAISED, bg=cor_azul, fg=cor_branco, command=copiar)
    botao_copiar.place(x=210, y=20)


# Frame baixo
app_senha = Label(frame_baixo, text="---", width=20, height=1,
                  font="Raleway 10 bold", compound=LEFT, padx=10, pady=15, relief=SOLID, anchor=CENTER, bg=cor_branco, fg=cor_preto)
app_senha.place(x=15, y=20)


app_caract = Label(frame_baixo, text="Número de caracteres", height=1,
                   font="Raleway 10 italic", relief=FLAT, compound=LEFT, anchor=NE, bg=cor_branco, fg=cor_preto)
app_caract.place(x=70, y=98)

# Spin de caracteres

var = IntVar()
var.set(6)
spin = Spinbox(frame_baixo, from_=3, to=15, width=2, textvariable=var)
spin.place(x=15, y=100)

# Listas de variáveis do gerador de senha

alfabeto_maior = string.ascii_uppercase
alfabeto_menor = string.ascii_lowercase
numeros = '123456789'
simbolos = '!@#*&$%'

# Letras Maiúsculas

check_upper = Checkbutton(frame_baixo, width=1, var=estado1,
                          onvalue=alfabeto_maior, offrelief=FLAT, offvalue='off', bg=cor_branco)
check_upper.place(x=11, y=130)

app_upper = Label(frame_baixo, text="ABC Letras maiúsculas", height=1,
                  font="Raleway 10 italic", relief=FLAT, compound=LEFT, anchor=NE, bg=cor_branco, fg=cor_preto)
app_upper.place(x=70, y=131)


# Letras Minúsculas

check_lower = Checkbutton(frame_baixo, width=1, var=estado2,
                          onvalue=alfabeto_menor, offrelief=FLAT, offvalue='off', bg=cor_branco)
check_lower.place(x=11, y=160)

app_lower = Label(frame_baixo, text="abc Letras minúsculas", height=1,
                  font="Raleway 10 italic", relief=FLAT, compound=LEFT, anchor=NE, bg=cor_branco, fg=cor_preto)
app_lower.place(x=70, y=161)


# Números

check_numeros = Checkbutton(frame_baixo, width=1, var=estado3,
                            onvalue=numeros, offrelief=FLAT, offvalue='off', bg=cor_branco)
check_numeros.place(x=11, y=190)

app_numeros = Label(frame_baixo, text="123 Números", height=1,
                    font="Raleway 10 italic", relief=FLAT, compound=LEFT, anchor=NE, bg=cor_branco, fg=cor_preto)
app_numeros.place(x=70, y=191)


# Símbolos

check_simbolos = Checkbutton(frame_baixo, width=1, var=estado4,
                             onvalue=simbolos, offrelief=FLAT, offvalue='off', bg=cor_branco)
check_simbolos.place(x=11, y=220)

app_simbolos = Label(frame_baixo, text="!@# Símbolos", height=1,
                     font="Raleway 10 italic", relief=FLAT, compound=LEFT, anchor=NE, bg=cor_branco, fg=cor_preto)
app_simbolos.place(x=70, y=221)


# Botão gerar e copiar

botao_gerar = Button(frame_baixo, text="Gerar Senha", font="Raleway 12 bold",
                     width=15, height=1, relief=FLAT, overrelief=RAISED, bg=cor_azul, fg=cor_branco, command=gerar)
botao_gerar.place(x=68, y=260)


botao_copiar = Button(frame_baixo, text="Copiar", font="Raleway 10 bold",
                      width=6, height=1, padx=10, pady=12, relief=FLAT, overrelief=RAISED, bg=cor_azul, fg=cor_branco)
botao_copiar.place(x=210, y=20)


janela.mainloop()
