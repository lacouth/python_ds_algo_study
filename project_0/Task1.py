"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
uniques = set()
for row in texts:
    uniques.add(row[0])
    uniques.add(row[1])
for row in calls:
    uniques.add(row[0])
    uniques.add(row[1])

print(f'There are {len(uniques)} different telephone numbers in the records.')
    
