#Aula 1 - configuração e criação da janela
from tkinter import*

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()  

    def tela(self):
        self.root.title("Cadastro de clientes")
        self.root.configure(background='pink')
        self.root.geometry("900x400")
        self.root.resizable(True,True)
        self.root.maxsize(width=1000, height=500)
        self.root.minsize(width=400, height=400)


Application()
