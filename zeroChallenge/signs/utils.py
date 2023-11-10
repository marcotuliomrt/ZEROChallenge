from geopy.geocoders import Nominatim
import folium
from folium.vector_layers import Marker
import random

def generate_random_coordinates(num_points):
    file_path = 'signs/random_coordinates_data.txt'
    coordinates = []
    with open(file_path, 'r') as file:
        for line in file:
            coordinates.append(line.strip().split(','))  
    return coordinates

def generate_random_classifications(num_points):
    classifications = []
    for n in range(num_points):
        p = random.choice(['Tree', 'Dirt', 'Sticker'])
        classifications.append(random.choice([p, 'Good']))
    return classifications

def get_address():
    """
    Get the address given the latitude and longitude parameters
    """
    file_path = 'signs/random_adress_data.txt'
    adresses = []
    with open(file_path, 'r') as file:
        for line in file:
            adresses.append(line.strip())  
    return adresses

  
#   geolocator = Nominatim(user_agent="geo_locator")
#   location = geolocator.reverse((latitude, longitude), language="en")

#   if location:
#     address_parts = [
#         location.raw.get('address', {}).get('city'),
#         location.raw.get('address', {}).get('postcode')
#     ]
#     address_filtered = ", ".join(filter(None, address_parts))
#     return address_filtered
#   else:
#     return "Address not found"
    
def create_marker(classification, coordinates, color):
  latitude, longitude = coordinates
  address_filtered = get_address(latitude, longitude)
  popup_text = f"{classification} | {address_filtered}"
  marker = Marker([latitude, longitude], icon=folium.Icon(color=color), popup=folium.Popup(popup_text, parse_html=True))
  return marker