(myst)=
# Guia rápido de Markdown/MyST

Este arquivo contém a sintaxe para as marcações Markdown e MyST mais comuns.  
Abra-o no seu editor de texto para copiar e colar rapidamente o que precisar.

Veja o [guia de estilo do MyST](https://canonical-documentation-with-sphinx-and-readthedocscom.readthedocs-hosted.com/style-guide-myst/) para informações e convenções detalhadas.

Veja também a [documentação do MyST](https://myst-parser.readthedocs.io/en/latest/index.html) para mais detalhes, e o [Guia de Estilo da Canonical](https://docs.ubuntu.com/styleguide/en) para convenções gerais de estilo.

## Título H2

### Título H3

#### Título H4

##### Título H5

## Formatação inline

- {guilabel}`Elemento da interface`
- `código`
- {command}`comando`
- {kbd}`Tecla`
- *Itálico*
- **Negrito**

## Blocos de código

Inicie um bloco de código:

    code:
      - example: true

````

# Exemplo de bloco de código

code:

* example: true

````

```yaml
# Exemplo de bloco de código
code:
  - example: true
````

(uma_secao_com_alvo)=

## Links

* [Site da Canonical](https://canonical.com/)
* {ref}`uma_secao_com_alvo`
* {ref}`Texto do link <uma_secao_com_alvo>`
* {doc}`index`
* {doc}`Texto do link <index>`

## Navegação

Use a seguinte sintaxe::

````
    ```{toctree}
    :hidden:

    sub-page1
    sub-page2
    ```
````

## Listas

1. Etapa 1
   - Item 1
     - Subitem
   - Item 2
     1. Subetapa 1
     2. Subetapa 2
1. Etapa 2
   1. Subetapa 1
      - Item
   1. Subetapa 2

Termo 1
: Definição

Termo 2
: Definição

## Tabelas

### Tabelas Markdown

| Cabeçalho 1                   | Cabeçalho 2 |
| ----------------------------- | ----------- |
| Célula 1<br>Segundo parágrafo | Célula 2    |
| Célula 3                      | Célula 4    |

Centralizado:

|          Cabeçalho 1          | Cabeçalho 2 |
| :---------------------------: | :---------: |
| Célula 1<br>Segundo parágrafo |   Célula 2  |
|            Célula 3           |   Célula 4  |

### Tabelas com list-table

```{list-table}
   :header-rows: 1

* - Cabeçalho 1
  - Cabeçalho 2
* - Célula 1

    Segundo parágrafo
  - Célula 2
* - Célula 3
  - Célula 4
```

Centralizado:

```{list-table}
   :header-rows: 1
   :align: center

* - Cabeçalho 1
  - Cabeçalho 2
* - Célula 1

    Segundo parágrafo
  - Célula 2
* - Célula 3
  - Célula 4
```

## Notas

```{note}
Uma nota.
```

```{tip}
Uma dica.
```

```{important}
Informação importante.
```

```{caution}
Isso pode danificar seu hardware!
```

## Imagens

![Texto alternativo](https://assets.ubuntu.com/v1/b3b72cb2-canonical-logo-166.png)

```{figure} https://assets.ubuntu.com/v1/b3b72cb2-canonical-logo-166.png
   :width: 100px
   :alt: Texto alternativo

   Legenda da figura
```

## Reutilização

### Chaves

As chaves podem ser definidas no início de um arquivo ou na opção `myst_substitutions` no `conf.py`.

Por exemplo, se você escrever:

- Veremos o emoji do gato `{{gato}}` e do camelo `{{camelo}}`.

Você obterá:

- Veremos o emoji do gato {{gato}} e do camelo {{camelo}}.

### Inclusão de arquivos

```{include} index.md
   :start-after: (amostras)=
   :end-before: referencias.md
```

## Abas

````{tabs}
```{group-tab} Aba 1

Conteúdo da Aba 1
```

```{group-tab} Aba 2
Conteúdo da Aba 2
```
````

## Glossário

```{glossary}

termo  
  Definição do termo de exemplo.
```

{term}`termo`

## Mais marcações úteis

* ```{versionadded} X.Y
  ```
* {abbr}`API (Interface de Programação de Aplicações)`

---

## Extensões personalizadas

Um link para um vídeo do YouTube:

```{youtube} iMLiK1fX4I0
```

```
