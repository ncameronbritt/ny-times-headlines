# get count of ebola-related articles from NY Times headlines for the past 60 days
import datetime
from time import sleep
import csv
import requests

#key for NY Times Article Search API
ny_times_api_key = '320e4aac7ecfbb1143eab253e1cc9549:10:66365660'

outfile = open('ebola_headlines.csv', 'w')
csv_writer = csv.writer(outfile)

header = ['date','article_count']
csv_writer.writerow(header)

base_url = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?'

start_date = datetime.date.today() #start date, here
numDays = 60 #num days to look back from start date

# iterate over date range
for i in range(0, numDays):
    #dateList.append(today - datetime.timedelta(days = i))
    day = today - datetime.timedelta(days = i)
    date_string = day.strftime('%Y%m%d')
    
    payload = (    ('q','ebola'), 
                   ('begin_date', date_string) ,
                   ('end_date', date_string),
                   ('sort','oldest'),
                   ('fl','pub_date,headline,snippet'),
                   ('api-key',ny_times_api_key)
               )
    
    r = requests.get(base_url, params = payload)
    json = r.json()
    count  = json['response']['meta']['hits']
    print str(day), count
    csv_writer.writerow([str(day),count])
    sleep(.1)

    
outfile.close()