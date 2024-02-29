from openpyxl import Workbook
import re
wb=Workbook()
ws=wb.active
import os
link=os.getcwd()#the text file should be saved under the project file
with open(link+'original_text.txt','r',encoding='utf-8') as file:
    content=file.read().split('\n')
    content2=[]
    for unit in content:
        if unit.strip() and unit !='* * *':
            if re.match(r'\[\d+\]\w+',unit):
                continue
            else:
                content2.append(unit)
    Chnewlist=[[i]for i in content2]
    
    for paragraph in Chnewlist:
        ws.append(paragraph)
    wb.save('aligntxt.xlsx')

with open(link+'translated_text.txt','r',encoding='utf-8') as file:
    content_k=file.read().split('\n') 
    contentkor=[item.strip() for item in content_k if item.strip()]
    kornewlist=[[k]for k in contentkor] 
    column_to_wrte='B'
    for i,paragraph in enumerate(contentkor,start=1):
        ws[column_to_wrte+str(i)]=paragraph
    wb.save('aligntxt.xlsx')


        
