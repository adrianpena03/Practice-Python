# Pandas is a Python library for data manipulation and analysis. 
# Download this CSV file and take a look at it. Use pandas library to read this file as a data frame.
# Write a program to find the name of the company that has the most expensive car. 
# Print out the name of this company. The correct output is mercedes-benz.

import pandas as pd

df = pd.read_csv('Automobile_data.csv')

max_price = df['price'].max()
company_name = df.loc[df['price'] == max_price, 'company'].iloc[0]

print(company_name)
