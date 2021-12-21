from tkinter import *
#Tela do programa
app = Tk()
app.title('Login de acesso')
app.geometry('500x300')
app.configure(background='#008')

#Exibição dos alunos presentes na tela
txt1 = Label(app, text='Bem Vindo ao Grau Técnico', background='#008', foreground='#fff')
txt1.place(x=160, y=10, width=150, height=30)

txt2=Label(app,text='Usuário',bg='#008',fg='#fff')
txt2.pack(ipadx=20, ipady=20, padx=5, pady=5, side='top', fill= X, expand=True)


app.mainloop() # executa o programa
