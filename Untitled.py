#!/usr/bin/env python
# coding: utf-8

# # Starting Code

# In[1]:


import yfinance as yf


# # Question 1 - Extracting Tesla Stock Data Using yfinance

# In[2]:


tsla = yf.Ticker("TSLA")
tsla_data = tsla.history(period="max")
tsla_data.head()


# # Question 2 - Extracting Tesla Revenue Data Using Webscraping

# In[3]:


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

# Set up Selenium WebDriver
driver = webdriver.Chrome()

# Open the Yahoo Finance Tesla financials page
url = 'https://finance.yahoo.com/quote/TSLA/financials/'
driver.get(url)

# Wait for the table to be present
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )

    # Parse the page with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Locate the table and extract data
    table = soup.find('table')
    rows = table.find_all('tr')

    # Extract headers
    headers = [header.text for header in rows[0].find_all('th')]

    # Extract the data for the "Total Revenue" row
    total_revenue_row = None
    for row in rows:
        if 'Total Revenue' in row.text:
            total_revenue_row = [col.text.strip() for col in row.find_all('td')]
            break

    # Check if the row was found and create a DataFrame
    if total_revenue_row:
        df = pd.DataFrame([total_revenue_row], columns=headers)
        print(df)
        df.to_csv('tesla_total_revenue.csv', index=False)
    else:
        print("No data found for 'Total Revenue'.")
    
    # Keep the browser open for 30 seconds
    time.sleep(30)
        
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()




# # Question 3 - Extracting GameStop Stock Data Using yfinance

# In[ ]:


gme = yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.head()


# # Question 4 - Extracting GameStop Revenue Data Using Webscraping

# In[5]:


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

# Set up Selenium WebDriver
driver = webdriver.Chrome()

# Open the Yahoo Finance GameStop financials page
url = 'https://finance.yahoo.com/quote/GME/financials/'
driver.get(url)

# Wait for the table to be present
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )

    # Parse the page with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Locate the table and extract data
    table = soup.find('table')
    rows = table.find_all('tr')

    # Extract headers
    headers = [header.text for header in rows[0].find_all('th')]

    # Extract the data for the "Total Revenue" row
    total_revenue_row = None
    for row in rows:
        if 'Total Revenue' in row.text:
            total_revenue_row = [col.text.strip() for col in row.find_all('td')]
            break

    # Check if the row was found and create a DataFrame
    if total_revenue_row:
        df = pd.DataFrame([total_revenue_row], columns=headers)
        print(df)
        df.to_csv('gamestop_total_revenue.csv', index=False)
    else:
        print("No data found for 'Total Revenue'.")
    
    # Keep the browser open for 30 seconds
    time.sleep(30)
        
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()


# # Question 5 - Tesla Stock and Revenue Dashboard

# In[ ]:





# # Question 6 - GameStop Stock and Revenue Dashboard

# In[ ]:





# # Question 7 - Sharing your Assignment Notebook

# In[ ]:


https://github.com/patocastro/ibm-notebook.git

