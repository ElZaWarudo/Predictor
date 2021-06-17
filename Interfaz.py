
from tkinter import ttk
import tkinter as tk
from TermPredictor import TermPredictor as TP

class Interfaz():
    def __init__(self):
        
        #Ventana
        ventana= tk.Tk()
        ventana.geometry("200x140")
        ventana.title("Grafica") 
        ventana.resizable(False, False)
        
        #Etiquetas
        opeL=ttk.Label(text="Operación:")
        opeL.place(x=30, y=20)
        
        
        #Combobox
        #Operacion
        self.opeC=ttk.Combobox(state="readonly")
        self.opeC.place(x=30, y=50)
        self.opeC["values"]= ["ETH-USD", "BTC-USD", "BCH-USD","LTC-USD"]
        self.opeC.current(0)
        
        #Botones
        nextB=tk.Button(text="Adelante", height = 1, width = 16, command=self.adelante)
        nextB.place(x=40, y=90)
        
        
        ventana.mainloop()

    def adelante(self):
        tp = TP(self.opeC.get())
   
def main():
        app = Interfaz()
        return 0

if __name__ == '__main__':
    main()