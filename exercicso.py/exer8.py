clientes = [["Ana", 3], ["Bruno", 5], ["Carla", 4], ["Diego", 2]]
n_caixas = 2
tempo = [0,0] 
for elementos in clientes:
        menor = min(tempo)# verifica o menor valor em tempo que é zero
        posiçao = tempo.index(menor) #pega o index de menor e dacerto pois é zero 
        tempo[posiçao] += elementos[1] # tempo posição da certo pois poisiçaõ é zero ou seja um numero 
print(max(tempo))# aqui exibe o maior valor