import os
import time
import requests
import sys

#Function to retrieve the html pages
def retrieve_html():
    #looping through the years
    for year in range(2013,2023):
        #looping through the months
        for month in range(1,13):
            if month<10:
                url = 'https://en.tutiempo.net/climate/0{}-{}/ws-637400.html'.format(month,year)
            else:
                url = 'https://en.tutiempo.net/climate/{}-{}/ws-637400.html'.format(month,year)
        
            texts = requests.get(url)
            text_utf = texts.text.encode('utf=8')

            if not os.path.exists("Data/Html_Data/{}".format(year)):
                os.makedirs("Data/Html_Data/{}".format(year))
            with open("Data/Html_Data/{}/{}.html".format(year,month),"wb") as output:
                output.write(text_utf)
        
        sys.stdout.flush()


#write the main function
if __name__=="__main__":
    start_time = time.time()
    #calling the function
    retrieve_html()
    stop_time = time.time()
    print("Time Taken {}".format(stop_time - start_time))