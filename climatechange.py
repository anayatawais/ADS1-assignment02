import matplotlib.pyplot as mp
import pandas as pd
import seaborn as sns
import scipy.stats
import plotly.express as px

def read_data(filename):
    data = pd.read_csv(filename, skiprows = 2)
    data = data.drop(['Country Code','Indicator Code'], axis = 1)
    data.set_index('Country Name', inplace = True)
    data_years = data.T
    data_countries = data
    return data_years, data_countries

filename = 'API_climatechange.csv'
data_years, data_countries = read_data(filename)

# Five indicators are selected from the climate change dataset
# PERcentage urban population
#Urban Population
# Total Population
#percentage urban population growth
# Agricultural land sq km
Per_Urban_total_population = data_countries.loc[data_countries['Indicator Name'] == 'Urban population (% of total population)'].T
Per_Urban_total_population = Per_Urban_total_population.drop("Indicator Name",axis=0)
Urban_population = data_countries.loc[data_countries['Indicator Name'] == 'Urban population'].T
Urban_population =Urban_population.drop("Indicator Name",axis=0)
Per_Urban_population_growth = data_countries.loc[data_countries['Indicator Name'] == 'Urban population growth (annual %)'].T
Per_Urban_population_growth = Per_Urban_population_growth.drop("Indicator Name",axis=0)
Population_total = data_countries.loc[data_countries['Indicator Name'] == 'Population, total'].T
Population_total = Population_total.drop("Indicator Name",axis=0)
Agricultural_land_sq_km = data_countries.loc[data_countries['Indicator Name'] == 'Agricultural land (sq. km)'].T
Agricultural_land_sq_km = Agricultural_land_sq_km.drop("Indicator Name",axis=0)

# Statistical properties of percentage urban population of five countries.
statis_prop = Per_Urban_total_population[['Pakistan','France','Sweden','Malaysia', 'United Kingdom']]
statis_prop.astype(float).describe()
# display the boxplot 

fig = px.box(statis_prop, y=['Pakistan','Malaysia','France','Sweden','United Kingdom'])
fig.show()


# Corrolation of Agricultural land for Pakistan and Malaysia
Pakistan_df = pd.concat([Agricultural_land_sq_km['Pakistan'], Population_total['Pakistan'], Urban_population['Pakistan'],Per_Urban_population_growth['Pakistan'],Per_Urban_total_population['Pakistan']],axis=1, ignore_index=True)
Pakistan_df.rename(columns={0: 'Agricultural_land_sq_km', 1: 'Population_total', 2: 'Urban_population', 3: 'Per_Urban_population_growth', 4: 'Per_Urban_total_population'}, inplace=True)
Pakistan_df = Pakistan_df.dropna()

matrix = Pakistan_df.astype(float).corr().round(2)
sns.heatmap(matrix, annot=True)
mp.show()
#Malaysia heatmap
Malaysia_df = pd.concat([Agricultural_land_sq_km['Malaysia'], Population_total['Malaysia'], Urban_population['Malaysia'],Per_Urban_population_growth['Malaysia'],Per_Urban_total_population['Malaysia']],axis=1, ignore_index=True)
Malaysia_df.rename(columns={0: 'Agricultural_land_sq_km', 1: 'Population_total', 2: 'Urban_population', 3: 'Per_Urban_population_growth', 4: 'Per_Urban_total_population'}, inplace=True)
Malaysia_df = Malaysia_df.dropna()

matrix = Malaysia_df.astype(float).corr().round(2)
sns.heatmap(matrix, annot=True)
mp.show()
#Trends

import matplotlib.pyplot as plt
Agricultural_land_sq_km.plot(y=['Sweden','Pakistan','France','United Kingdom','Malaysia'], use_index=True)
plt.savefig("Agricultural_land_sq_km.svg")
Population_total.plot(y=['Sweden','Pakistan','France','United Kingdom','Malaysia'], use_index=True)
plt.savefig("Population_total.svg")
Per_Urban_population_growth.plot(y=['Sweden','Pakistan','France','United Kingdom','Malaysia'], use_index=True)
plt.savefig("Per_Urban_population_growth.svg")
Urban_population.plot(y=['Sweden','Pakistan','France','United Kingdom','Malaysia'], use_index=True)
plt.savefig("Urban_population.svg")
Per_Urban_total_population.plot(y=['Sweden','Pakistan','France','United Kingdom','Malaysia'], use_index=True)
plt.savefig("Per_Urban_total_population.svg")
