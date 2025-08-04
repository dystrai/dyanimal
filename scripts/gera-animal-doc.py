#!/usr/bin/env python3

from csv import DictReader
from dataclasses import dataclass
import logging
from pathlib import Path

import emoji

@dataclass
class Animal:
    emoji: str
    name: str
    nome: str

def texto_sobre_animal(animal: Animal) -> str: 
    return f'''\
---
title: {animal.nome.title()}
---

({animal.nome})=

# {animal.nome.title()}

Você está lendo o artigo sobre {animal.nome}, que em inglês se escreve 
`{animal.name}`, e cujo emoji é {animal.emoji}.

A vantagem de saber o nome de seu animal em ingês é que você poderá obter maiores informações sobre ele no [verbete em inglês](wikien:{animal.name}). 
Você também poderá ler o [verbete do animal em português](wikipt:{animal.nome}).

Na sua documentação, usando a plataforma [MkDocs](https://www.mkdocs.org/) com o tema [MkDocs Material](https://squidfunk.github.io/mkdocs-material/),
você deverá inserir o código curto[^1] `{emoji.demojize(animal.emoji)}`.

[^1]: Código curto, em inglês, é *short code*.
'''

logging.basicConfig(level=logging.INFO)

cam_script = Path(__file__).parent
cam_csv_animais = cam_script.parent /"docs"/"_static"/"animais-emojis.csv"
if cam_csv_animais.exists():
    try:
        leitor = DictReader(cam_csv_animais.open(encoding='utf-8'))
        dados_animal = {}
        for dados in leitor:
            dados_animal[dados["nome"]] = Animal(**dados)
    except Exception as e:
        print(e)

cam_animais = cam_script.parent / "docs" / "animais"
cam_animais.mkdir(parents=True, exist_ok=True)
cam_idx_animais = cam_animais / "index.md"

with cam_idx_animais.open(mode='w', encoding='utf-8') as idx_animais:
    idx_animais.write('# Animais\n\n')
    for nome,animal in dados_animal.items():
        idx_animais.write(f"{{doc}}`{animal.emoji} <{nome}>`\n")

    idx_animais.write('''\

```{toctree}
---
maxdepth: 1
caption: Sumário
glob: true
---

*
```
''')

for nome,animal in dados_animal.items():
    cam_arq_animal = cam_animais / f"{nome}.md"
    with cam_arq_animal.open(mode="w", encoding="utf-8") as arq_animal:
        texto: str = texto_sobre_animal(animal)
        arq_animal.write(texto)
    logging.info(f"Gerada documentação para {animal.nome}")



