#scrape postcode data from Pos Malaysia API
import pandas as pd
import requests
from tqdm import tqdm

num = ["%.4d" % i for i in range(0,10000)]

def get_postcode(num):
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    url = "https://api.pos.com.my/PostcodeWebApi/api/Postcode?Postcode={}0".format(i)
    data = requests.get(url, headers=headers).json()
    return data

mergedcode = []
for i in num:
    new = get_postcode(i)
    if all(elem in mergedcode for elem in new):
        continue
    else:
        mergedcode.extend(new)
