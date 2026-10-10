import requests # ensina sobre os modulos e vlivliotecas do python 
from bs4 import BeautifulSoup

url =  "https://ge.globo.com/futebol/brasileirao-serie-a/"
headers = {"User-Agent": "Mozilla/5.0"}
resposta = requests.get(url, headers=headers)
# LINHAS DE TESTE:
print("--- TESTE DE ENDEREÇO ---")
print(f"O Python está acessando: {resposta.url}")
print("-------------------------")
tradutor = BeautifulSoup(resposta.text, 'html.parser')
tags_times = tradutor.find_all("div", class_="menu-item-equipe")
if not tags_times:
    tags_times = tradutor.find_all("a", class_="menu-item-link")

times_lista = [
    "Athletico-PR",
    "Atlético-MG",
    "Bahia",
    "Botafogo",
    "Bragantino",
    "Chapecoense",
    "Corinthians",
    "Coritiba",
    "Cruzeiro",
    "Flamengo",
    "Fluminense",
    "Grêmio",
    "Internacional",
    "Mirassol",
    "Palmeiras",
    "Remo",
    "Santos",
    "São Paulo",
    "Vasco",
    "Vitória",
]
tupla_times = tuple(times_lista)
print("--- TUPLA COMPLETA DO BRASILEIRÃO ---")
print(tupla_times)
print("-" * 37)
print(tupla_times[:5]) 
print(tupla_times[-4:])
print(sorted(tupla_times))
print(tupla_times.index("São Paulo") + 1)