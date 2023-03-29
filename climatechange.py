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
