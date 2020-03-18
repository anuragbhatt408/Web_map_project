import folium 
import pandas

pd = pandas.read_csv("Volcanoes_USA.txt")
lat = list(pd["LAT"])
lon = list(pd["LON"]) 
elev = list(pd["ELEV"])

def color_producer(elevation):
    if elevation <1000:
        return 'green'
    elif 1000<= elevation <3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location = [38,-99],zoom_start = 6)

fgv = folium.FeatureGroup(name = "volcanoes in USA")

for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location =[lt,ln], radius = 7, popup = str(el)+"m",
                        fill_color = color_producer(el),color = 'grey',fill = True,fill_opacity = 0.7))

fgp = folium.FeatureGroup(name = "color")    
fgp.add_child(folium.GeoJson(data = open('world.json','r',encoding = 'utf-8-sig').read(),
                            style_function= lambda x:{'fillColor': 'yellow'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map1.html")
