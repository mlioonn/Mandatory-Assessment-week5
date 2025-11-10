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
              
        
