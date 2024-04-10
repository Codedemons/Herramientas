import requests

# Coordenadas geográficas de Ciudad del Carmen, Campeche, México
latitude = 18.6536
longitude = -91.8247

# Definir el radio de búsqueda en metros (ajústalo según sea necesario)
radius = 1000  # Por ejemplo, 1000 metros

# Consulta de Overpass para buscar negocios cercanos en Ciudad del Carmen
overpass_query = f"""
    [out:json];
    node["amenity"="restaurant"](around:{radius},{latitude},{longitude});
    out;
"""

# URL de la API de Overpass
overpass_url = "https://overpass-api.de/api/interpreter"

# Realizar la solicitud POST a la API de Overpass
response = requests.post(overpass_url, data=overpass_query)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta a formato JSON
    data = response.json()
    # Iterar sobre los resultados e imprimir la información de los negocios
    for node in data['elements']:
        name = node.get('tags', {}).get('name', 'Unnamed')
        print(name)
else:
    print("Error al realizar la solicitud:", response.status_code)
