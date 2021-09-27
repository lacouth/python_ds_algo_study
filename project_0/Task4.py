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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

unique_callers = set()
unique_receivers = set()
unique_texts = set()
for row in texts:
    unique_texts.add(row[0])
    unique_texts.add(row[1])
for row in calls:
    unique_callers.add(row[0])
    unique_receivers.add(row[1])

telemarketers = unique_callers.difference(unique_receivers).difference(unique_texts)
print('These numbers could be telemarketers: ')
for phone in sorted(telemarketers):
    print(phone)