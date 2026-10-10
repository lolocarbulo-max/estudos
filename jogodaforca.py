import tkinter as tk
palavra = "python"
janela = tk.Tk()
janela.title("jogo da  forca ")
meu_labe = tk.Label(text="digite s para sair  p para progreso " )
meu_label2 = tk.Label(text="progresso")
meu_labe.pack()
meu_entrada = tk.Entry()
meu_entrada.pack()
letras_descobertas = ["_"] * len(palavra)
label3 = tk.Label(text="palavras tentadas")
label3.pack()
letras_tentadas = set()
letras_tentadas_labe = tk.Label(text="")
letras_tentadas_labe.pack()
tetaivas = tk.Label(text="0")
tetaivas.pack()
tentativas =  0
def sair():
    janela.destroy()
def progreso():
     meu_labe.config(text="".join(letras_descobertas))
     label3.config(text=str(letras_tentadas))
def jogo():
     global tentativas
     a = meu_entrada.get()
     if a not in palavra:
          letras_tentadas.add(a)
          tentativas+= 1
          tetaivas.config(text=str(tentativas))
          if tentativas >= len(palavra):
               janela.destroy()
     elif a in palavra:
         letras_tentadas.add(a)
         for posicao in range(len(palavra)):
             if palavra[posicao] ==a:
                  letras_descobertas[posicao] = a
     # DEPOIS vem o resto
     meu_entrada.delete(0,tk.END)
     letras_tentadas_labe.config(text=str(letras_tentadas))
     meu_labe.config(text="".join(letras_descobertas))
     label3.config(text=str(letras_tentadas))
     
         


meu_botoa = tk.Button(janela,text="sair",command=sair)
meu_botoa.pack()
botao_p = tk.Button(janela,text="aperte em mim para ver o progreso",command=progreso)
botao_p.pack()
meu_botoa2 = tk.Button(janela,text="aperte em mim para jogar",command=jogo)
meu_botoa2.pack()
janela.mainloop()