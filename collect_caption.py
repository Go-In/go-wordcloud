import sys
import csv
import pandas as pd

posts_data = []

count = 0

with open('post.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        posts_data.append(row['caption'])
        print(row['caption'])
        count += 1