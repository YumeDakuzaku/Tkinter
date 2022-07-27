#Adicionando função ao botão limpar
from tkinter import*
from tkinter import ttk

from pyparsing import replaceWith

root = Tk()

class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0,END)
        self.nome_entry.delete(0,END)
        self.fone_entry.delete(0,END)
        self.cidade_entry.delete(0,END)

class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()

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
        self.bt_limpar = Button(self.frame_1, text="Limpar", bd=4, bg="lightgreen", fg="purple", font=('verdana',8,'bold'),command=self.limpa_tela)
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

        self.lb_fone = Label(self.frame_1, text="Telefone", bg="gray", fg="purple")
        self.lb_fone.place(relx=0.05, rely=0.6)

        self.fone_entry = Entry(self.frame_1)
        self.fone_entry.place(relx=0.05, rely=0.7, relwidth=0.3)
        
        #Criação da Label e entrada da cidade

        self.lb_cidade = Label(self.frame_1, text="Cidade", bg="gray", fg="purple")
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.3)


    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, column=("col1","col2","col3","col4"))
        self.listaCli.heading("#0", text ="")
        self.listaCli.heading("#1", text ="Código")
        self.listaCli.heading("#2", text ="Nome")
        self.listaCli.heading("#3", text ="Telefone")
        self.listaCli.heading("#4", text ="Cidade")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)





Application()
