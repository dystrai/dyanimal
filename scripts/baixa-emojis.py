import csv
import os

import emoji
import requests

# Caminhos
CSV_PATH = 'docs/_static/animais-emojis.csv'
IMAGES_DIR = 'docs/_static/emoji-images'

# Cria pasta de destino se não existir
os.makedirs(IMAGES_DIR, exist_ok=True)

# Obtém URLs dos emojis via API do GitHub
EMOJI_API_URL = 'https://api.github.com/emojis'
response = requests.get(EMOJI_API_URL)
emoji_map = response.json()

# Função para baixar imagem

def download_emoji_image(emoji_name, dest_path):
    url = emoji_map.get(emoji_name)
    if url:
        r = requests.get(url)
        if r.status_code == 200:
            with open(dest_path, 'wb') as f:
                f.write(r.content)
            print(f'Baixado: {emoji_name}')
        else:
            print(f'Erro ao baixar {emoji_name}: {r.status_code}')
    else:
        print(f'Emoji não encontrado: {emoji_name}')

# Lê o CSV e baixa as imagens
with open(CSV_PATH, encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        emoji_unicode = row['emoji']
        emoji_name = emoji.demojize(emoji_unicode).strip(':')
        dest_file = os.path.join(IMAGES_DIR, f'{emoji_name}.png')
        download_emoji_image(emoji_name, dest_file)
