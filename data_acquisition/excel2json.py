import pandas as pd
import json, os
link=os.path.realpath('training text.xlsx')
data=pd.read_excel(link)
json_data=[]
json_data2=[]
for index,row in data.iterrows():
    Chinese_text=row['Chinese']
    Korean_text=row['Korean']
    json_data.append({'instruction':'请将下列中文翻译成韩文','input':Chinese_text,'output':Korean_text})
    json_data2.append({'instruction':'请将下列韩文翻译成中文','input':Korean_text,'output':Chinese_text})
with open('datatest_Chn2Kor.json','w',encoding='utf-8')as json_file:
    json.dump(json_data,json_file,ensure_ascii=False,indent=4)
with open('datatest_Kor2Chn.json','w',encoding='utf-8')as json_file:
    json.dump(json_data2,json_file,ensure_ascii=False,indent=4)

