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

    # Sort the neighborhoods based on the length of the list of providers in descending order
    sorted_neighborhoods = sorted(list_of_neighborhoods, key=lambda element: len(neighborhoods[element]), reverse=True)
    
    # Get the top 20 neighborhoods
    top_20_neighborhoods = sorted_neighborhoods[:20]
    
    return [top_20_neighborhoods, [len(neighborhoods[hood]) for hood in top_20_neighborhoods]]

providers = get_most_providers()
