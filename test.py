# retrieve log file
import requests

url = "https://s3.amazonaws.com/tcmg476/http_access_log"
r = requests.get(url, stream = True)

# download file
# parse file
# answer questions:
#     1. How many total requests were made in the time period represented in the log?
        # 726736
#     2. How many requests were made on each day? per week? per month?
        #
#     3. What percentage of the requests were not successful (any 4xx status code)?
        #
#     4. What percentage of the requests were redirected elsewhere (any 3xx codes)?
        #
#     5. What was the most-requested file?
        #
#     6. What was the least-requested file?
        #
# output data to screen (choose format: human readable, machine readable, plain text, JSON, etc)
# break logs down into separate files by month (log file should be split into 12 smaller files; should be written in the same directory as program file)
