import pandas as pd

def get_pittsburgh_obesity_areas():
    data = pd.read_csv("datasets/obesity-ac-2006-2010censustracts.csv")
    obesity_by_neighborhood = {}

    for i in range(len(data)):
        data_point = data.iloc[i]
        municipality = data_point['Municipality'].strip()  # Removes leading/trailing spaces
        neighborhood = data_point['City Neighborhood']
        obesity_rate = float(data_point['2006-2010 estimate of obesity'])

        # Check if the municipality is 'Pittsburgh', accounting for case variations
        if municipality.lower() == "pittsburgh":
            if neighborhood not in obesity_by_neighborhood:
                obesity_by_neighborhood[neighborhood] = []

            obesity_by_neighborhood[neighborhood].append(obesity_rate)

    avg_obesity_by_neighborhood = {neighborhood: sum(rates)/len(rates) for neighborhood, rates in obesity_by_neighborhood.items()}

    sorted_neighborhoods = sorted(avg_obesity_by_neighborhood, key=avg_obesity_by_neighborhood.get, reverse=False)

    return [sorted_neighborhoods, [avg_obesity_by_neighborhood[neighborhood] for neighborhood in sorted_neighborhoods]]

pittsburgh_obesity_areas = get_pittsburgh_obesity_areas()