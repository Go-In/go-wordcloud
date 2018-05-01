import sys
import csv
import pandas as pd

posts_data = []

count = 0

with open('post.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['user_id'] in ['3628099245', '193904360', '183683575', '32491004', '1258755888', '3229691469', '342005484', '578578647', '1180519026', '4965671393', '14531662', '365940386', '29720794', '207448830', '2243447781', '420023789', '45967409', '1195098698', '201883385', '1519917150', '648669145']:
            posts_data.append(row['caption'])
            print(row['caption'])
            count += 1