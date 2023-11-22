import pandas as pd
from util import fpsnippets

def get_blood_lead_levels():
    neighborhoods = {}
    data = pd.read_csv("./datasets/wprdc_censustracts.csv")

    for i in range(len(data)):
        person = data.iloc[i]

        # chose only the 2020 rates, because of issues pointed out from the data guide. Also if the note has "unstable", it means that
        # not a sufficient amount of children were found with elevated levels to establish an issue with the region
        # Likewise, a None object is useless here. If a child does not have elevated levels, they do not add to the possible issues
        if person['percentEBLL2020'] is not None:
            if str(person['note2020']).count("unstable") == 0:
                # if the levels are not 0 and not unstable, add the data
                if fpsnippets.census_to_neighborhoods(person['CensusTract']) is not None and len(fpsnippets.census_to_neighborhoods(person['CensusTract'])) != 0:
                    try:
                        neighborhoods[fpsnippets.census_to_neighborhoods(person['CensusTract'])[0]] += 1
                    except:
                        neighborhoods[fpsnippets.census_to_neighborhoods(person['CensusTract'])[0]] = 1
        
    list_of_neighborhoods = list(neighborhoods.keys())
    list_of_neighborhoods.sort(key=lambda element: neighborhoods[element])
    list_of_neighborhoods.reverse()

    return([
        [hood for hood in list_of_neighborhoods], 
        [neighborhoods[hood] for hood in list_of_neighborhoods]
    ])

lead_levels = get_blood_lead_levels()