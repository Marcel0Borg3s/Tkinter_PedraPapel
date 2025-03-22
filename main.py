import tkinter as tk
from tkinter import LabelFrame, Label, Button

def escolha_pedra():
    jokenpo(escolha="Pedra")

def escolha_papel():
    jokenpo(escolha="Papel")

def escolha_tesoura():
    jokenpo(escolha="Tesoura")

def jokenpo(escolha):
    from random import choice

    opcoes = ["Pedra", "Papel", "Tesoura"]
    escolha_pc = choice(opcoes)

    if escolha == escolha_pc:
        resultado["text"] = f"Você escolheu {escolha} e minha opção foi: {escolha_pc}. Empatamos!"
    elif (escolha == "Pedra" and escolha_pc == "Tesoura") or (escolha == "Papel" and escolha_pc == "Pedra") or (escolha == "Tesoura" and escolha_pc == "Papel"):
        resultado["text"] = f"Você escolheu {escolha} e minha opção foi: {escolha_pc}. Você ganhou!"
    else:
        resultado["text"] = f"Você escolheu {escolha} e minha opção foi: {escolha_pc}. Você perdeu!"
        

# Criando a janela
janela = tk.Tk()
janela.title("Jokenpô")
janela.geometry("600x400+1400+600")

# Criando os elementos da janela
frame = LabelFrame(janela, text="Escolha uma opção")
frame.pack()

# flaticon.com
icone_pedra = tk.PhotoImage(file=r"E:\Programer\Python\Projetos\Tkinter_PedraPapel\images\rock.png")
icone_papel = tk.PhotoImage(file=r"E:\Programer\Python\Projetos\Tkinter_PedraPapel\images\paper.png")
icone_tesoura = tk.PhotoImage(file=r"E:\Programer\Python\Projetos\Tkinter_PedraPapel\images\scissor.png")

Button(frame, text="Pedra", command=escolha_pedra, image=icone_pedra, compound=tk.TOP, width=50, height=50).grid(row=3, column=0, padx=10, pady=10)
Button(frame, text="Papel", command=escolha_papel, image=icone_papel, compound=tk.TOP, width=50, height=50).grid(row=3, column=1, padx=10, pady=10) 
Button(frame, text="Tesoura", command=escolha_tesoura, image=icone_tesoura, compound=tk.TOP, width=50, height=50).grid(row=3, column=2, padx=10, pady=10)



resultado = Label(frame, padx=10, pady=10)
resultado.grid(row=4, column=0, columnspan=3)




janela.mainloop()