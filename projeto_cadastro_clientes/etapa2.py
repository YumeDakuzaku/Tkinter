#Criação de frames
from tkinter import*

from numpy import place

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        root.mainloop()


    def tela(self):
        self.root.title("Cadastro de clientes")
        self.root.configure(background='gray')
        self.root.geometry("900x400")
        self.root.resizable(True,True)
        self.root.maxsize(width=1000, height=500)
        self.root.minsize(width=400, height=400)
    
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='white', highlightbackground='purple',highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='white', highlightbackground='purple',highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
            


Application()
