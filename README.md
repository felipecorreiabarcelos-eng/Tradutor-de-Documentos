# 🌎 Tradutor de Documentos PDF

Sistema simples feito em Python que lê um arquivo PDF em inglês, traduz o conteúdo para português e gera um arquivo de saída com o texto original e a tradução lado a lado.

> Projeto desenvolvido como trabalho da faculdade — Ciência da Computação, 3º período.

## 📌 Funcionalidades

- Lê um PDF inteiro, página por página
- Traduz o texto de inglês para português
- Mantém o texto original junto da tradução no arquivo final
- Gera um arquivo `.txt` com o resultado

## 🛠️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [PyPDF2](https://pypi.org/project/PyPDF2/) — leitura e extração de texto do PDF
- [deep-translator](https://pypi.org/project/deep-translator/) — tradução do texto

## 📂 Estrutura do projeto

```
tradutor-pdf/
├── tradutor_pdf.py      # código principal
├── requirements.txt     # bibliotecas necessárias
├── .gitignore
└── README.md
```

## ▶️ Como usar

1. Clone o repositório:
```bash
git clone https://github.com/SEU-USUARIO/tradutor-pdf.git
cd tradutor-pdf
```

2. (Opcional, mas recomendado) Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute o programa passando o caminho do PDF que deseja traduzir:
```bash
python tradutor_pdf.py caminho/do/arquivo.pdf
```

5. O resultado será salvo automaticamente como `documento_traduzido.txt` na mesma pasta.

## 📖 Exemplo de saída

```
===== PÁGINA 1 =====

--- TEXTO ORIGINAL (Inglês) ---
This is an example text extracted from the PDF...

--- TRADUÇÃO (Português) ---
Este é um texto de exemplo extraído do PDF...
```

## 🐛 Correções recentes (v1.1)

- ✅ Corrigido bug crítico de loop infinito na função `quebrar_texto_em_blocos`
- ✅ Melhorado tratamento de erros e mensagens do usuário
- ✅ Adicionada validação para verificar se o arquivo PDF existe
- ✅ Atualizada documentação para refletir o uso correto de `deep-translator`

## 🚧 Possíveis melhorias futuras

- [ ] Gerar a saída em `.docx` ou `.pdf` em vez de `.txt`
- [ ] Suportar outros idiomas de origem/destino
- [ ] Criar uma interface gráfica simples
- [ ] Tratar PDFs escaneados (usando OCR)
- [ ] Adicionar testes automatizados

## 📄 Licença

Este projeto é livre para fins de estudo.
