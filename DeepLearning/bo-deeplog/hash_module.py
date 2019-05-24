


from datetime import datetime
import hashlib

'''
  generate a hash for a text
'''
def textual_hash(input_array, start_position, next_position):

    for index in range(start_position, len(input_array), next_position ):
        t_value = input_array[index].encode('utf8')
        h = hashlib.sha1(t_value)
        n =  int(h.hexdigest(), base=16)
        input_array[index] = n
    return input_array



'''
  generate a hash for a text
'''
def date_milliseconds(input_array, start_position, next_position):

    for index in range(start_position, len(input_array), next_position ):
        utc_time = datetime.strptime(input_array[index], "%Y-%m-%dT%H:%M:%S.%fZ")
        input_array[index] = int(utc_time.timestamp())
    return input_array