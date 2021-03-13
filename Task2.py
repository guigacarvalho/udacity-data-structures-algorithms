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
phone_dict = {}
for call in calls:
    acc_call_duration_0 = int(phone_dict.get(call[0], 0)) + int(call[3])
    acc_call_duration_1 = int(phone_dict.get(call[1], 0)) + int(call[3])
    phone_dict.update({ call[0]: acc_call_duration_0 })
    phone_dict.update({ call[1]: acc_call_duration_1 })

longest_time_phone_number = max(phone_dict, key=lambda x:phone_dict.get(x))
longest_time = phone_dict.get(longest_time_phone_number)

print(longest_time_phone_number, "spent the longest time,", longest_time, "seconds, on the phone during September 2016.")
