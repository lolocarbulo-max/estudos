import os
import csv
import json
import PyPDF2#biblioteca com os comandos PyPDF2.PdfReader,.pages e  .extract_text() o primeiro le o e trasforma em paginas o segundo pega as paginas e o terceiro extrai
arquivos_digitados = input("digite um arquivo para sabeer seu conteudo ")
arquivo=  os.path.exists(arquivos_digitados)#checa se na minha maquina se o arquivo existe 
if arquivo == True:
    e =os.path.splitext(arquivos_digitados)[1]# aqui pega separa o endereço em 2 o nome e a extenssão tipo pdf
    if e == ".csv":
       with open(arquivos_digitados,"r",encoding="utf-8") as f:# with e a porta aberta e open o pegador do conteudo ecoding o modo de leiturapara a maquina
          a = f.read() # modo de leitura
          print(a)
    elif e == ".json":
        with open(arquivos_digitados,"r",encoding="utf-8") as c :
             d =json.load(c)#transfora em objeto python
             t = json.dumps(d,indent=3) # faz o inverso transforma em texto e o indent faz o recuo de 3
             print(t)
    elif e == ".txt":
       with open(arquivos_digitados,"r",encoding="utf-8")as x:
           g = x.read() # modo de leitura 
           print(g)
    elif e == ".pdf":
       with open(arquivos_digitados,"rb")as pd:#rb  pois ele tem imagens e posições
            pdy = PyPDF2.PdfReader(pd)#sse é o que vai ler o nosso arquivo pdf e vai transformar em pasta
            pdw = pdy.pages#pega as paginas
            texto =""
            for pdj in pdw:
               pdd = pdj.extract_text()# esse daqui extrai o conteudo
               texto += pdd # resposnsavel pelo exibimento
            print(texto)



else:
    print("não achei")