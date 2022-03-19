import folium

dic = {'EM':'red','EDI':'blue','CP':'gray','EEM':'green','CM':'black'}
m = folium.Map(location=[-22.931764890730523, -43.553580856368654], tiles="OpenStreetMap", zoom_start=14)

with open('coordenadas.txt') as f:
    markers = f.readlines()
    for marker in markers:
        print(marker)
        spl = marker.strip().split(';')
        print(spl)
        lat = spl[0]
        long = spl[1]
        tipo = spl[2]
        nome = spl[3]
        folium.Marker(
            location=[float(lat), float(long)],
            popup=f'{tipo} {nome}',
            icon=folium.Icon(color=dic[tipo])
        ).add_to(m)
folium.Marker(location=[-22.931764890730523, -43.553580856368654], popup='Casa',icon=folium.Icon(color='orange')).add_to(m)
m.save('escolas.html')