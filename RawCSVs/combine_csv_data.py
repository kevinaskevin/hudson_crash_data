# Filename: combine_csv_data.py
# Author: Kevin Bing -- kevinrbing@gmail.com
# Made with Python 3.6.1

'''
This is the Python code that stiches together the various csv files that can be downloaded from http://www.state.nj.us/transportation/refdata/accident/ 
'''

import fileinput, sys, csv

fileyear = 2005
filelist = []
for number in range(11):
    filelist.append('Hudson' + str(fileyear + number) + 'Accidents.txt')
print(filelist) # This is just a list with consecutive years from 2005-2015

for filename in filelist:
    print(filename)
    r = csv.reader(open(filename, 'rt'), delimiter=',')
    # for writer 'a' is append. 'w' is write over
    w = csv.writer(open('MasterCrashFile.csv', 'a', newline='\n', encoding='utf-8'))
    for row in r:
        try:
		    # Filters for just Jersey City
            if row[2][:6] == 'JERSEY': 
                w.writerow(row)
        except:
            # there's some thing with the PO Box and Woodbridge.
            # It seems to be NJTPA's address thats throwing an error
            print('.')
