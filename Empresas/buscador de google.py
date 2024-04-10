import requests
from bs4 import BeautifulSoup

def buscar_empresas(query):
    url = f"https://www.google.com/search?q={query}&num=20"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        resultados = soup.find_all('h3')
        for resultado in resultados:
            print(resultado.text)
    else:
        print("Error al realizar la solicitud")

buscar_empresas("Negocios en Isla aguada")
