def format_duration(seconds):
    SECOND_YEARS = 31536000
    SECOND_DAYS = 86400
    SECOND_HOURS = 3600
    SECOND_MINUTES = 60
    SECOND = 1
    result = ""
    temp_div = 0
    temp_mod = 0
    unit = ""
    if(seconds == 0):
        return "now"
    while(seconds > 0):
        if(seconds >= SECOND_YEARS):
            temp_div = int(seconds / SECOND_YEARS)
            temp_mod = int(seconds % SECOND_YEARS)
            unit = "year"
        elif(seconds >= SECOND_DAYS):
            temp_div = int(seconds / SECOND_DAYS)
            temp_mod = int(seconds % SECOND_DAYS)
            unit = "day"
        elif(seconds >= SECOND_HOURS):
            temp_div = int(seconds / SECOND_HOURS)
            temp_mod = int(seconds % SECOND_HOURS)
            unit = "hour"
        elif(seconds >= SECOND_MINUTES):
            temp_div = int(seconds / SECOND_MINUTES)
            temp_mod = int(seconds % SECOND_MINUTES)
            unit = "minute"
        elif(seconds >= SECOND):
            temp_div = int(seconds / SECOND)
            temp_mod = int(seconds % SECOND)
            unit = "second"
        if(temp_div > 1):
            unit += "s"
        if(temp_mod == 0):
            if(result == ""):
                result += str(temp_div) + " " + unit
            else:
                result = result[:-2]
                result += " and "  + str(temp_div) + " " + unit
        else:
            result += str(temp_div) + " " + unit + ", "
        seconds = temp_mod
    return result


# print(format_duration(0))
# print(format_duration(1))
# print(format_duration(2))
# print(format_duration(60))
# print(format_duration(62))
# print(format_duration(15731080))
# print(format_duration(132030240))
# print(format_duration(205851834))
# print(format_duration(253374061))
# print(format_duration(242062374))
# print(format_duration(101956166))
# print(format_duration(33243586))
    
# times = [("year", 365 * 24 * 60 * 60), 
#          ("day", 24 * 60 * 60),
#          ("hour", 60 * 60),
#          ("minute", 60),
#          ("second", 1)]

# def format_duration(seconds):

#     if not seconds:
#         return "now"

#     chunks = []
#     for name, secs in times:
#         qty = seconds // secs
#         if qty:
#             if qty > 1:
#                 name += "s"
#             chunks.append(str(qty) + " " + name)

#         seconds = seconds % secs

#     return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]