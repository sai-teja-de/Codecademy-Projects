#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# In this project, you will act as a data visualization developer at Yahoo Finance! You will be helping the "Netflix Stock Profile" team visualize the Netflix stock data. In finance, a _stock profile_ is a series of studies, visualizations, and analyses that dive into different aspects a publicly traded company's data. 
# 
# For the purposes of the project, you will only visualize data for the year of 2017. Specifically, you will be in charge of creating the following visualizations:
# + The distribution of the stock prices for the past year
# + Netflix's earnings and revenue in the last four quarters
# + The actual vs. estimated earnings per share for the four quarters in 2017
# + A comparison of the Netflix Stock price vs the Dow Jones Industrial Average price in 2017 
# 
# Note: We are using the Dow Jones Industrial Average to compare the Netflix stock to the larter stock market. Learn more about why the Dow Jones Industrial Average is a general reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp).
# 
# During this project, you will analyze, prepare, and plot data. Your visualizations will help the financial analysts asses the risk of the Netflix stock.
# 
# Financial Data Source: [Yahoo Finance](https://finance.yahoo.com/quote/DATA/)
# 

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# Let's load the datasets and inspect them.

# Note: In the Yahoo Data, `Adj Close` represents the adjusted close price adjusted for both dividends and splits. This means this is the true closing stock price for a given business day.

# In[2]:


netflix_stocks=pd.read_csv('NFLX.csv')
netflix_stocks.head()


# Note: You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). 
# 

# In[3]:


dowjones_stocks=pd.read_csv('DJI.csv')
dowjones_stocks.head()


# In[4]:


netflix_stocks_quarterly=pd.read_csv('NFLX_daily_by_quarter.csv')
netflix_stocks_quarterly.head()


# In[5]:


netflix_stocks.columns


# In[6]:


netflix_stocks.rename(columns={'Adj Close':'Price'},inplace=True)
dowjones_stocks.rename(columns={'Adj Close':'Price'},inplace=True)
netflix_stocks_quarterly.rename(columns={'Adj Close':'Price'},inplace=True)


# In[7]:


netflix_stocks.head()


# In[8]:


dowjones_stocks.head()
netflix_stocks_quarterly.head()


# 
# 
# In this step, we will be visualizing the Netflix quarterly data! 
# 
# We want to get an understanding of the distribution of the Netflix quarterly stock prices for 2017. Specifically, we want to see in which quarter stock prices flucutated the most. We can accomplish this using a violin plot with four violins, one for each business quarter!
# 
# 

# In[9]:


sns.set()
ax = sns.violinplot(data=netflix_stocks_quarterly,x='Quarter',y='Price')
ax.set_title('Dsitribution of 2017 Netfilx Stock Prices by Quarter')
plt.show()


#  

#  

# 
# 
# Next, we will chart the performance of the earnings per share (EPS) by graphing the estimate Yahoo projected for the Quarter compared to the actual earnings for that quarters. We will accomplish this using a scatter chart. 
# 
# 
# 

# In[10]:


x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]
plt.scatter(x_positions,earnings_actual,color='red',alpha=0.5)
plt.scatter(x_positions,earnings_estimate,color='blue',alpha=0.5)
plt.legend(['Actual','Estimate'])
plt.xticks(x_positions, chart_labels)
plt.title('Earnings Per Share in Cents')
plt.show()


# ## Graph Literacy
# 
# + What do the purple dots tell us about the actual and estimate earnings per share in this graph? 
# In color theory red and blue mix to make purple.
# 

#  

#  

# In[11]:


# The metrics below are in billions of dollars
revenue_by_quarter = [2.79, 2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["2Q2017","3Q2017","4Q2017", "1Q2018"]

# Revenue
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.85 # Width of each bar
bars1_x = [t*element + w*n for element
             in range(d)]



# Earnings
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.85 # Width of each bar
bars2_x = [t*element + w*n for element
             in range(d)]





middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Revenue", "Earnings"]


# 
# 
# In this last step, we will compare Netflix stock to the Dow Jones Industrial Average in 2017. We will accomplish this by plotting two line charts side by side in one figure. 
# 

# In[19]:


# Left plot Netflix

plt.figure(figsize=(12,8))
ax1 = plt.subplot(2,1,1)
plt.plot(netflix_stocks['Date'], netflix_stocks['Price'],marker='o')
plt.subplots_adjust(wspace=.5)
plt.show()




# Right plot Dow Jones
plt.figure(figsize=(12,8))
ax2 = plt.subplot(2,1,2)
plt.plot(dowjones_stocks['Date'], dowjones_stocks['Price'],marker='s')
plt.subplots_adjust(wspace=.5)
plt.show()




# - How did Netflix perform relative to Dow Jones Industrial Average in 2017?
# - Which was more volatile?
# - How do the prices of the stocks compare?

#  

# In[ ]:




