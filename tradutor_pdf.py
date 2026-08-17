"""
Tradutor de Documentos PDF (Inglês -> Português)
Trabalho da faculdade - Ciência da Computação, 3º período

Autor: [coloque seu nome aqui]
Disciplina: [coloque a disciplina aqui]

Descrição:
    Este programa lê um arquivo PDF escrito em inglês, extrai o texto
    página por página, traduz cada página para português usando a
    biblioteca googletrans e gera um novo arquivo de texto contendo
    o texto original e a tradução, para que seja possível comparar os dois.

Bibliotecas usadas:
    - PyPDF2         -> para ler o PDF e extrair o texto
    - deep-translator -> para traduzir o texto (usa o Google Tradutor por baixo)

Como instalar as bibliotecas (rodar no terminal):
    pip install PyPDF2
    pip install deep-translator
"""

import sys
from PyPDF2 import PdfReader
from deep_translator import GoogleTranslator

# Tamanho máximo de caracteres que vamos mandar de uma vez pro tradutor
# (a API do Google tem um limite, então quebramos o texto em pedaços menores)
TAMANHO_MAXIMO_BLOCO = 4500


def ler_pdf(caminho_do_arquivo):
    """
    Recebe o caminho de um PDF e devolve uma lista onde cada posição
    é o texto de uma página do documento.
    """
    print(f"Lendo o arquivo: {caminho_do_arquivo}")

    leitor = PdfReader(caminho_do_arquivo)
    texto_das_paginas = []

    numero_de_paginas = len(leitor.pages)
    print(f"O PDF tem {numero_de_paginas} página(s).")

    for i in range(numero_de_paginas):
        pagina = leitor.pages[i]
        texto = pagina.extract_text()

        # Às vezes o PyPDF2 não consegue extrair texto de uma página
        # (por exemplo, se ela for uma imagem escaneada)
        if texto is None:
            texto = ""

        texto_das_paginas.append(texto)

    return texto_das_paginas


def quebrar_texto_em_blocos(texto, tamanho_maximo):
    """
    Quebra um texto grande em pedaços menores, tentando cortar
    em uma quebra de linha para não cortar frase no meio.
    """
    blocos = []
    inicio = 0

    while inicio < len(texto):
        fim = inicio + tamanho_maximo

        if fim >= len(texto):
            blocos.append(texto[inicio:])
            break

        # tenta achar uma quebra de linha próxima do limite
        posicao_quebra = texto.rfind("\n", inicio, fim)

        if posicao_quebra == -1:
            posicao_quebra = fim

        blocos.append(texto[inicio:posicao_quebra])
        inicio = posicao_quebra

    return blocos


def traduzir_texto(texto, tradutor):
    """
    Traduz um texto (em inglês) para português.
    Quebra em blocos menores se o texto for muito grande.
    """
    if texto.strip() == "":
        return ""

    blocos = quebrar_texto_em_blocos(texto, TAMANHO_MAXIMO_BLOCO)
    texto_traduzido = ""

    for bloco in blocos:
        if bloco.strip() == "":
            continue
        try:
            texto_traduzido += tradutor.translate(bloco)
        except Exception as erro:
            print(f"Ops, deu erro ao traduzir um trecho: {erro}")
            texto_traduzido += "[ERRO AO TRADUZIR ESTE TRECHO]"

    return texto_traduzido


def salvar_resultado(paginas_originais, paginas_traduzidas, caminho_saida):
    """
    Salva um arquivo .txt com o texto original e a tradução de cada página,
    um embaixo do outro, para facilitar a comparação.
    """
    with open(caminho_saida, "w", encoding="utf-8") as arquivo:
        for numero_pagina in range(len(paginas_originais)):
            arquivo.write(f"===== PÁGINA {numero_pagina + 1} =====\n\n")

            arquivo.write("--- TEXTO ORIGINAL (Inglês) ---\n")
            arquivo.write(paginas_originais[numero_pagina])
            arquivo.write("\n\n")

            arquivo.write("--- TRADUÇÃO (Português) ---\n")
            arquivo.write(paginas_traduzidas[numero_pagina])
            arquivo.write("\n\n")

    print(f"Arquivo traduzido salvo em: {caminho_saida}")


def main():
    # Verifica se o usuário passou o nome do arquivo pelo terminal
    if len(sys.argv) < 2:
        print("Como usar: python tradutor_pdf.py nome_do_arquivo.pdf")
        return

    caminho_pdf = sys.argv[1]
    caminho_saida = "documento_traduzido.txt"

    # 1) Lê o PDF e separa o texto por página
    paginas_originais = ler_pdf(caminho_pdf)

    # 2) Traduz cada página
    tradutor = GoogleTranslator(source="en", target="pt")
    paginas_traduzidas = []

    for i, texto_pagina in enumerate(paginas_originais):
        print(f"Traduzindo página {i + 1} de {len(paginas_originais)}...")
        traducao = traduzir_texto(texto_pagina, tradutor)
        paginas_traduzidas.append(traducao)

    # 3) Salva o resultado final (original + tradução) em um .txt
    salvar_resultado(paginas_originais, paginas_traduzidas, caminho_saida)

    print("Tradução concluída!")


if __name__ == "__main__":
    main()
