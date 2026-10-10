listas = ["oola senhor","salava","dinisouro","dinisouro"]
dici = {
}
for a in listas:
   dici[a] = dici.get(a,0) 
   dici[a] += 1
print(dici)
