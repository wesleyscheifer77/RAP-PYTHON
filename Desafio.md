Projeto da Entrevista de Emprego da Empresa Trajetoria
Desafio: 
- Desenvolver um RPA simples para automatizar a coleta de dados de produtos do site da
Amazon (https://www.amazon.com.br/ref=nav_logo). O RPA deve pesquisar por livros sobre
automação de processos e deve coletar informações de pelo menos 8 produtos da lista de
resultados. Após, esses dados devem ser salvos numa planilha de excel ou csv e ordenados
de forma alfabética a partir do título dos livros (A-Z).
Os dados coletados devem ser os seguintes:
1) Nome do livro;
2) Nome(s) do(s) autor(es);
3) Preço de livro físico (capa comum ou dura). Se não houver, utilizar preço da versão para
Kindle;
4) Nota média
5) Número de avaliações
   
- A consulta a ser feita na barra de pesquisa do site deve ser algo do tipo: “livros sobre
automacao”. Após, os dados podem ser retirados na própria página de resultados ou
diretamente na página do produto desejado.

- A planilha precisará conter pelo menos cinco colunas: “Titulo”, “Autor”, “Preço”, “Nota” e
“Avaliações”. Ainda, ela precisará ser ordenada de forma alfabética por título de livro. Se for
preciso adicionar uma coluna para ID (identificador), não há problema.

Ferramentas
- Para o case, pode ser utilizado qualquer tipo de biblioteca, entretanto, a linguagem deve
obrigatoriamente ser python. Como sugestão de stack, colocamos selenium com chromedriver
(para web scraping) e pandas (para armazenamento e tratamento de dados). O ambiente de
execução é de livre escolha (PyCharm, VS Code, Jupyter...).

Para Rodar precisará instalar:
- pip install requests
- pip install beautifulsoup4
- pip install lxml
- pip install pandas
- pip install selenium

Criar um ambiente virutal:
- python -m venv venv

Ativar o ambiente virtual:
- .\venv\Scripts\activate

Depedências do Projeto:
- pip install selenium beautifulsoup4 webdriver-manager pandas
- pip install -r requirements.txt

Obviamente ter o Python instalado!!!
