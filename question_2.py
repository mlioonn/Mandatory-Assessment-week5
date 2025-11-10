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