# coding: utf8
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Dataframe in Pandas
df = pd.read_csv('../data/subagencias_modified_geopos.csv')

# Read datasets
tMax = pd.read_csv('../data/external/Temperatura_maxima.csv', encoding='utf8')
tAvg = pd.read_csv('../data/external/Temperatura_promedio.csv', encoding='utf8')
tMin = pd.read_csv('../data/external/Temperatura_minima.csv', encoding='utf8')

# Filter dataset
tMaxSub = tMax.loc[tMax['ANO'] >= 2013]
tAvgSub = tAvg.loc[tAvg['ANO'] >= 2013]
tMinSub = tMin.loc[tMin['ANO'] >= 2013]

# rm YEAR, METRIC UNIT cols
tMaxSub = tMaxSub.drop(['ANO', 'UNIDAD DE MEDICION'], axis=1)
tMinSub = tMinSub.drop(['ANO', 'UNIDAD DE MEDICION'], axis=1)

# Remove NA or empty values
# group by state and sum the values of [3:14]
# and avg by last 3 years [2013:2015]
tMaxSubAvg = tMaxSub.dropna(how='all').groupby(['ENTIDAD']).sum()/3
tMinSubAvg = tMinSub.dropna(how='all').groupby(['ENTIDAD']).sum()/3

# Group by month and avg by 12
tMaxSubAvg['MAX TEMP'] = tMaxSubAvg.sum(axis=1)/12
tMinSubAvg['MIN TEMP'] = tMinSubAvg.sum(axis=1)/12
 
# rm MONTHS cols
#print(tMaxSubAvg.columns)
tMaxSubAvg = tMaxSubAvg.drop(tMaxSubAvg.columns[0:12], axis=1)
tMinSubAvg = tMinSubAvg.drop(tMinSubAvg.columns[0:12], axis=1)

# Combine dataframes
tSubAvg = pd.concat([tMaxSubAvg, tMinSubAvg], axis=1)

# sort dataframe by high - low
tSubAvg = tSubAvg.sort_values(by=['MAX TEMP'])

# Print dataframe to csv
tSubAvg.to_csv("../data/subagencias_modified_geopos_maxTemp.csv")

plt.plot(tSubAvg, linewidth=2, linestyle=':', marker='v', label='Temperatura')

plt.style.use('seaborn-white')
plt.title("Min/Max Temperatura por Estado", fontsize=14, fontstyle='italic', fontweight='bold',)
plt.ylabel('Temperatura')
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titlesize'] = 10
plt.rcParams['xtick.labelsize'] = 8
plt.rcParams['ytick.labelsize'] = 8
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.titlesize'] = 12
plt.xticks(rotation=90)
plt.show()
