from django.shortcuts import render, redirect
from .models import Sign
from django.views.decorators.csrf import csrf_exempt
import folium
from .utils import generate_random_data, get_address, create_colored_marker



@csrf_exempt
def index(request):
    num_points = 20
    coordinates = generate_random_data(num_points)

    latitude, longitude = 48.76385, 11.42065

    marker_latitude, marker_longitude = latitude, longitude

    my_map = folium.Map(location=[latitude, longitude], zoom_start=12, width='800px', height='800px')

    # Add a marker to the map
    folium.Marker(location=[marker_latitude, marker_longitude], popup='Marker').add_to(my_map)

    # Convert the Folium map to HTML
    map_html = my_map._repr_html_()


    all_signs = Sign.objects.all()

    return render(request, 'signs/index.html', {'signs': all_signs, 'map_html': map_html})
        
def solved(request):

    latitude, longitude = 48.76385, 11.42065

    marker_latitude, marker_longitude = latitude, longitude

    my_map = folium.Map(location=[latitude, longitude], zoom_start=12, width='800px', height='800px')

    # Add a marker to the map
    folium.Marker(location=[marker_latitude, marker_longitude], popup='Marker').add_to(my_map)

    # Convert the Folium map to HTML
    map_html = my_map._repr_html_()

    signs = Sign.objects.filter(solved = 'True')

    return render(request, f'signs/solved.html', {'signs': signs, 'map_html': map_html})

def unsolved(request):

    latitude, longitude = 48.76385, 11.42065

    marker_latitude, marker_longitude = latitude, longitude

    my_map = folium.Map(location=[latitude, longitude], zoom_start=12, width='800px', height='800px')

    # Add a marker to the map
    folium.Marker(location=[marker_latitude, marker_longitude], popup='Marker').add_to(my_map)

    # Convert the Folium map to HTML
    map_html = my_map._repr_html_()

    signs = Sign.objects.filter(solved = 'False')

    return render(request, f'signs/unsolved.html', {'signs': signs, 'map_html': map_html})


def all(request):
    return redirect('index')
        
    