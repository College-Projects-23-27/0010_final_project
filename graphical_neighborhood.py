import matplotlib.pyplot as plot
from lead_levels.lead_level import get_blood_lead_levels

def graph_data(neighborhoods, values):
    plot.bar(neighborhoods, values)
    plot.xticks(rotation=90, fontsize='x-small')
    plot.autoscale(enable=True, axis='x', tight=False)
    plot.tight_layout()
    plot.show()