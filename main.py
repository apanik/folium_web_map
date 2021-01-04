import folium

map = folium.Map(location=[23.777176,90.399452], tiles = "Mapbox bright")
map.save("Map.html")