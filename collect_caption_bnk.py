import sys
import csv
import pandas as pd

posts_data = []

count = 0

with open('post.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['user_id'] in ['4636716008', '4637027618', '4636727204', '4636949254', '4636773691', '4636929947', '4637960766', '4636727323', '4636901761', '4636911622', '4636817438', '4637003212', '4636884027', '4636818387', '4636856314', '4636805439', '4636779495', '4637883190', '4636714065', '4636729266', '4636793604', '4636917839', '4636948310', '4636878303', '4636895671', '5510050298', '3040495379', '1413656901']:
            posts_data.append(row['caption'])
            print(row['caption'])
            count += 1