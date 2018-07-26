import folium
import pandas
data=pandas.read_csv("Volcanoes_USA.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
name=list(data['NAME'])
#print(name)
map = folium.Map(location=[32.52,13.11],zoom_start=3,tiles="Mapbox Bright")

fgv=folium.FeatureGroup(name="Volacanoes")
fgp=folium.FeatureGroup(name="Population")

def colors(el):
    if el<=1500:
        return 'green'
    elif el<=3000:
        return 'blue'
    else:
        return 'red'
#list=[[25.56,91.91],[25.57,91.89],[25.58,91.89]]
#for coordi in list:
for lt,ln,el,nm in zip(lat,lon,elev,name):
    #fg.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup= str(el)+str(nm)+" m",fill_color=colors(el),color='grey',fill_opacity=0.7))
    fgv.add_child(folium.Marker(location=[lt,ln],popup=str(el)+"m",icon=folium.Icon(color=colors(el))))

fgp.add_child(folium.GeoJson(data=open("world.json",'r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'yellow'} if x['properties']['POP2005'] < 15000000
else {'fillColor':'red'} if 15000000 <= x['properties']['POP2005'] < 70000000 else {'fillColor':'purple'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())



map.save("Map1.html")
