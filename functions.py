from tkinter import messagebox
from tkinter import *
import pygame

player = 'X'
cor = 'blue'
jog = 'X'

tabuleiro = [0, 0, 0,
             0, 0, 0,
             0, 0, 0]
# 0 - Nulo | 1 - X | 2 - O

def jogada(botão, campo, VezDeQuem, tela):
    global pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9,visor
    visor = tela

    with open('C:\\Users\\KAY\\Documents\\Programa Jogo Da Velha\\Arquivos\\Arquivos Complementares\\XouO.txt', 'r') as arquivo:
        VezDeQuem = arquivo.read()

    if VezDeQuem == 'X':
        cor = 'blue'
    else:
        cor = 'red'

    if campo == 1:
        botão.place_forget()
        font = 'tahoma, 60'
        pos1 = Label(tela, text=VezDeQuem, bg='white', fg=cor, border=0,font=font)
        pos1.place(relx=0.302, rely=0.165, relheight=0.19, relwidth=0.113)
        if VezDeQuem == 'X':
            tabuleiro[0] = 1
        else:
            tabuleiro[0] = 2

        pygame.mixer.init()
        pygame.mixer.music.load('C:\\Users\\KAY\\Documents\\Programa Jogo Da Velha\\Arquivos\\Sons\\Som De Click.mp3')
        pygame.mixer.music.play()

    elif campo == 2:
        botão.place_forget()
        font = 'tahoma, 60'
        pos2 = Label(tela, text=VezDeQuem, bg='white', fg=cor, border=0,font=font)
        pos2.place(relx=0.447, rely=0.168, relheight=0.19, relwidth=0.113)
        if VezDeQuem == 'X':
            tabuleiro[1] = 1
        else:
            tabuleiro[1] = 2

        pygame.mixer.init()
        pygame.mixer.music.load('C:\\Users\\KAY\\Documents\\Programa Jogo Da Velha\\Arquivos\\Sons\\Som De Click.mp3')
        pygame.mixer.music.play()

    elif campo == 3:
        botão.place_forget()
        font = 'tahoma, 60'
        pos3 = Label(tela, text=VezDeQuem, bg='white', fg=cor, border=0,font=font)
        pos3.place(relx=0.59, rely=0.168, relheight=0.19, relwidth=0.113)
        if VezDeQuem == 'X':
            tabuleiro[2] = 1
        else:
            tabuleiro[2] = 2
        pygame.mixer.init()
        pygame.mixer.music.load('C:\\Users\\KAY\\Documents\\Programa Jogo Da Velha\\Arquivos\\Sons\\Som De Click.mp3')
        pygame.mixer.music.play()

    elif campo == 4:
        botão.place_forget()
        font = 'tahoma, 60'
        pos4 = Label(tela, text=VezDeQuem, bg='white', fg=cor, border=0,font=font)
        pos4.place(relx=0.31, rely=0.41, relheight=0.19, relwidth=0.113)
        if VezDeQuem == 'X':
            tabuleiro[3] = 1
        else:
            tabuleiro[3] = 2

        pygame.mixer.init()
        pygame.mixer.music.load('C:\\Users\\KAY\\Documents\\Programa Jogo Da Velha\\Arquivos\\Sons\\Som De Click.mp3')
        pygame.mixer.music.play()

    elif campo == 5:
        botão.place_forget()
        font = 'tahoma, 60'
        pos5 = Label(tela, text=VezDeQuem, bg='white', fg=cor, border=0,font=font)
        pos5.place(relx=0.445, rely=0.41, relheight=0.19, relwidth=0.113)
        if VezDeQuem == 'X':
            tabuleiro[4] = 1
        else:
            tabuleiro[4] = 2

        pygame.mixer.init()
        pygame.mixer.music.load('C:\\Users\\KAY\\Documents\\Programa Jogo Da Velha\\Arquivos\\Sons\\Som De Click.mp3')
        pygame.mixer.music.play()

    elif campo == 6:
        botão.place_forget()
        font = 'tahoma, 60'
        pos6 = Label(tela, text=VezDeQuem, bg='white', fg=cor, border=0,font=font)
        pos6.place(relx=0.583, rely=0.41, relheight=0.19, relwidth=0.113)
        if VezDeQuem == 'X':
            tabuleiro[5] = 1
        else:
            tabuleiro[5] = 2

        pygame.mixer.init()
        pygame.mixer.music.load('C:\\Users\\KAY\\Documents\\Programa Jogo Da Velha\\Arquivos\\Sons\\Som De Click.mp3')
        pygame.mixer.music.play()

    elif campo == 7:
        botão.place_forget()
        font = 'tahoma, 60'
        pos7 = Label(tela, text=VezDeQuem, bg='white', fg=cor, border=0,font=font)
        pos7.place(relx=0.304, rely=0.65, relheight=0.19, relwidth=0.113)
        if VezDeQuem == 'X':
            tabuleiro[6] = 1
        else:
            tabuleiro[6] = 2

        pygame.mixer.init()
        pygame.mixer.music.load('C:\\Users\\KAY\\Documents\\Programa Jogo Da Velha\\Arquivos\\Sons\\Som De Click.mp3')
        pygame.mixer.music.play()

    elif campo == 8:
        botão.place_forget()
        font = 'tahoma, 60'
        pos8 = Label(tela, text=VezDeQuem, bg='white', fg=cor, border=0,font=font)
        pos8.place(relx=0.445, rely=0.65, relheight=0.19, relwidth=0.113)
        if VezDeQuem == 'X':
            tabuleiro[7] = 1
        else:
            tabuleiro[7] = 2

        pygame.mixer.init()
        pygame.mixer.music.load('C:\\Users\\KAY\\Documents\\Programa Jogo Da Velha\\Arquivos\\Sons\\Som De Click.mp3')
        pygame.mixer.music.play()

    elif campo == 9:
        botão.place_forget()
        font = 'tahoma, 60'
        pos9 = Label(tela, text=VezDeQuem, bg='white', fg=cor, border=0,font=font)
        pos9.place(relx=0.586, rely=0.65, relheight=0.19, relwidth=0.113)
        if VezDeQuem == 'X':
            tabuleiro[8] = 1
        else:
            tabuleiro[8] = 2

        pygame.mixer.init()
        pygame.mixer.music.load('C:\\Users\\KAY\\Documents\\Programa Jogo Da Velha\\Arquivos\\Sons\\Som De Click.mp3')
        pygame.mixer.music.play()
        
    if VezDeQuem == 'X':
        jog = 'O'
    else:
        jog = 'X'

    with open('C:\\Users\\KAY\\Documents\\Programa Jogo Da Velha\\Arquivos\\Arquivos Complementares\\XouO.txt', 'w') as arquivo:
        arquivo.write(jog)

    situacao = verificar_vitoria(tabuleiro)
    if situacao == 'Em andamento':
        pass
    elif situacao == 'Velha':
        action('velha')
    elif situacao == 1:
        action('X')
    elif situacao == 2:
        action('O')
    
def verificar_vitoria(tabuleiro):
    # Verificar linhas e colunas
    for i in range(3):
        # Verificar linhas
        if tabuleiro[i * 3] == tabuleiro[i * 3 + 1] == tabuleiro[i * 3 + 2] != 0:
            return tabuleiro[i * 3]

        # Verificar colunas
        if tabuleiro[i] == tabuleiro[i + 3] == tabuleiro[i + 6] != 0:
            return tabuleiro[i]

    # Verificar diagonais
    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] != 0:
        return tabuleiro[0]
    if tabuleiro[2] == tabuleiro[4] == tabuleiro[6] != 0:
        return tabuleiro[2]

    # Verificar empate (velha)
    if 0 not in tabuleiro:
        return "Velha"

    # O jogo está em andamento
    return "Em andamento"

def action(ação):
    global ximg, oimg, vimg
    if ação == 'X':
        for widget in visor.winfo_children():
            widget.destroy()
        ximg =PhotoImage(file='C:\\Users\\KAY\\Documents\\Programa Jogo Da Velha\\Arquivos\\Imagens\\xganhou.png')
        xganhou = Label(visor, image=ximg)
        xganhou.place(relx=0.0)

        pygame.mixer.init()
        pygame.mixer.music.load('C:\\Users\\KAY\\Documents\\Programa Jogo Da Velha\\Arquivos\\Sons\\win.wav')
        pygame.mixer.music.play()

        visor.after(2000, reiniciar)
    elif ação == 'O':
        for widget in visor.winfo_children():
            widget.destroy()
        oimg =PhotoImage(file='C:\\Users\\KAY\\Documents\\Programa Jogo Da Velha\\Arquivos\\Imagens\\oganhou.png')
        oganhou = Label(visor, image=oimg)
        oganhou.place(relx=0.0)

        pygame.mixer.init()
        pygame.mixer.music.load('C:\\Users\\KAY\\Documents\\Programa Jogo Da Velha\\Arquivos\\Sons\\win.wav')
        pygame.mixer.music.play()

        visor.after(2000, reiniciar)
    elif ação == 'velha':
        for widget in visor.winfo_children():
            widget.destroy()
        vimg =PhotoImage(file='C:\\Users\\KAY\\Documents\\Programa Jogo Da Velha\\Arquivos\\Imagens\\velha.png')
        velha = Label(visor, image=vimg)
        velha.place(relx=0.0)

        pygame.mixer.init()
        pygame.mixer.music.load('C:\\Users\\KAY\\Documents\\Programa Jogo Da Velha\\Arquivos\\Sons\\derrota.mp3')
        pygame.mixer.music.play()

        visor.after(2000, reiniciar)

def reiniciar():
    global file,label,botão1,botão2,botão3,botão4,botão5,botão6,botão7,botão8,botão9,VezDeX,situacao

    tabuleiro = [0, 0, 0,
                 0, 0, 0,
                 0, 0, 0]
    for widget in visor.winfo_children():
        widget.destroy()
    with open('C:\\Users\\KAY\\Documents\\Programa Jogo Da Velha\\Arquivos\\Arquivos Complementares\\XouO.txt', 'r') as arquivo:
        VezDeX = arquivo.read()

    file = PhotoImage(file='C:\\Users\\KAY\\Documents\\Programa Jogo Da Velha\\Arquivos\\Imagens\\Tabuleiro.png')
    label = Label(visor, image=file)
    label.place(relx=0.0)

    botão1 = Button(visor, bg='white', border=0, activebackground='white', command=lambda: jogada(botão1, 1, VezDeX, visor))
    botão1.place(relx=0.302, rely=0.165, relheight=0.19, relwidth=0.113)

    botão2 = Button(visor, bg='white', border=0, activebackground='white', command=lambda: jogada(botão2, 2, VezDeX, visor))
    botão2.place(relx=0.447, rely=0.168, relheight=0.19, relwidth=0.113)

    botão3 = Button(visor, bg='white', border=0, activebackground='white', command=lambda: jogada(botão3, 3, VezDeX, visor))
    botão3.place(relx=0.59, rely=0.168, relheight=0.19, relwidth=0.113)

    botão4 = Button(visor, bg='white', border=0, activebackground='white', command=lambda: jogada(botão4, 4, VezDeX, visor))
    botão4.place(relx=0.31, rely=0.41, relheight=0.19, relwidth=0.113)

    botão5 = Button(visor, bg='white', border=0, activebackground='white', command=lambda: jogada(botão5, 5, VezDeX, visor))
    botão5.place(relx=0.445, rely=0.41, relheight=0.19, relwidth=0.113)

    botão6 = Button(visor, bg='white', border=0, activebackground='white', command=lambda: jogada(botão6, 6, VezDeX, visor))
    botão6.place(relx=0.583, rely=0.41, relheight=0.19, relwidth=0.113)

    botão7 = Button(visor, bg='white', border=0, activebackground='white', command=lambda: jogada(botão7, 7, VezDeX, visor))
    botão7.place(relx=0.304, rely=0.65, relheight=0.19, relwidth=0.113)

    botão8 = Button(visor, bg='white', border=0, activebackground='white', command=lambda: jogada(botão8, 8, VezDeX, visor))
    botão8.place(relx=0.445, rely=0.65, relheight=0.19, relwidth=0.113)

    botão9 = Button(visor, bg='white', border=0, activebackground='white', command=lambda: jogada(botão9, 9, VezDeX, visor))
    botão9.place(relx=0.586, rely=0.65, relheight=0.19, relwidth=0.113)
    
