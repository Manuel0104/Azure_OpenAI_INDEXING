from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
import pandas as pd
import re
import json 

## Define azureAI search settings
service_name = 'doc-search-preview'
index_name = 'mydata-index'
admin_key = '' #add your admin key
endpoint = f"https://{service_name}.search.windows.net/"
credentials = AzureKeyCredential(admin_key)

## Load the data (csv file)
file_path = 'data/customer_support_tickets.xlsx'
df = pd.read_excel(file_path)

## Initiliaze the client 
search_client = SearchClient(endpoint = endpoint, index_name = index_name, credential = credentials)

## Upload data to the Azure - AIsearch

data = []

for _, row in df.iterrows():  
    data.append({  
        "@search.action": "upload", 
        "TicketID": str(row['Ticket ID']), 
        "TicketType": row['Ticket Type'], 
        "TicketSubject": row['Ticket Subject'],
        "TicketDescription" : row['Ticket Description'],
        "TicketStatus": row ['Ticket Status'],
        "TicketPriority": row['Ticket Priority'],
        "TicketChannel": row['Ticket Channel']
    })  

result = search_client.upload_documents(data)  
print("Upload result:", result)
