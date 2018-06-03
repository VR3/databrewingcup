import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

def strip_chars(str):
    return str.replace(u"\xa0", u"")
def strip_spaces(str):
    return str.replace(u" ", u"")

# Read datasets
pib = pd.read_csv('../data/external/PIB_Entidad_Federativa.csv', skipinitialspace=True, index_col=0, converters={'2014': strip_chars, '2015': strip_chars, '2016': strip_spaces})


# rm YEAR, METRIC UNIT cols
pibSub = pib.drop(['2003', '2007', '2010'], axis=1)

# Sum and average
pibSub['PIB'] = pibSub.sum(axis=1)/3

# Drop YEARS
pibSubAvg = pibSub.drop(['2014', '2015', '2016'], axis=1)

print(pibSubAvg)

# Print dataframe to csv
pibSubAvg.to_csv("../data/subagencias_modified_geopos_maxTemp_pib.csv")

plt.plot(pibSubAvg, linewidth=2, linestyle=':', marker='v', label='PIB')

plt.style.use('seaborn-white')
plt.title("PIB Estatal Promedio 3 Años", fontsize=14, fontstyle='italic', fontweight='bold',)
plt.ylabel('PIB')
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titlesize'] = 10
plt.rcParams['xtick.labelsize'] = 8
plt.rcParams['ytick.labelsize'] = 8
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.titlesize'] = 12
plt.xticks(rotation=90)
plt.show()
