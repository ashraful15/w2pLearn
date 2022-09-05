import datetime
# ---- example index page ----
def index():

    timeStart = '2021-03-08 10:42:16'
    timeStart = datetime.datetime.strptime(timeStart, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %I:%M:%S")

    timeEnd = '2021-12-08 10:43:16'
    timeEnd = datetime.datetime.strptime(timeEnd, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %I:%M:%S")

    date_fixed = str(datetime.datetime.now())[:19]
    timeNow = datetime.datetime.strptime(date_fixed, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %I:%M:%S")


    if timeNow>timeStart and timeNow<timeEnd:
        retStr= 'OK'
    else:
        retStr = 'NOT OK'


    return retStr