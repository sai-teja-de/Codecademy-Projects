#importing libraries
import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

#reading csv to pandas data frame
df=pd.read_csv('WorldCupMatches.csv')

#adding a new column
df['Total Goals']=df['Home Team Goals']+df['Away Team Goals']

#plotting Total goals vs Year
sns.set_style('whitegrid')
sns.set_context('poster',font_scale=0.8)
f, ax = plt.subplots(figsize=(12,7))
ax = sns.barplot(data=df,x='Year',y='Total Goals')
ax.set_title("Average Number Of Goals Scored In World Cup Matches By Year")
plt.show()

#reading goals.csv to data frame
df_goals=pd.read_csv('goals.csv')
print(df_goals.head())

#plotting boxplot
sns.set_context('notebook',font_scale=1.25)
f, ax2 = plt.subplots(figsize=(12,7))
ax2 = sns.boxplot(data=df_goals,x='year',y='goals')
ax2.set_title('Goals in years')
plt.show()
