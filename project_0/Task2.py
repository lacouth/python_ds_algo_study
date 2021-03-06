"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
phones = {}
def add_to_dict(phone,time):
    if phone in phones:
        phones[phone] += time
    else:
        phones[phone] = time

for row in calls:
    add_to_dict(row[0],int(row[-1]))
    add_to_dict(row[1],int(row[-1]))

phone_max = max(phones,key=phones.get)

print(f'{phone_max} spent the longest time, {phones[phone_max]} seconds, on the phone during September 2016.')


