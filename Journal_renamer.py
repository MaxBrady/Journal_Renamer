#!/usr/bin/python
#max_journal_2020-11-17.txt
import os

WORKING_DIR = "/Users/maxbrady/Journal"

DIR_CONTENTS = os.listdir(WORKING_DIR)
for content in DIR_CONTENTS:
    print()
    print(content)
    #To skip over entries that can't be automatically converted like "Sep920". Single digit days.
    if len(content) == 6: 
        continue
    if content.startswith('max_journal_2020-'):
    #ignore allready renamed files.
        print("ignoring")
        continue
    if content.upper().startswith('NOV') or content.upper().startswith('OCT') or content.upper().startswith ('SEP'):
        print("Upper Month")
        #Files were created only in Nov, Oct, Sep. No other months were created.      
        month = content[0:3] 
        print(month)
        day_raw = content[3:5] 
        print(day_raw)
        try: 
            day_int = int(day_raw)
        except ValueError:
            print("Filename Format Error: %s" % content)
            continue
        print(day_int)


#Construct new filename
# We need to look at month variable and create month_numeric based on the value of month.
# Example: If month is "nov" then month_numeric should be "11"
    print("about to check Nov") 
    print("month: %s" % month)
    
    if month.lower() == "nov":
        print("Month starts with Nov")
        month_numeric = 11
    print("about to check Oct")
    if month.lower() == "oct":
        print("Month starts with Oct")
        month_numeric = 10
    print("about to check Sep")
    if month.lower() == "sep":
        print("Month starts with Sep")
        month_numeric = 9
       
    # Continue with setting month_numeric for Oct and Sept.
    # Now construct new filename using month_numeric, day_int, and the year 2020.
    # New filename should be in format max_journal_2020-11-17.txt.v
    
# new_filename = max_journal_2020-month_numeric-day_int.txt
#   print(new_filename)

    new_filename = "max_journal_2020-%02d-%02d.txt" % (month_numeric, day_int)
    print('old fn: %s; new fn: %s' % (content, new_filename))
    os.rename(os.path.join(WORKING_DIR, content), os.path.join(WORKING_DIR, new_filename))
