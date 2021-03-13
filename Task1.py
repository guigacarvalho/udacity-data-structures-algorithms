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
phone_set = set()
for text in texts:
    phone_set.add(text[0])
    phone_set.add(text[1])

for call in calls:
    phone_set.add(call[0])
    phone_set.add(call[1])

print("There are", len(phone_set), "different telephone numbers in the records.")