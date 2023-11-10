from geopy.geocoders import Nominatim
import webbrowser

def get_street_name(latitude, longitude):
    geolocator = Nominatim(user_agent="geo_locator")
    location = geolocator.reverse((latitude, longitude), language="en")
    
    # Check if the location was found
    if location:
        return location.address
    else:
        return None

def open_google_maps(coordinates):
    """
    Opens a Google Maps link with the specified coordinates.

    Parameters:
    - coordinates (tuple): A tuple containing latitude and longitude.
    """
    if len(coordinates) != 2:
        raise ValueError("Coordinates should be a tuple containing latitude and longitude.")

    latitude, longitude = coordinates
    url = f"https://www.google.com/maps/place/{latitude},{longitude}"
    
    webbrowser.open(url)

def get_google_maps_link(coordinates):
    """
    Generates a Google Maps link with the specified coordinates.

    Parameters:
    - coordinates (tuple): A tuple containing latitude and longitude.

    Returns:
    - str: Google Maps link for the specified coordinates.
    """
    if len(coordinates) != 2:
        raise ValueError("Coordinates should be a tuple containing latitude and longitude.")

    latitude, longitude = coordinates
    url = f"https://www.google.com/maps/place/{latitude},{longitude}"

    return url

latitude = 48.76385  # Example latitude
longitude = 11.42065  # Example longitude

# Example usage - print street name
street_name = get_street_name(latitude, longitude)
print(f"Street Name: {street_name}")

# Example usage - open google maps
coordinates = (latitude, longitude)
open_google_maps(coordinates)

google_maps_link = get_google_maps_link(coordinates)
print(google_maps_link)