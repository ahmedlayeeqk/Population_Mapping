from turtle import fillcolor
import folium
import pandas as pd

df = pd.read_csv("Volcanoes.txt")
lat = list(df["LAT"])
lon = list(df["LON"])
elev = list(df["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 < elevation < 2000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[38.5,-98],zoom_start=6,tiles = "Stamen Terrain");

fgv = folium.FeatureGroup(name = "Volcanoes")

for lt,lo,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,lo], popup="Elevation:{}".format(el)+"m",fill = True,color ="grey", 
    fill_color = color_producer(el),opacity = 0.0))

fgp = folium.FeatureGroup(name = "Population")
fgp.add_child(folium.GeoJson(data = open("world.json","r",encoding='utf-8-sig').read(),style_function= lambda x:{'fillColor':"orange" if x['properties']['POP2005'] < 10000000 else "green" if 10000000 <=x['properties']['POP2005'] <20000000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Volc.html")