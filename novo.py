from PIL import Image
try:
    with open(r"C:\Users\loloc\OneDrive\Área de Trabalho\wa-sstoast-toggle-rebranding-step2.png", "rb") as f:
        img = Image.open(f)
        img.save(r"C:\Users\loloc\OneDrive\Área de Trabalho\novo_arquivo.png")
        img.show()
except  FileNotFoundError as e:
    print(f"Ocorreu um erro: {e}")
