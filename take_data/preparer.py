import pandas as pd

data=pd.read_csv(r'take_data\Hackathon.csv',encoding='utf-8')
places=list(data['Location'][1:])
categories=list(data.iloc[1:,2])
location_to_index={}

for idx,name in enumerate(places):
    location_to_index[name]=idx

def transform(places):
    global location_to_index
    ans=[]
    for i in places:
        ans.append(location_to_index[i])
    return ans