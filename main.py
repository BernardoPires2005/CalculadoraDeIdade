from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date

janela = Tk()
janela.title("")
janela.geometry('310x400')

# cores
cor1 = '#000000' #Preto
cor2 = '#3b3b3b' #Cinza
cor3 = '#ffffff' #Branco
cor4 = '#fcc058' #laranja

# Criando Frames
frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0, relief=FLAT, bg=cor1)
frame_cima.grid(row=0, column=0)
frame_baixo = Frame(janela, width=310, height=260, pady=0, padx=0, relief=FLAT, bg=cor2)
frame_baixo.grid(row=1, column=0)

# Função para calcular idade
def calcular():
    inicial = cal_1.get()
    final = cal_2.get()

    # separando os valores e atributos
    mes_1, dia_1, ano_1 = [int(f) for f in inicial.split('/')]
    data_inicial = date(ano_1, mes_1, dia_1)

    mes_2, dia_2, ano_2 = [int(f) for f in final.split('/')]
    data_nascimento = date(ano_2, mes_2, dia_2)

    anos = relativedelta(data_inicial, data_nascimento).years
    meses = relativedelta(data_inicial, data_nascimento).months
    dias = relativedelta(data_inicial, data_nascimento).days

    l_anos['text'] = anos
    l_meses['text'] = meses
    l_dias['text'] = dias


# Criando Labels para frame de cima
l_calculadora = Label(frame_cima, text='CALCULADORA', width=25, height=1, padx=3, relief=FLAT, anchor='center', font=('Ivy 15 bold'), bg=cor1, fg=cor3)
l_calculadora.place(x=0, y=30)

l_idade = Label(frame_cima, text='DE IDADE', width=11, height=1, padx=3, relief=FLAT, anchor='center', font=('Arial 35 bold'), bg=cor1, fg=cor4)
l_idade.place(x=0, y=60)

# Criando Labels para frame de baixo
l_data_inicial = Label(frame_baixo, text='Data Final', height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('Ivy 11'), bg=cor2, fg=cor3)
l_data_inicial.place(x=30, y=70)

cal_1 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern='mm/dd/y', y=2023)
cal_1.place(x=190, y=70)

l_data_nascimento = Label(frame_baixo, text='Data de Nascimento', height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('Ivy 11'), bg=cor2, fg=cor3)
l_data_nascimento.place(x=30, y=30)

cal_2 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern='mm/dd/y', y=2023)
cal_2.place(x=190, y=30)

l_anos = Label(frame_baixo, text='--', height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 25 bold'), bg=cor2, fg=cor3)
l_anos.place(x=60, y=130)
l_anos_nome = Label(frame_baixo, text='Anos', height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 11 bold'), bg=cor2, fg=cor3)
l_anos_nome.place(x=60, y=175)

l_meses = Label(frame_baixo, text='--', height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 25 bold'), bg=cor2, fg=cor3)
l_meses.place(x=140, y=130)
l_meses_nome = Label(frame_baixo, text='Meses', height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 11 bold'), bg=cor2, fg=cor3)
l_meses_nome.place(x=140, y=175)

l_dias = Label(frame_baixo, text='--', height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 25 bold'), bg=cor2, fg=cor3)
l_dias.place(x=220, y=130)
l_dias_nome = Label(frame_baixo, text='Dias', height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 11 bold'), bg=cor2, fg=cor3)
l_dias_nome.place(x=220, y=175)

# criando button calcular

b_calcular = Button(frame_baixo, command=calcular, text='Calcular', width=20, height=1, relief='raised', overrelief='ridge', font=('Ivy 10 bold'), bg=cor2, fg=cor3)
b_calcular.place(x=75, y=220)

janela.mainloop()
