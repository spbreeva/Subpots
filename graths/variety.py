from matplotlib import axes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from function import plot_table

pd.df = pd.read_csv('graths/winemag-data_first150k.csv')


plot_table(pd.df, 'variety', 'designation', 'green')