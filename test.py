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

total = 0

# number of requests for each day
# for x in range(31):
#         if x < 9:
#                 date = "/Oct/1994"
#                 date = "0" + str(x + 1) + date
#                 print(date)
#                 with open('Oct1994.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0
#         else:
#                 date = "/Oct/1994"
#                 date = str(x + 1) + date
#                 print(date)
#                 with open('Oct1994.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0

# for x in range(31):
#         if x < 9:
#                 date = "/Nov/1994"
#                 date = "0" + str(x + 1) + date
#                 print(date)
#                 with open('Nov1994.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0
#         else:
#                 date = "/Nov/1994"
#                 date = str(x + 1) + date
#                 print(date)
#                 with open('Nov1994.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0

# for x in range(31):
#         if x < 9:
#                 date = "/Dec/1994"
#                 date = "0" + str(x + 1) + date
#                 print(date)
#                 with open('Dec1994.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0
#         else:
#                 date = "/Dec/1994"
#                 date = str(x + 1) + date
#                 print(date)
#                 with open('Dec1994.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0

# for x in range(31):
#         if x < 9:
#                 date = "/Jan/1995"
#                 date = "0" + str(x + 1) + date
#                 print(date)
#                 with open('Jan1995.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0
#         else:
#                 date = "/Jan/1995"
#                 date = str(x + 1) + date
#                 print(date)
#                 with open('Jan1995.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0

# for x in range(31):
#         if x < 9:
#                 date = "/Feb/1995"
#                 date = "0" + str(x + 1) + date
#                 print(date)
#                 with open('Feb1995.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0
#         else:
#                 date = "/Feb/1995"
#                 date = str(x + 1) + date
#                 print(date)
#                 with open('Feb1995.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0

# for x in range(31):
#         if x < 9:
#                 date = "/Mar/1995"
#                 date = "0" + str(x + 1) + date
#                 print(date)
#                 with open('Mar1995.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0
#         else:
#                 date = "/Mar/1995"
#                 date = str(x + 1) + date
#                 print(date)
#                 with open('Mar1995.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0

# for x in range(31):
#         if x < 9:
#                 date = "/Apr/1995"
#                 date = "0" + str(x + 1) + date
#                 print(date)
#                 with open('Apr1995.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0
#         else:
#                 date = "/Apr/1995"
#                 date = str(x + 1) + date
#                 print(date)
#                 with open('Apr1995.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0

# for x in range(31):
#         if x < 9:
#                 date = "/May/1995"
#                 date = "0" + str(x + 1) + date
#                 print(date)
#                 with open('May1995.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0
#         else:
#                 date = "/May/1995"
#                 date = str(x + 1) + date
#                 print(date)
#                 with open('May1995.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0

# for x in range(31):
#         if x < 9:
#                 date = "/Jun/1995"
#                 date = "0" + str(x + 1) + date
#                 print(date)
#                 with open('Jun1995.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0
#         else:
#                 date = "/Jun/1995"
#                 date = str(x + 1) + date
#                 print(date)
#                 with open('Jun1995.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0

# for x in range(31):
#         if x < 9:
#                 date = "/Jul/1995"
#                 date = "0" + str(x + 1) + date
#                 print(date)
#                 with open('Jul1995.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0
#         else:
#                 date = "/Jul/1995"
#                 date = str(x + 1) + date
#                 print(date)
#                 with open('Jul1995.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0

# for x in range(31):
#         if x < 9:
#                 date = "/Aug/1995"
#                 date = "0" + str(x + 1) + date
#                 print(date)
#                 with open('Aug1995.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0
#         else:
#                 date = "/Aug/1995"
#                 date = str(x + 1) + date
#                 print(date)
#                 with open('Aug1995.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0

# for x in range(31):
#         if x < 9:
#                 date = "/Sep/1995"
#                 date = "0" + str(x + 1) + date
#                 print(date)
#                 with open('Sep1995.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0
#         else:
#                 date = "/Sep/1995"
#                 date = str(x + 1) + date
#                 print(date)
#                 with open('Sep1995.txt') as f:
#                         for line in f:
#                                 finded = line.find(date)
#                                 if finded != -1 and finded != 0:
#                                         total += 1
#                 print(total)
#                 total = 0

# for x in range(31):
        # if x < 9:
        #         date = "/Oct/1995"
        #         date = "0" + str(x + 1) + date
        #         print(date)
        #         with open('Oct1995.txt') as f:
        #                 for line in f:
        #                         finded = line.find(date)
        #                         if finded != -1 and finded != 0:
        #                                 total += 1
        #         print(total)
        #         total = 0
        # else:
        #         date = "/Oct/1995"
        #         date = str(x + 1) + date
        #         print(date)
        #         with open('Oct1995.txt') as f:
        #                 for line in f:
        #                         finded = line.find(date)
        #                         if finded != -1 and finded != 0:
        #                                 total += 1
        #         print(total)
        #         total = 0
                
#       run for every date to get value
# Oct/1994: 11168
        # 24: 705
        # 25: 1194
        # 26: 1680
        # 27: 1889
        # 28: 1817
        # 29: 898
        # 30: 902
        # 31: 2083
# Nov/1994: 41251
        # 1: 1886
        # 2: 2106
        # 3: 2112
        # 4: 1775
        # 5: 568
        # 6: 582
        # 7: 1564
        # 8: 1260
        # 9: 1376
        # 10: 1216
        # 11: 710
        # 12: 487
        # 13: 613
        # 14: 1330
        # 15: 1207
        # 16: 2142
        # 17: 2266
        # 18: 1266
        # 19: 648
        # 20: 784
        # 21: 1777
        # 22: 1753
        # 23: 1520
        # 24: 1675
        # 25: 1349
        # 26: 681
        # 27: 588
        # 28: 1660
        # 29: 2237
        # 30: 2113
# Dec/1994: 29803
        # 1: 992
        # 2: 1324
        # 3: 712
        # 4: 591
        # 5: 1790
        # 6: 1378
        # 7: 1524
        # 8: 1467
        # 9: 1413
        # 10: 489
        # 11: 603
        # 12: 1708
        # 13: 1804
        # 14: 1265
        # 15: 1149
        # 16: 1071
        # 17: 1143
        # 18: 1102
        # 19: 1840
        # 20: 1249
        # 21: 1118
        # 22: 908
        # 23: 457
        # 24: 123
        # 25: 387
        # 26: 280
        # 27: 513
        # 28: 465
        # 29: 301
        # 30: 336
        # 31: 301
# Jan/1995: 43666
        # 1: 251
        # 2: 491
        # 3: 1016
        # 4: 885
        # 5: 1104
        # 6: 587
        # 7: 346
        # 8: 450
        # 9: 1345
        # 10: 1665
        # 11: 1346
        # 12: 1830
        # 13: 1680
        # 14: 481
        # 15: 760
        # 16: 1958
        # 17: 1488
        # 18: 1670
        # 19: 2306
        # 20: 1958
        # 21: 624
        # 22: 788
        # 23: 1566
        # 24: 2237
        # 25: 1923
        # 26: 2230
        # 27: 2005
        # 28: 1339
        # 29: 1268
        # 30: 2825
        # 31: 3244
# Feb/1995: 72112
        # 1: 2722
        # 2: 2845
        # 3: 2531
        # 4: 2707
        # 5: 1930
        # 6: 3589
        # 7: 5216
        # 8: 4409
        # 9: 5023
        # 10: 2972
        # 11: 1003
        # 12: 1938
        # 13: 3212
        # 14: 3393
        # 15: 3531
        # 16: 2598
        # 17: 2133
        # 18: 1676
        # 19: 1158
        # 20: 1555
        # 21: 1870
        # 22: 2786
        # 23: 2445
        # 24: 1824
        # 25: 1525
        # 26: 1267
        # 27: 2057
        # 28: 2197
# Mar/1995: 99761
        # 1: 2153
        # 2: 2097
        # 3: 1649
        # 4: 1414
        # 5: 1623
        # 6: 2892
        # 7: 3139
        # 8: 2682
        # 9: 2968
        # 10: 3373
        # 11: 1505
        # 12: 1616
        # 13: 3964
        # 14: 4473
        # 15: 4293
        # 16: 3686
        # 17: 1968
        # 18: 1485
        # 19: 1345
        # 20: 4787
        # 21: 6616
        # 22: 4169
        # 23: 4885
        # 24: 2046
        # 25: 2435
        # 26: 2160
        # 27: 4519
        # 28: 5376
        # 29: 6353
        # 30: 4627
        # 31: 3463
# Apr/1995: 65010
        # 1: 1652
        # 2: 1446
        # 3: 2914
        # 4: 3131
        # 5: 3486
        # 6: 3523
        # 7: 4016
        # 8: 2286
        # 9: 2501
        # 10: 3396
        # 11: 3485
        # 12: 3867
        # 13: 2338
        # 14: 1188
        # 15: 1029
        # 16: 1180
        # 17: 1507
        # 18: 1703
        # 19: 2306
        # 20: 2057
        # 21: 2229
        # 22: 1665
        # 23: 966
        # 24: 1433
        # 25: 1545
        # 26: 2337
        # 27: 1941
        # 28: 2006
        # 29: 1055
        # 30: 822
# May/1995: 63778
        # 1: 1511
        # 2: 2078
        # 3: 2426
        # 4: 2322
        # 5: 2402
        # 6: 3307
        # 7: 2300
        # 8: 2268
        # 9: 3318
        # 10: 2836
        # 11: 2400
        # 12: 1654
        # 13: 900
        # 14: 1092
        # 15: 1787
        # 16: 1729
        # 17: 1950
        # 18: 2274
        # 19: 2270
        # 20: 1114
        # 21: 2505
        # 22: 2923
        # 23: 2669
        # 24: 2159
        # 25: 3330
        # 26: 2159
        # 27: 805
        # 28: 582
        # 29: 1271
        # 30: 1642
        # 31: 1795
# Jun/1995: 53720
        # 1: 1944
        # 2: 1734
        # 3: 999
        # 4: 1117
        # 5: 1734
        # 6: 2378
        # 7: 1715
        # 8: 2061
        # 9: 1670
        # 10: 1028
        # 11: 866
        # 12: 1801
        # 13: 1832
        # 14: 2463
        # 15: 1841
        # 16: 1797
        # 17: 1339
        # 18: 991
        # 19: 2815
        # 20: 2022
        # 21: 2555
        # 22: 2369
        # 23: 1988
        # 24: 984
        # 25: 1625
        # 26: 2245
        # 27: 2197
        # 28: 2187
        # 29: 1819
        # 30: 1604
# Jul/1995: 54941
        # 1: 810
        # 2: 1221
        # 3: 1740
        # 4: 2580
        # 5: 1955
        # 6: 1747
        # 7: 1285
        # 8: 829
        # 9: 758
        # 10: 1743
        # 11: 2215
        # 12: 1830
        # 13: 1877
        # 14: 1818
        # 15: 1028
        # 16: 935
        # 17: 2181
        # 18: 1740
        # 19: 1906
        # 20: 1853
        # 21: 2070
        # 22: 1290
        # 23: 1636
        # 24: 2185
        # 25: 2916
        # 26: 2440
        # 27: 2468
        # 28: 2657
        # 29: 1291
        # 30: 1559
        # 31: 2378
# Aug/1995: 66077
        # 1: 2479
        # 2: 3138
        # 3: 2666
        # 4: 2828
        # 5: 1714
        # 6: 1541
        # 7: 1851
        # 8: 2796
        # 9: 2795
        # 10: 2657
        # 11: 1995
        # 12: 1178
        # 13: 1758
        # 14: 2804
        # 15: 2115
        # 16: 2267
        # 17: 2175
        # 18: 2053
        # 19: 991
        # 20: 1374
        # 21: 2219
        # 22: 2374
        # 23: 2774
        # 24: 2318
        # 25: 2260
        # 26: 1256
        # 27: 1242
        # 28: 2207
        # 29: 1937
        # 30: 2297
        # 31: 2018
# Sep/1995: 89095
        # 1: 1191
        # 2: 1019
        # 3: 654
        # 4: 1065
        # 5: 1171
        # 6: 1749
        # 7: 2382
        # 8: 3208
        # 9: 1602
        # 10: 1613
        # 11: 3543
        # 12: 3287
        # 13: 4746
        # 14: 3963
        # 15: 3764
        # 16: 1883
        # 17: 2021
        # 18: 3494
        # 19: 4079
        # 20: 4524
        # 21: 5471
        # 22: 3381
        # 23: 2897
        # 24: 2853
        # 25: 4358
        # 26: 4894
        # 27: 4153
        # 28: 4004
        # 29: 3822
        # 30: 2304
# Oct/1995: 34740
        # 1: 2174
        # 2: 4594
        # 3: 3818
        # 4: 3969
        # 5: 3718
        # 6: 3853
        # 7: 1548
        # 8: 2022
        # 9: 2814
        # 10: 3708
        # 11: 2522

# Weeks (Sunday-Saturday; dd/mm)
#    1994:
        # 23/10-29/10: 8183
        # 30/10-05/11: 11432
        # 06/11-12/11: 7195
        # 13/11-19/11: 9472
        # 20/11-26/11: 9539
        # 27/11-03/12: 9626
        # 04/12-10/12: 8652
        # 11/12-17/12: 8743
        # 18/12-24/12: 6797
        # 25/12-31/12: 2583
#    1995:
        # 01/01-07/01: 4680
        # 08/01-14/01: 8797
        # 15/01-21/01: 10764
        # 22/01-28/01: 12088
        # 29/01-04/02: 18142
        # 05/02-11/02: 24142
        # 12/02-18/02: 18481
        # 19/02-25/02: 13163
        # 26/02-04/03: 12834
        # 05/03-11/03: 18182
        # 12/03-18/03: 21485
        # 19/03-25/03: 26283
        # 26/03-01/04: 28150
        # 02/04-08/04: 20802
        # 09/04-15/04: 17804
        # 16/04-22/04: 12647
        # 23/04-29/04: 11283
        # 30/04-06/05: 14868
        # 07/05-13/05: 15676
        # 14/05-20/05: 12216
        # 21/05-27/05: 16550
        # 28/05-03/06: 9967
        # 04/06-10/06: 11703
        # 11/06-17/06: 11939
        # 18/06-24/06: 13724
        # 25/06-01/07: 12487
        # 02/07-08/07: 11357
        # 09/07-15/07: 11269
        # 16/07-22/07: 11975
        # 23/07-29/07: 15593
        # 30/07-05/08: 16762
        # 06/08-12/08: 14813
        # 13/08-19/08: 14163
        # 20/08-26/08: 14575
        # 27/08-02/09: 11911
        # 03/09-09/09: 11831
        # 10/09-16/09: 22799
        # 17/09-23/09: 25867
        # 24/09-30/09: 26388
        # 01/10-07/10: 23674
        # 08/10-14/10: 11066


#     3. What percentage of the requests were not successful (any 4xx status codes)?
# 215363
total = 0
#finds number of requests with 4XX error code
with open('httpaccesslog.txt') as f:
        for line in f:
                for x in range(100):
                        finded = line.find(str(x + 400))
                        if finded != -1:
                                total += 1
                                break
        print(total)
                      
#     4. What percentage of the requests were redirected elsewhere (any 3xx codes)?
#     5. What was the most-requested file?
#     6. What was the least-requested file?

# output data to screen (choose format: human readable, machine readable, plain text, JSON, etc)
# break logs down into separate files by month (log file should be split into 12 smaller files; should be written in the same directory as program file)
