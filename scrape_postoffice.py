#scrape post office information from Pos Malaysia website
import requests
import pandas as pd
from bs4 import BeautifulSoup

statelist = ["%.2d" % i for i in range(1,14+1)]

def get_list(state, page):
    url = "https://www.pos.com.my/postal-services/quick-access/?findOutletState={}&findOutletLocation=&page={}".format(state,page)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    table = soup.find('table')

    output_rows = []
    for table_row in table.findAll('tr'):
        columns = table_row.findAll('td')
        output_row = []
        for column in columns:
            text = column.text
            text = text.replace("\n","").replace("\r","")
            output_row.append(text)
        output_rows.append(output_row)

    del output_rows[:2]
    return output_rows

def save_state(state):
    filename = 'postoffice_{}_my.csv'.format(state)
    mergedlist = []
    for i in range(1,20+1):
        print(i)
        newlist = get_list(state, i)
        if all(elem in mergedlist for elem in newlist):
            break
        else:
            mergedlist.extend(newlist)
    df = pd.DataFrame(mergedlist)
    df.to_csv(filename)

for i in statelist:
    save_state(i)
