from matplotlib import axes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

def plot_table(table, param1, param2, zvet):
    data = table[[param1,param2]].value_counts()
    x_values = data.index.map(str).values
    y_values = data.values
    fig, ax = plt.subplots()
    ax.bar(x_values, y_values, color = zvet)
    plt.xlabel(param1)
    plt.xticks(fontsize=7, fontname='Times New Roman')
    plt.tick_params(axis='x', which='major', pad=5)
    plt.ylabel(param2)
    plt.ylabel(f"{param1} Value (log)")
    plt.yscale("log")
    plt.locator_params(axis='x', nbins=10)
    fig.autofmt_xdate(rotation=90)
    plt.savefig(f"{param1}_{param2}_plot.png")
    plt.show()