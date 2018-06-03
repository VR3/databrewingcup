import matplotlib.pyplot as plt
import pandas as pd

def replace_underscore(str):
  return str.replace('_', ' ')

# Read dataset
gini = pd.read_csv('../data/external/coeficiente_gini.csv', converters={'ENTIDAD': replace_underscore})

# Sum and average
gini['GINI'] = gini.sum(axis=1)/3

# Drop YEARS
gini = gini.drop(['2010', '2012', '2014'], axis=1)
# gini = gini.drop(gini.columns[0], axis=1)

# Sort
gini = gini.sort_values(by=['GINI'])

print(gini)

# Print dataframe to csv
gini.to_csv("../data/subagencias_modified_geopos_maxTemp_pib_gini.csv")

plt.plot(gini, linewidth=2, linestyle=':', label='GINI')

plt.title("Coeficiente GINI", fontsize=14, fontstyle='italic', fontweight='bold',)
plt.ylabel('GINI')
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titlesize'] = 10
plt.rcParams['xtick.labelsize'] = 8
plt.rcParams['ytick.labelsize'] = 8
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.titlesize'] = 12
plt.xticks(rotation=90)
plt.show()
