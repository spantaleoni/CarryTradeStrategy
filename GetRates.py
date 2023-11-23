import requests
import re
from bs4 import BeautifulSoup

from w3lib.html import replace_entities
import pandas as pd
 
#https://www.global-rates.com/en/interest-rates/central-banks/central-banks.aspx






def GetGlobalRates(countries, printflg):
    #page = requests.get('https://intomillion.com/central-bank-rates/') # Getting page HTML through request
    page = requests.get('https://www.global-rates.com/en/interest-rates/central-banks/central-banks.aspx')
    soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup
    
    
    #print(soup)
    #links = soup.select("tr class=""tabledata1"") # Selecting all of the anchors with titles
    rows = soup.find_all('tr', {'class': re.compile('tabledata*')})
    
    #lines = rows.find_all('td')
    #results = [r.text.split(' ')[0].strip() for r in rows]
    res = [r.text.strip() for r in rows]
    results = [r.split('\n') for r in res]
    
    #print(results)
    data = []
    
    for row in results:
        name = row[1]
        value = format(row[2][:5], '1')
        value = float(value)
        data.append([name, value])
    
        #print(line)
        #print(val)
    
    df = pd.DataFrame(data, columns=['Name', 'Value'])
    
    #print(df)
    dfsorted = df.sort_values(by=['Value'], ascending=True)
    
    if printflg is True:
        print(dfsorted)
    
    dfsorted.to_csv('global_interest_rates.csv')
    
    if printflg is True:
        print("LONG => ", dfsorted['Name'].iloc[-1], "  ", "RATES => ", dfsorted['Value'].iloc[-1])
        print("SHORT => ", dfsorted['Name'].iloc[0], "  ", "RATES => ", dfsorted['Value'].iloc[0])
        
    return dfsorted




GlobalRatesDF = GetGlobalRates("all", 'False')