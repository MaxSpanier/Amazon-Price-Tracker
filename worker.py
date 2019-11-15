from scraper import scrape
from scraper import get_time
import numpy as np
import pandas as pd
from pandas import ExcelWriter, ExcelFile
from xlrd import open_workbook, cellname
import os
from time import sleep

'''
To change the product to track
    1. change the URL variable to the desired amazon link
    2. create a new excel file in the working directory and name whatever you      want
    3. change the excel_file_name variable to the just created .xlsx files name
'''

#url of the wanted product
URL = 'https://www.amazon.de/Samsung-Smartphone-Touch-Display-interner-Speicher-Schwarz/dp/B079SNGV9P?ref_=Oct_RAsinC_Ajax_3468301_1&pf_rd_r=YF1F1F75XK5W087HY38M&pf_rd_p=34f30df4-f7fa-5d71-9c73-291146886fa2&pf_rd_s=merchandised-search-10&pf_rd_t=101&pf_rd_i=3468301&pf_rd_m=A3JWKAKR8XB7XF'

#name of the excel file wich the methods write and read
#the file must exist in the same directory
excel_file_name = 'S9+.xlsx'
#three arrays to store the values of the product and time
namesList = []
priceList = []
dateList = []

#calls the scraper and appends the data to the fitting array
def write_data(url):
    name, price, date = scrape(url)
    namesList.append(name)
    priceList.append(price)
    dateList.append(date)

#writes the arrays into the dataframe and the writes the dataframe into the excel sheet
def write_excel(excel_file):
    df = pd.DataFrame({'Name': namesList,
                        'Preis': priceList,
                        'Datum': dateList})
    df.to_excel(excel_file, sheet_name='Tabelle1', index=False)

def change_product():
    return 0

#clears the arrays -> extracts the data from the excel sheet and appends it to the arrays -> deletes the excel file and creates a new one
def read_data(excel_file, nL, pL, dL):
    #nL = namesList | pL = priceList | dL = dateList
    if (nL and pL and dL):
        nL = []
        pL = []
        dL = []

    if os.stat(excel_file).st_size != 0:
        excel_df = pd.read_excel(excel_file, sheet_name='Tabelle1')
        for i in range(0, len(excel_df)):
            nL.append(excel_df.at[i, 'Name'])
        for i in range(0, len(excel_df)):
            pL.append(excel_df.at[i, 'Preis'])
        for i in range(0, len(excel_df)):
            dL.append(excel_df.at[i, 'Datum'])

    os.remove(excel_file)
    f = open(excel_file, 'w+')
    f.close()

#processes the data with the methods above
def work():
    read_data(excel_file_name, namesList, priceList, dateList)
    write_data(URL)
    write_excel(excel_file_name)

#starts the routine of scraping and writing
#change the time variable to change the delay between the searches
def start_routine():
    while(True):
        time = 5
        cur_time = get_time()
        print('Writing at', cur_time)
        work()
        print('Sleeping for', time, 'seconds...')
        print('-----------------------------------')
        sleep(time)
