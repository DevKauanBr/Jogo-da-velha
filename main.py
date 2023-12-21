#Importações
from tkinter import *
from funções import jogada

#Configurações Gerais
tela = Tk()
tela.geometry('700x400')
tela.title('Jogo Da Velha')
tela.resizable(False, False)

with open('C:\\Users\\KAY\\Documents\\Programa Jogo Da Velha\\Arquivos\\Arquivos Complementares\\XouO.txt', 'r') as arquivo:
    VezDeX = arquivo.read()


#Widgets
file = PhotoImage(file='C:\\Users\\KAY\\Documents\\Programa Jogo Da Velha\\Arquivos\\Imagens\\Tabuleiro.png')
label = Label(tela, image=file)
label.place(relx=0.0)

botão1 = Button(tela, bg='white', border=0, activebackground='white', command=lambda: jogada(botão1, 1, VezDeX, tela))
botão1.place(relx=0.302, rely=0.165, relheight=0.19, relwidth=0.113)

botão2 = Button(tela, bg='white', border=0, activebackground='white', command=lambda: jogada(botão2, 2, VezDeX, tela))
botão2.place(relx=0.447, rely=0.168, relheight=0.19, relwidth=0.113)

botão3 = Button(tela, bg='white', border=0, activebackground='white', command=lambda: jogada(botão3, 3, VezDeX, tela))
botão3.place(relx=0.59, rely=0.168, relheight=0.19, relwidth=0.113)

botão4 = Button(tela, bg='white', border=0, activebackground='white', command=lambda: jogada(botão4, 4, VezDeX, tela))
botão4.place(relx=0.31, rely=0.41, relheight=0.19, relwidth=0.113)

botão5 = Button(tela, bg='white', border=0, activebackground='white', command=lambda: jogada(botão5, 5, VezDeX, tela))
botão5.place(relx=0.445, rely=0.41, relheight=0.19, relwidth=0.113)

botão6 = Button(tela, bg='white', border=0, activebackground='white', command=lambda: jogada(botão6, 6, VezDeX, tela))
botão6.place(relx=0.583, rely=0.41, relheight=0.19, relwidth=0.113)

botão7 = Button(tela, bg='white', border=0, activebackground='white', command=lambda: jogada(botão7, 7, VezDeX, tela))
botão7.place(relx=0.304, rely=0.65, relheight=0.19, relwidth=0.113)

botão8 = Button(tela, bg='white', border=0, activebackground='white', command=lambda: jogada(botão8, 8, VezDeX, tela))
botão8.place(relx=0.445, rely=0.65, relheight=0.19, relwidth=0.113)

botão9 = Button(tela, bg='white', border=0, activebackground='white', command=lambda: jogada(botão9, 9, VezDeX, tela))
botão9.place(relx=0.586, rely=0.65, relheight=0.19, relwidth=0.113)

tela.mainloop()
