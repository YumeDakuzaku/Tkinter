#Criação da estilização dos widgets
from tkinter import*
from matplotlib.pyplot import gray

from numpy import place

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        root.mainloop()


    def tela(self):
        self.root.title("Cadastro de clientes")
        self.root.configure(background='gray')
        self.root.geometry("900x400")
        self.root.resizable(True,True)
        self.root.maxsize(width=1000, height=500)
        self.root.minsize(width=600, height=400)
    
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='gray', highlightbackground='purple',highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='white', highlightbackground='purple',highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    
    def widgets_frame1(self):
        self.bt_limpar = Button(self.frame_1, text="Limpar", bd=4, bg="lightgreen", fg="purple", font=('verdana',8,'bold'))
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)   

        self.bt_buscar = Button(self.frame_1, text="Buscar", bd=4, bg="lightgreen", fg="purple", font=('verdana',8,'bold'))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)       

        self.bt_novo = Button(self.frame_1, text="Novo",bd=4, bg="lightgreen", fg="purple", font=('verdana',8,'bold'))
        self.bt_novo.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)   

        self.bt_alterar = Button(self.frame_1, text="Alterar", bd=4, bg="lightgreen", fg="purple", font=('verdana',8,'bold'))
        self.bt_alterar.place(relx=0.4, rely=0.1, relwidth=0.1, relheight=0.15)   

        self.bt_apagar = Button(self.frame_1, text="Apagar", bd=4, bg="lightgreen", fg="purple", font=('verdana',8,'bold'))
        self.bt_apagar.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.15)    

        #Criação da Label e entrada do código

        self.lb_codigo = Label(self.frame_1, text="Código", bg="gray", fg="purple")
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)
        
        #Criação da Label e entrada do nome

        self.lb_nome = Label(self.frame_1, text="Nome", bg="gray", fg="purple")
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

        #Criação da Label e entrada do telefone

        self.lb_nome = Label(self.frame_1, text="Telefone", bg="gray", fg="purple")
        self.lb_nome.place(relx=0.05, rely=0.6)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.7, relwidth=0.3)
        
        #Criação da Label e entrada da cidade

        self.lb_nome = Label(self.frame_1, text="Cidade", bg="gray", fg="purple")
        self.lb_nome.place(relx=0.5, rely=0.6)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.5, rely=0.7, relwidth=0.3)

Application()
