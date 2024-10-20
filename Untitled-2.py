#!/usr/bin/env python
# coding: utf-8

# # Starting Code

# In[2]:


import yfinance as yf


# # Question 1 - Extracting Tesla Stock Data Using yfinance

# In[3]:


tsla = yf.Ticker("TSLA")
tsla_data = tsla.history(period="max")
tsla_data.head()


# # Question 2 - Extracting Tesla Revenue Data Using Webscraping

# In[8]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website containing revenue data
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'

# Send a GET request to fetch the HTML content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Initialize an empty list to store the scraped data
data = []

# Extract rows from the second tbody element that contains the revenue data
for row in soup.find_all("tbody")[1].find_all('tr'):
    col = row.find_all("td")
    date = col[0].text.strip()
    revenue = col[1].text.strip()

    # Append the date and revenue to the data list
    data.append({"Date": date, "Revenue": revenue})

# Convert the list of dictionaries to a DataFrame
tesla_revenue = pd.DataFrame(data)

# Display the last five rows of the DataFrame
print(tesla_revenue.tail())





# # Question 3 - Extracting GameStop Stock Data Using yfinance

# In[4]:


gme = yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.head()


# # Question 4 - Extracting GameStop Revenue Data Using Webscraping

# In[9]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website containing revenue data
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'

# Send a GET request to fetch the HTML content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Initialize an empty list to store the scraped data
data = []

# Extract rows from the second tbody element that contains the revenue data
for row in soup.find_all("tbody")[1].find_all('tr'):
    col = row.find_all("td")
    date = col[0].text.strip()
    revenue = col[1].text.strip()

    # Append the date and revenue to the data list
    data.append({"Date": date, "Revenue": revenue})

# Convert the list of dictionaries to a DataFrame
tesla_revenue = pd.DataFrame(data)

# Display the last five rows of the DataFrame
print(tesla_revenue.tail())



    


# # Question 5 - Tesla Stock and Revenue Dashboard

# In[12]:


import yfinance as yf
import matplotlib.pyplot as plt

# Function to create and display a stock price graph
def make_graph(data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], label='Close Price', color='blue', marker='o', linestyle='-')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Close Price (USD)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Download Tesla stock data for the entire history
tesla_stock = yf.download('TSLA', period="max")

# Call the make_graph function with Tesla stock data for all available history
make_graph(tesla_stock, 'Tesla Historical Stock Prices (All Time)')
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests

# URL of the website containing revenue data
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'

# Send a GET request to fetch the HTML content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Initialize an empty list to store the scraped data
data = []

# Extract rows from the second tbody element that contains the revenue data
for row in soup.find_all("tbody")[1].find_all('tr'):
    col = row.find_all("td")
    date = col[0].text.strip()  # Extract the date
    revenue = col[1].text.strip().replace('$', '').replace(',', '')  # Clean the revenue data
    data.append({"Date": date, "Revenue": revenue})  # Append to data list

# Convert the list of dictionaries to a DataFrame
tesla_revenue = pd.DataFrame(data)

# Remove any rows where revenue is empty or invalid
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != '']

# Convert Revenue to numeric
tesla_revenue['Revenue'] = pd.to_numeric(tesla_revenue['Revenue'], errors='coerce')

# Sort by Date to ensure chronological order
tesla_revenue['Date'] = pd.to_datetime(tesla_revenue['Date'], errors='coerce', format='%b %Y')
tesla_revenue = tesla_revenue.dropna().sort_values('Date')

# Function to create and display a revenue graph
def plot_revenue(data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Revenue'], marker='o', linestyle='-', color='green')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Revenue (in billions USD)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Call the plot_revenue function with Tesla revenue data
plot_revenue(tesla_revenue, 'Tesla Revenue Over Time (Scraped Data)')



# # Question 6 - GameStop Stock and Revenue Dashboard

# In[13]:


import yfinance as yf
import matplotlib.pyplot as plt

# Function to create and display a stock price graph
def make_graph(data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], label='Close Price', color='blue', marker='o', linestyle='-')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Close Price (USD)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Download Tesla stock data for the entire history
tesla_stock = yf.download('GME', period="max")

# Call the make_graph function with Tesla stock data for all available history
make_graph(tesla_stock, 'Tesla Historical Stock Prices (All Time)')


# # Question 7 - Sharing your Assignment Notebook

# In[ ]:


https://github.com/patocastro/ibm-notebook.git

