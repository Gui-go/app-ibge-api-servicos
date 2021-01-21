import requests
import pandas as pd
import json
# import geopandas as gpd
# import folium


def get_malha(cd):
    res = requests.get(f'http://servicodados.ibge.gov.br/api/v3/malhas/municipios/{cd}?formato=application/vnd.geo+json')
    if res.status_code == 200:
        print('Request realizado com sucesso!')
        gj = json.loads(res.content.decode('utf-8'))
    else:
        print('Deu ruim no request  :/')
    
    return gj

# gj2 = get_malha(4205407)

# m = folium.Map([-27, -50], zoom_start=7, tiles='cartodbpositron')
# folium.GeoJson(gj).add_to(m)
# m.save('try.html')