import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


# Função para buscar os produtos relacionados à automação na Amazon com Selenium
def buscar_livros(query):
    # URL da Amazon para busca
    url_base = "https://www.amazon.com.br/s?k={}&ref=nav_logo"
    url = url_base.format(query)

    # Configurar o Selenium WebDriver (usando o ChromeDriver com WebDriverManager)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Modo sem interface gráfica (opcional)

    # Usando o WebDriverManager para obter o ChromeDriver automaticamente
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Acessar a URL
    driver.get(url)

    # Esperar até que os resultados estejam carregados
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.s-main-slot'))  # Espera até a área de resultados ser carregada
        )
    except Exception as e:
        print(f"Erro ao carregar a página: {e}")
        driver.quit()
        return None

    # Capturar o HTML da página após o carregamento
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Fechar o navegador
    driver.quit()

    return soup


# Função para extrair dados dos livros da página de resultados
def extrair_dados_livros(soup):
    livros = []
    resultados = soup.find_all('div', {'data-asin': True})

    # Garantir que há resultados para processar
    if not resultados:
        print("Nenhum produto encontrado. Verifique a consulta ou a estrutura da página.")
        return []

    for resultado in resultados[:10]:  # Limitando a 10 produtos
        # Título
        titulo = resultado.find('span', {'class': 'a-text-normal'})  # Verifique se essa classe ainda existe
        if not titulo:
            # Verificar se o <h2> existe e tentar obter o título de dentro do <span>
            h2 = resultado.find('h2')
            if h2:
                titulo = h2.find('span')  # Se o <h2> foi encontrado, tenta encontrar o <span> dentro dele
        if titulo:
            titulo = titulo.text.strip()
        else:
            titulo = "Título não disponível"

        # Autor
        autor = resultado.find('div', {'class': 'a-row a-size-base a-color-secondary'})
        if autor:
            autor = autor.text.strip()
        else:
            autor = 'Autor não disponível'

        # Preço
        preco = resultado.find('span', {'class': 'a-price-whole'})
        if preco:
            preco = preco.text.strip()
            preco = f"R$ {preco}"  # Adicionando o símbolo "R$" ao preço
        else:
            # Tentando pegar o preço para Kindle, caso não exista preço físico
            preco_kin = resultado.find('span', {'class': 'a-price-symbol'})
            if preco_kin:
                preco = preco_kin.text.strip()
                preco = f"R$ {preco}"  # Adicionando o símbolo "R$" ao preço
            else:
                preco = 'Preço não disponível'

        # Nota
        nota = resultado.find('span', {'class': 'a-icon-alt'})
        if nota:
            nota = nota.text.strip()
        else:
            nota = 'Nota não disponível'

        # Número de Avaliações (corrigido)
        num_avaliacoes = resultado.find('span', {'class': 'a-size-base s-underline-text'})
        if num_avaliacoes:
            num_avaliacoes = num_avaliacoes.text.strip()
        else:
            num_avaliacoes = 'Número de avaliações não disponível'

        livro = {
            'Título': titulo,
            'Autor(es)': autor,
            'Preço': preco,
            'Nota': nota,
            'Número de Avaliações': num_avaliacoes
        }

        livros.append(livro)

    return livros


# Função principal para rodar o processo
def main():
    query = 'livros sobre automacao'
    soup = buscar_livros(query)

    if not soup:
        print("Nenhum livro encontrado. Verifique a consulta ou a estrutura da página.")
        return

    livros = extrair_dados_livros(soup)

    # Verificando se a lista de livros não está vazia
    if not livros:
        print("Nenhum livro encontrado. Verifique a consulta ou a estrutura da página.")
        return  # Finaliza a execução caso nenhum livro seja encontrado

    # Convertendo para DataFrame para facilitar a manipulação
    df = pd.DataFrame(livros)

    # Ordenando por título (A-Z)
    df = df.sort_values(by='Título', ascending=True)

    # Salvando os dados em um arquivo CSV
    df.to_csv('livros_automacao.csv', index=False)
    print("Dados salvos em 'livros_automacao.csv'.")


# Executando o script
if __name__ == "__main__":
    main()
