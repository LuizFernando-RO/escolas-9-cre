# -*- coding: utf-8 -*-
import folium
import requests
import pickle

markers = []
errors = []
with open('escolas.txt') as f:
  escolas = f.readlines()
  for escola in escolas:
    spl = escola.strip().split(';')
    tipo = spl[0]
    nome = spl[1]
    logr = spl[2]
    cep = spl[3]
    query = f'{tipo} {nome} {logr} Campo Grande RJ {cep}'
    print(query)
    baseurl='http://dev.virtualearth.net/REST/v1/Locations/'
    key='ADD_YOUR_BING_API_KEY'
    try:
      # print(f"{baseurl}{query}?o=json&key={key}")
      response = requests.get(f"{baseurl}{query}?o=json&key={key}")
      data = response.json()['resourceSets'][0]['resources'][0]['geocodePoints'][0]['coordinates']
      markers.append(data + [tipo, nome])
    except:
      print(f'erro em {cep}')
      errors.append(cep)

with open('marcadores', 'wb') as f:
  pickle.dump(markers,f)

dic = {'EM':'red','EDI':'blue','CP':'gray','EEM':'green','CM':'black'}
m = folium.Map(location=[-22.931764890730523, -43.553580856368654], tiles="OpenStreetMap", zoom_start=14)
for marker in markers:
  folium.Marker(
      location=[marker[0], marker[1]],
      popup=f'{marker[2]} {marker[3]}',
      icon=folium.Icon(color=dic[marker[2]])
   ).add_to(m)
folium.Marker(location=[-22.882047368658117, -43.61259482736827], popup='EDI Pintando o Sete', icon=folium.Icon(color='blue')).add_to(m)
# folium.Marker(location=['HOME_LAT', 'HOME_LONG'], popup='Casa',icon=folium.Icon(color='orange')).add_to(m)
m.save('escolas.html')