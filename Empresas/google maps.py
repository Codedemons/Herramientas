import googlemaps

# Inicializar el cliente de Google Maps sin una clave de API
gmaps = googlemaps.Client()

# Obtener la ubicación actual (puedes usar alguna librería para obtener la ubicación actual)
# En este ejemplo, se asume una ubicación específica en latitud y longitud
latitude = 37.774929
longitude = -122.419416

# Realizar la solicitud a la API para buscar negocios cercanos
places_result = gmaps.places_nearby(location=(latitude, longitude), radius=500, type='restaurant')

# Iterar sobre los resultados e imprimir la información de los negocios
for place in places_result['results']:
    print(place['name'], place['vicinity'])
