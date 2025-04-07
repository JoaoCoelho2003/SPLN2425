# TPC6 - Web Scraping e Extração de Conteúdo

Este projeto consiste num script Python que realiza web scraping para extrair e guardar conteúdo de um conjunto de páginas web. O script utiliza as bibliotecas `requests`, `BeautifulSoup` e `shelve` para obter, analisar e armazenar em cache as páginas web.

## Funcionalidades

1. **Cache com `shelve`**:
	- O script utiliza uma base de dados `shelve` (`page_cache.db`) para armazenar em cache o conteúdo das páginas web obtidas, reduzindo pedidos de rede redundantes.

2. **Web Scraping**:
	- Extrai todos os URLs de ficheiros a partir de um URL base (`https://natura.di.uminho.pt/~jj/bs4/folha8-2023/`) ao analisar as tags HTML `<a>`.

3. **Extração de Conteúdo**:
	- Para cada URL extraído, o script obtém o conteúdo da página e extrai:
	  - O título (meta tag `og:title`).
	  - A descrição (meta tag `og:description`).
	  - O conteúdo principal do artigo (se disponível).

4. **Saída para Ficheiros**:
	- Guarda o conteúdo extraído em ficheiros de texto na diretoria `output_files`. Cada ficheiro é nomeado com base no URL, substituindo caracteres especiais para garantir compatibilidade.

## Como Executar

1. **Instalar Dependências**:
	Certifique-se de que tem as bibliotecas Python necessárias instaladas:
	```bash
	pip install requests beautifulsoup4
	```

2. **Executar o Script**:
	Execute o script no terminal:
	```bash
	python script_name.py
	```

3. **Saída**:
	- O script cria a diretoria `output_files` (caso ainda não exista).
	- Cada página web processada gera um ficheiro de texto com o conteúdo extraído.