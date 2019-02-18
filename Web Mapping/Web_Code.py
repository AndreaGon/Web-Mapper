import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")

def popupcolor(elevation):
    if elevation <= 1000:
        return "green"
    elif elevation > 1000 and elevation <= 3000:
        return "orange"
    else:
        return "red"

lat = data["LAT"]
lon = data["LON"]
elev = data["ELEV"]

map = folium.Map(location = [48,-121], zoom_start = 5)

fgv=folium.FeatureGroup(name="Volcanoes")

for l,t,el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[l, t], popup=str(el), color= "grey", fill= True, fill_opacity= 0.8, fill_color=  popupcolor(el)))

fgp=folium.FeatureGroup(name="Population")


fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding ="utf-8-sig").read(),
style_function = lambda x : {"fillColor" : "green" if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
