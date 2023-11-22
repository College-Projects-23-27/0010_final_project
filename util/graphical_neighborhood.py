import matplotlib.pyplot as plot

def graph_data(neighborhoods, values):
    plot.bar(neighborhoods, values)
    plot.xticks(rotation=90, fontsize='x-small')
    plot.autoscale(enable=True, axis='x', tight=False)
    plot.tight_layout()
    plot.show()