import folium


map = folium.Map(location=[24.249981,89.920029], zoom_start=9)
tooltip = 'Here is My Home!'

folium.Marker(
    location=[24.249981, 89.920029],
    popup='This is my sweet home',
    icon=folium.Icon(icon='cloud')
).add_to(map)

map.save("Map.html")