import plotly.graph_objects as go
import numpy as np
import pandas as pd
counties = {}
co_poverty = pd.read_csv('data.csv')
co_poverty = co_poverty.rename(columns={"County": "county_name", "Individuals Below Poverty Level": "below_poverty"})
us_cities = pd.read_csv('uscities.csv')
co_cities = us_cities[us_cities['state_id']=="CO"]
# by_county = co_cities.groupby(co_cities["county_name"])
by_county_df = pd.DataFrame({'count' : co_cities.groupby( [ "county_name", "lat","lng"] ).size()}).reset_index()
for index, row in by_county_df.iterrows():
    if row["county_name"] not in counties:
        counties[row["county_name"]+" County"] = [row["lat"], row["lng"]]

# final_pd = pd.concat([pd.DataFrame([keys, values[0], values[1]], columns=["county_name", "lat","long"]) for keys, values in counties.items()],ignore_index=True)

# print(final_pd.head())
almost_df = pd.DataFrame(columns=["county_name", "lat","long"])
for keys, values in counties.items():
   almost_df = almost_df.append({'county_name': keys,'lat': values[0], 'long': values[1]}, ignore_index=True)

final = pd.merge(co_poverty, almost_df, how='inner', on='county_name', left_on=None, right_on=None,
         left_index=False, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False,
         validate=None)
print(final)