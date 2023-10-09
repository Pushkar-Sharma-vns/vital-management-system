from datetime import datetime


def convert_string_to_datetime(timestamp):
    datetime_str = timestamp
    for i in range(0,len(datetime_str)):
        if datetime_str[i] == '/':
            datetime_str[i] = '-'
    if 'Z' not in datetime_str:
        datetime_str += '00:00:00'
    # print(datetime_str)
    datetime_object = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%SZ')
    # print(datetime_object)
    return datetime_object


def get_vitals_for_username(username, start_time, end_time, vitals_list):
    vitals = []
    for vital in vitals_list:
        timestamp = vital.get("timestamp")
        if vital.get("username") == username and (timestamp >= start_time or timestamp <= end_time):
            vitals.append(vital)      
    return vitals
