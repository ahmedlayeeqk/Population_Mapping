import folium

map = folium.Map(location=([-30.0,92]),tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name = "My_Map2")

fg.add_child(folium.Marker(location=((-30.4,91.8)),popup="This is the place",icon=folium.Icon(color = "pink")))

map.add_child(fg)

map.save("Try.html")