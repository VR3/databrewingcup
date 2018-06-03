import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

# Read dataset
tourism = pd.read_csv('../data/external/Actividad_Turistica.csv', encoding="latin-1")

# rm YEAR, METRIC UNIT cols
tourismSub = tourism.loc[tourism['Ano'] >= 2012]

tourismSub = tourismSub.drop(['Ano','LlegTur_Tot','LlegTur_Nac','LlegTur_Ext','TurNoch_Tot','TurNoch_Nac','TurNoch_Ext','Estad_Tot','Dens_Tot'], axis=1)

# Sum and average
tourismSub.Porc_Ocup = pd.to_numeric(tourismSub.Porc_Ocup, errors='coerce')

# Sort values by occupancy percentage
tourismSubAvg = tourismSub.dropna(how='all').groupby(['Estado']).sum(axis=1)/3
tourismSubAvg = tourismSubAvg.sort_values(by=['Porc_Ocup'])

print(tourismSubAvg)

# Print dataframe to csv
tourismSubAvg.to_csv("../data/subagencias_modified_geopos_maxTemp_pib_tourism.csv")

plt.plot(tourismSubAvg, linewidth=2, linestyle=':', marker='v', label='PIB')

plt.style.use('seaborn-white')
plt.title("Ocupación Porcentual", fontsize=14, fontstyle='italic', fontweight='bold',)
plt.ylabel('Porcentaje')
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titlesize'] = 10
plt.rcParams['xtick.labelsize'] = 8
plt.rcParams['ytick.labelsize'] = 8
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.titlesize'] = 12
plt.xticks(rotation=90)
plt.show()
