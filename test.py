# retrieve log file
# download file
import requests

url = "https://s3.amazonaws.com/tcmg476/http_access_log"
r = requests.get(url, stream = True)

# parse file
    
regex = r"(.*) - - \[(.*)\] \"(.*?) (.*?\..*?) (HTTP\/\d\.\d)\" (\d*) (\d*)"

# answer questions:
#     1. How many total requests were made in the time period represented in the log?
#       726,736
#     2. How many requests were made on each day? per week? per month?
#       example: 
total = 0

with open('Oct1994.txt') as f:
        for line in f:
                finded = line.find('24/Oct/1994')
                if finded != -1 and finded != 0:
                        total += 1

print(total)
#       run for every date to get value
#     3. What percentage of the requests were not successful (any 4xx status code)?
#     4. What percentage of the requests were redirected elsewhere (any 3xx codes)?
#     5. What was the most-requested file?
#     6. What was the least-requested file?

# output data to screen (choose format: human readable, machine readable, plain text, JSON, etc)
# break logs down into separate files by month (log file should be split into 12 smaller files; should be written in the same directory as program file)
