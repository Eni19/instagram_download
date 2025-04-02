import requests
import os

# Criar a pasta para salvar as imagens, se não existir
folder_name = "imagens_salvas"
os.makedirs(folder_name, exist_ok=True)

# Ler as URLs do arquivo txt
with open("urls.txt", "r") as file:
    urls = file.readlines()

# Baixar cada imagem
for i, url in enumerate(urls):
    url = url.strip()  # Remover espaços e quebras de linha
    if not url:
        continue  # Pular linhas vazias

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Lança um erro se a resposta for ruim (ex: 404)

        # Criar nome do arquivo (ex: imagem_1.jpg, imagem_2.jpg, ...)
        filename = os.path.join(folder_name, f"imagem_{i + 1}.jpg")

        # Salvar a imagem
        with open(filename, "wb") as img_file:
            for chunk in response.iter_content(1024):
                img_file.write(chunk)

        print(f"Imagem {i + 1} baixada com sucesso: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar {url}: {e}")

print("Download concluído!")
