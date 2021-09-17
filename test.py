import requests
import pandas as pd
from datetime import datetime
import re
import time

# Function that compiles all te functions
def main(request_data_file):

    read_csv_request_file(request_data_file)
    
  
             
def read_csv_request_file(excel_url):
   
    df = pd.read_excel(excel_url, sheet_name = 'Orders',skiprows=0 )
    
    for x,y in zip(df['Order Date'] , df['Sales'] ) :
        
        print("order date:",x, "sale \t",y)

#request_data_file = r'C:\Users\Administrator\Desktop\Orders-With.xlsx'
request_data_file = r'D:\python project\inventam_task\Orders-With.xlsx'
main(request_data_file)

main(request_data_file)
