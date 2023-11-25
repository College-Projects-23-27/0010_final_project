import pandas as pd
import matplotlib.pyplot as plot

# Absolute import from the parent package
from util import fpsnippets

def get_most_providers():
    data = pd.read_csv("datasets/data-primary-care-access-facilities.csv")
    neighborhoods = {}

    for i in range(len(data)):
        data_point = data.iloc[i]
        neighborhood = fpsnippets.geo_to_neighborhood(data_point['Latitude'], data_point['Longitude'])

        if neighborhood is not None:
            neighborhoods.setdefault(neighborhood, []).append(data_point['GROUP_NAME'])

    list_of_neighborhoods = list(neighborhoods.keys())
    list_of_neighborhoods.sort(key=lambda element: len(neighborhoods[element]), reverse=False)
    
    return [list_of_neighborhoods, [len(neighborhoods[hood]) for hood in list_of_neighborhoods]]

providers = get_most_providers()
