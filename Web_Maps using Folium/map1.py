import folium
map = folium.Map(location=[25.56,91.91],zoom_start=13,tiles="Mapbox Bright")

fg=folium.FeatureGroup(name="My map")
list=[[25.56,91.91],[25.57,91.89],[25.58,91.89]]
for coordi in list:
    fg.add_child(folium.Marker(location=coordi,icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")
