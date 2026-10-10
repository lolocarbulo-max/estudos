import tkinter as tk
janela = tk.Tk()
interface = janela.title("ola mundo")
valor_atual = 0
def cliclar():
    global valor_atual
    meu_botao.config(text=f"o valor atula é de {valor_atual}")
    valor_atual += 1
    print(valor_atual)
meu_botao = tk.Button(janela,text="clique em mim ",command=cliclar)

meu_botao.pack()
janela.mainloop()
    
   

         