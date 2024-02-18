import sys
from bs4 import BeautifulSoup
import pandas as pd
import os
import csv


#function to extract tables from the html page
def met_data(month,year):
    file_html = open('Data/Html_Data/{}/{}.html'.format(year,month),'rb')
    plain_text = file_html.read()

    tempD = []
    finalD = []

    soup = BeautifulSoup(plain_text,"lxml")
    for table in soup.findAll('table',{'class':'medias mensuales numspan'}):
        for tbody in table:
            for tr in tbody:
                a = tr.get_text()
                tempD.append(a)
    
    rows = len(tempD)/15  #Getting the number of rows

    for times in range(round(rows)):
        newtempD = []
        for i in range(15):
            newtempD.append(tempD[0]) #appending the first 15 elemenys of the list to the new list as a row
            tempD.pop(0)  # removing the 0th element in the list
        finalD.append(newtempD) # appen the row to the final list

    length = len(finalD)

    finalD.pop(length-1) #removing the lasty element/row
    finalD.pop(0)  #removing the firsdt row (header labels)

    for a in range(len(finalD)):
        finalD[a].pop(6)
        finalD[a].pop(13)
        finalD[a].pop(12)
        finalD[a].pop(11)
        finalD[a].pop(10)
        finalD[a].pop(9)
        finalD[a].pop(0)

    return finalD

#Main Function
if __name__ == "__main__":
    if not os.path.exists("Data/CSV_Data"):
        os.makedirs("Data/CSV_Data")
    for year in range(2013,2023):
        final_data = []
        with open("Data/CSV_Data/real_"+str(year)+'.csv','w') as csvfile:
            wr = csv.writer(csvfile,dialect = 'excel')
            wr.writerow(['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM'])
        #iterating through the months
        for month in range(1,13):
            temp = met_data(month,year)
            final_data = final_data+temp
        
        #Checking & removing null values
        with open("Data/CSV_Data/real_"+str(year)+'.csv','a') as csvfile:
            wr = csv.writer(csvfile,dialect = 'excel')
            for row in final_data:
                flag = 0
                for elem in row:
                    if elem =="" or elem=="-":
                        flag=1
                if flag !=1:
                    wr.writerow(row)

