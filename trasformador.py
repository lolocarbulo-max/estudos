import tkinter as tk
janela = tk.Tk()
interface = janela.title("ola mundo")
meu_abel = tk.Label(janela,text="digite um valor")
meu_abel.pack()
valor_a_ser_trasformado = tk.Entry(janela)
valor_a_ser_trasformado.pack()
def trasformar():
    try:
        a = float(valor_a_ser_trasformado.get())
        f = (a * 9/5)  + 32
        meu_b.config(text=f"a gora o valor é de {f}")
        print(f)
    except ValueError:
        print("não dá para dividir por zero")
meu_b = tk.Button(janela,text="o valor é de e agora é de",command=trasformar) 
meu_b.pack()
janela.mainloop()
