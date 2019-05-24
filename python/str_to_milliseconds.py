


from datetime import datetime

utc_time = datetime.strptime("2015-09-15T17:13:29.380Z", "%Y-%m-%dT%H:%M:%S.%fZ")


utc_time2 = datetime.strptime("2018-05-29T22:09:30.380Z", "%Y-%m-%dT%H:%M:%S.%fZ")

milliseconds = (utc_time - datetime(1970, 1, 1))

timestamp = utc_time.timestamp()
timestamp2 = utc_time2.timestamp()

print(milliseconds)
print( int(timestamp) )
print( int(timestamp2) )