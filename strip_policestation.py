# Filename: strip_policestation.py
# Author: Kevin Bing -- kevinrbing@gmail.com
# Made with Python 3.6.1

import re, string
import csv

'''
The following two functions represent a lot of judgement calls to clean up the
`PoliceDepartment` and `PoliceStation` columns.  Often times the data is messy
so this type of sanitaiton is needed to make it machine readeable.  Specifically
I'm trying to get everything to work in an Excel pivot table.
'''

pattern = re.compile('[\W_]+')

def PoliceDepartment_clean(clean_string):
    clean_string = pattern.sub('', clean_string) 
    if clean_string.startswith(('JERS', 'JC', 'WEST', 'NORTH', 'SOUTH', 'EAST')):
        clean_string = 'JERSEY CITY POLICE'
    elif clean_string.startswith(('HUDS', 'HC', 'SHER')):
        clean_string = 'HUDSON COUNTY SHERIFF'
    elif clean_string.startswith('BAYO'):
        clean_string = 'BAYONNE'
    elif 'KEARNY' in clean_string:
        clean_string = 'KEARNY'
    elif 'PARK' in clean_string:
        clean_string = 'StateParkService'
    else:
        clean_string = 'OTHER'
    return clean_string

def PoliceStation_clean(pstring, pdept):
    if 'SOUTH' in pstring:
        pstring = 'SOUTH'
    elif 'EAST' in pstring:
        pstring = 'EAST'
    elif 'NORTH' in pstring:
        pstring = 'NORTH'
    elif 'WEST' in pstring:
        pstring = 'WEST'
    elif 'JERSEY' in pdept:
        pstring = 'JC OTHER'
    else:
        pstring = pdept
    return pstring

r = csv.reader(open('MasterCrashFile_w_headers.csv', newline=''), delimiter=',')
w = csv.writer(open('MasterCrashFile_PoliceStation.csv', 'a', newline='\n', encoding='utf-8'))

for row in r:
    if row[0] != 'UniqueID': # Skip header row
        row[7] = PoliceDepartment_clean(row[7])
        row[8] = PoliceStation_clean(row[8], row[7])
    w.writerow(row)

# for some reason I have a dataloss of 12 rows


