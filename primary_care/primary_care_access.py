import pandas as pd
import fpsnippets
import matplotlib.pyplot as plot
import graphical_neighborhood

def get_most_providers():
    data = pd.read_csv("data-primary-care-access-facilities.csv")

    neighborhoods = {}

    # For each primary care facility, get the nighberhood. If it is in the dictionary of neighborhoods, add it to the list. If it is not, then create a new key
    # Ignore if it is not in Pittsburgh
    for i in range(len(data)):
        data_point = data.iloc[i]

        neighborhood = fpsnippets.geo_to_neighborhood(data_point['Latitude'], data_point['Longitude'])

        if neighborhood is not None:
            try:
                neighborhoods[neighborhood].append(data_point['GROUP_NAME'])
            except:
                neighborhoods[neighborhood] = [data_point['GROUP_NAME']]

    list_of_neighborhoods = list(neighborhoods.keys())
    list_of_neighborhoods.sort(key=lambda element: len(neighborhoods[element]))
    list_of_neighborhoods.reverse()
    return[
        [hood for hood in list_of_neighborhoods], 
        [len(neighborhoods[hood]) for hood in list_of_neighborhoods]
    ]

providers = get_most_providers()
graphical_neighborhood(providers[0], providers[1])