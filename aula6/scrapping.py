import requests # Envia requisições
from bs4 import BeautifulSoup # Trata a requisição

url = "https://www.netshoes.com.br/lst/mi-basquete1?mi=hm_sc_cat7_basquete_181023-mas-00&psn=Banner_Categoria_7"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
res = requests.get(url, headers=headers)

if res.status_code == 200:
    print("Requisição feita com sucesso")
    print(res.text)
    
    soup = BeautifulSoup(res.text, "html.parser")
    produtos = soup.find_all("h2", class_="card__description--name")
    print("Produtos de basquete da netshoes")
    for index, produto in enumerate(produtos):
        print(f"{index + 1}. {produto.text.strip()}")

else:
    print(f"Erro na requisição: {res.status_code}")