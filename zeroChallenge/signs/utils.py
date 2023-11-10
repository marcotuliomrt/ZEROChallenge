from geopy.geocoders import Nominatim
from folium.vector_layers import Marker
import random

def generate_random_data(num_points):
    coordinates = []
    for n in range(num_points):
        latitude = random.uniform(48.7, 48.8)  # Adjust latitude range as needed
        longitude = random.uniform(11.3, 11.5)  # Adjust longitude range as needed
        coordinates.append((latitude, longitude))
    return coordinates

def get_address(coordinates):
  """
  Get the address given the latitude and longitude parameters
  """
  latitude, longitude = coordinates
  geolocator = Nominatim(user_agent="geo_locator")
  location = geolocator.reverse((latitude, longitude), language="en")

  if location:
    address_parts = [
        location.raw.get('address', {}).get('city'),
        location.raw.get('address', {}).get('postcode'),
        location.raw.get('address', {}).get('country')
    ]
    address_filtered = ", ".join(filter(None, address_parts))
    return address_filtered
  else:
    return "Address not found"
    
def create_colored_marker(classification, coordinates, color):
  latitude, longitude = coordinates
  address_filtered = get_address(latitude, longitude)
  popup_text = f"{classification} | {address_filtered}"
  marker = Marker([latitude, longitude], icon=folium.Icon(color=color), popup=folium.Popup(popup_text, parse_html=True))
  return marker