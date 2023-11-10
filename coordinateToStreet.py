from geopy.geocoders import Nominatim

def get_street_name(latitude, longitude):
    geolocator = Nominatim(user_agent="geo_locator")
    location = geolocator.reverse((latitude, longitude), language="en")
    
    # Check if the location was found
    if location:
        return location.address
    else:
        return None

# Example usage
latitude = 48.76385  # Example latitude
longitude = 11.42065  # Example longitude

street_name = get_street_name(latitude, longitude)
print(f"Street Name: {street_name}")