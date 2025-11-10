"""
Functions and Strings
All code for this question must be written in the file question_1.py provided.
Write a function seconds_to_time(time) that takes an int as a parameter representing
the time in seconds, and returns a string (str type). The format of the returned String is as
follows:
(a) [8 marks] hh:mm:ss where two digits are always used for hours (h), minutes (m), and
seconds (s) when the time is greater than an hour. For example 3625 seconds is
represented by 01:00:25.
(b) [8 marks] mm:ss where two digits are always used for minutes (m), and seconds (s)
when the time is less than an hour. For examples: 85 seconds is represented by 01:25,
and 16 seconds is represented by 00:16.
(c) [4 marks] In addition the method returns None if the time is negative or greater than
99:59:59
"""


hours = 0
minutes = 0
seconds = 0
def seconds_to_time(time):
    if time < 0 or time > 359999:
        return None
    elif 3600 <= time <= 359999:
        hours = time // 3600
        minutes = (time % 3600) // 60
        seconds = time % 60
        
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    else:
        minutes = time // 60
        seconds = time % 60
        
        return f"{minutes:02}:{seconds:02}"
              
        
