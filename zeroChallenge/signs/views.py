from django.shortcuts import render, redirect
from .models import Sign
from django.views.decorators.csrf import csrf_exempt
import folium
from .utils import \
    generate_random_coordinates, \
    generate_random_classifications, create_marker, get_address



@csrf_exempt
def index(request):
    all_signs = Sign.objects.all()

    initial_latitude, initial_longitude = 48.765633, 11.423611 # Center of ingolstadt

    my_map = folium.Map(location=[initial_latitude, initial_longitude], zoom_start=15, width='800px', height='800px')

    # Add a marker to the map
    for sign in all_signs:
        classification = sign.classification
        adress = sign.adress
        latitude = float(sign.latitude)
        longitude = float(sign.longitude)
        color = 'green' if classification == 'Good' else 'red'
        
        popup_text = f"{classification} | {adress}"
        folium.Marker(location=[latitude, longitude], icon=folium.Icon(color=color), popup=folium.Popup(popup_text, parse_html=True)).add_to(my_map)

    # Convert the Folium map to HTML
    map_html = my_map._repr_html_()

    return render(request, 'signs/index.html', {'signs': all_signs, 'map_html': map_html})
        
def solved(request):

    signs = Sign.objects.filter(solved=True)

    initial_latitude, initial_longitude = 48.765633, 11.423611 # Center of ingolstadt

    my_map = folium.Map(location=[initial_latitude, initial_longitude], zoom_start=15, width='800px', height='800px')

    # Add a marker to the map
    for sign in signs:
        classification = sign.classification
        adress = sign.adress
        latitude = float(sign.latitude)
        longitude = float(sign.longitude)
        color = 'green' if classification == 'Good' else 'red'
        
        popup_text = f"{classification} | {adress}"
        folium.Marker(location=[latitude, longitude], icon=folium.Icon(color=color), popup=folium.Popup(popup_text, parse_html=True)).add_to(my_map)

    # Convert the Folium map to HTML
    map_html = my_map._repr_html_()

    return render(request, f'signs/solved.html', {'signs': signs, 'map_html': map_html})

def unsolved(request):

    signs = Sign.objects.filter(solved=False)

    initial_latitude, initial_longitude = 48.765633, 11.423611 # Center of ingolstadt

    my_map = folium.Map(location=[initial_latitude, initial_longitude], zoom_start=15, width='800px', height='800px')

    # Add a marker to the map
    for sign in signs:
        classification = sign.classification
        adress = sign.adress
        latitude = float(sign.latitude)
        longitude = float(sign.longitude)
        color = 'green' if classification == 'Good' else 'red'
        
        popup_text = f"{classification} | {adress}"
        folium.Marker(location=[latitude, longitude], icon=folium.Icon(color=color), popup=folium.Popup(popup_text, parse_html=True)).add_to(my_map)

    # Convert the Folium map to HTML
    map_html = my_map._repr_html_()

    return render(request, f'signs/unsolved.html', {'signs': signs, 'map_html': map_html})


def all(request):
    return redirect('index')
        
    