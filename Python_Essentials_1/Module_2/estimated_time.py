hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

endtime_mins = (dura + mins)
while endtime_mins >= 60:
    hour += 1
    endtime_mins -= 60
    if hour == 24:
        hour = 0
    
print(str(hour) + ":" + str(endtime_mins))