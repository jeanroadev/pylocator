import requests
import webbrowser

def get_geolocation(ip_address):
    access_key = 'API KEY'
    url = f"http://api.ipstack.com/{ip_address}?access_key={access_key}"
    response = requests.get(url)
    data = response.json()
    
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    
    return {
        "ip": ip_address,
        "latitude": latitude,
        "longitude": longitude,
        "city": data.get("city"),
        "region": data.get("region_name"),
        "country": data.get("country_name"),
        "provider": data.get("connection", {}).get("isp")
    }

ip_address = input("Por favor, ingresa la dirección IP: ")

geolocation_data = get_geolocation(ip_address)
print(geolocation_data)


if geolocation_data["latitude"] and geolocation_data["longitude"]:
    latitude = geolocation_data["latitude"]
    longitude = geolocation_data["longitude"]
    google_maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"
    webbrowser.open(google_maps_url)
else:
    print("No se pudo obtener la ubicación.")
