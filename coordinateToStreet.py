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
    return(url)

latitude = 48.76385  # Example latitude
longitude = 11.42065  # Example longitude

# Example usage - print street name
street_name = get_street_name(latitude, longitude)
print(f"Street Name: {street_name}")

# Example usage - open google maps
coordinates = (latitude, longitude)


# Example usage - get the link
google_maps_link = open_google_maps(coordinates)
print(google_maps_link)