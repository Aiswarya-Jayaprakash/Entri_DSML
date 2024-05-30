#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from a file
file_name = "E:\\ENTRI DSML\\Python\\fifa_data.csv"
df = pd.read_csv(file_name)

# Display basic information about the dataset
print(df.info())
print(df.head())


# In[4]:


# 1. Which country has the most number of players?
country = df['Nationality'].value_counts()
most_players_country = country.idxmax()
print(f"The country with the most number of players is {most_players_country} with {country.max()} players.")


# In[9]:


# 2. Plot a bar chart of 5 top countries with the most number of players.
top_5_countries = country.head(5)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_5_countries.index, y=top_5_countries.values, palette='viridis')
plt.title('Top 5 Countries with the Most Number of Players')
plt.xlabel('Country')
plt.ylabel('Number of Players')
plt.show()
print("2. The top 5 countries with the most players are shown in the bar chart and have well-established football programs.")


# In[27]:


# 3. Which player has the highest salary?
highest_salary_player = df.loc[df['Wage'] == df['Wage'].max(), ['Name', 'Wage']]
print(f"The player with the highest salary is {highest_salary_player.iloc[0]['Name']} with a salary of {highest_salary_player.iloc[0]['Wage']}.")


# In[15]:


# 4. Plot a histogram to get the salary range of the players.
df['Wage'] = df['Wage'].astype(str).str.replace('€', '').str.replace('K', '').astype(float)
plt.figure(figsize=(10, 6))
plt.hist(df['Wage'], bins=30, color='blue', edgecolor='black')
plt.title('Salary Range of Players')
plt.xlabel('Salary (in thousands of euros)')
plt.ylabel('Number of Players')
plt.show()
print("4. The histogram shows the salary range of players. Most players earn between 0 and 100 thousand euros which indicates  a wide range of salaries is offered to players.")


# In[24]:


# 5. Who is the tallest player in the fifa?
tallest_player = df.sort_values(by=['Height'], ascending = False)
tallest_player[['Name', 'Height']].head(1)
print(f"The tallest player is {tallest_player.iloc[0]['Name']} with a height of {tallest_player.iloc[0]['Height']}.")


# In[18]:


#6. Which club has the most number of players?
club = df['Club'].value_counts()
most_players_club = club.idxmax()
print(f"The club with the most number of players is {most_players_club} with {club.max()} players.")


# In[17]:


preferred_foot_counts = df['Preferred Foot'].value_counts()
plt.figure(figsize=(10, 6))
preferred_foot_counts.plot(kind='bar', color='green')
plt.title('Preferred Foot of Players')
plt.xlabel('Preferred Foot')
plt.ylabel('Number of Players')
plt.show()
print("7. The most preferred foot among players is {}.".format(preferred_foot_counts.idxmax()))

