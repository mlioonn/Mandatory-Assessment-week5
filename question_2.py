"""Functions and Strings
All code for this question must be written in the file question_2.py provided.
Write a function time_to_seconds(time) which takes a str (string) as a parameter and
returns a time in second as an int. The function should accept the following string format for
the parameter time :
(a) [8 marks] hh:mm:ss where two digits are always used for hours (h), minutes (m), and
seconds (s). For example 01:00:25 represents an hour and twenty five seconds.
(b) [8 marks] mm:ss where two digits are always used for minutes (m), and seconds (s).
For example 01:25 represents a minute and twenty five seconds. This format is always
used when the time is less than an hour.
(c) [4 marks] For any other format the function returns None
"""


def time_to_seconds(time):
    newTimeList = []
    timeList = time.split(":")
    newTimeList = [int(x) for x in timeList]
    if len(newTimeList) != 2 and len(newTimeList) != 3:
        return None
    else:
        if len(newTimeList) == 3:
            seconds = newTimeList[0] * 3600 + newTimeList[1] * 60 + newTimeList[2]
            return seconds
        elif len(newTimeList) == 2:
            seconds = newTimeList[0] * 60 + newTimeList[1] 
            return seconds
        else: 
            return None
        

    
print(time_to_seconds("60:59"))
