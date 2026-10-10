import tkinter as tk
janela = tk.Tk()
janela.geometry("300x200")
listas = tk.Listbox(janela)
listas.pack()
entrada = tk.Entry(janela)
entrada.pack()
def colocar():
    entrada2 = entrada.get()
    listas.insert(tk.END,entrada2)
    entrada.delete(0,tk.END)
meu_botao = tk.Button(janela,text="aperte em mim",command=colocar)
meu_botao.pack()
janela.mainloop()
