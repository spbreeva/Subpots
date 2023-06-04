from matplotlib import axes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 




pd.df = pd.read_csv('graths/winemag-data_first150k.csv')

data = pd.df['province'].value_counts()


x_values = data.index.values
y_values = data.values

fig, ax = plt.subplots()
ax.bar(x_values, y_values, color = 'blue')


plt.xlabel('Province')
plt.xticks(fontsize=7, fontname='Times New Roman')
plt.tick_params(axis='x', which='major', pad=5)
plt.ylabel('Count')
plt.ylabel("Province Value (log)")
plt.yscale("log")
plt.title('Number of Occurrences by Province')
plt.locator_params(axis='x', nbins=10)
fig.autofmt_xdate(rotation=90)


plt.savefig(f"province_plot.png")

plt.show()