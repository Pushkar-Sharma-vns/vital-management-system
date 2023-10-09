from utility import convert_string_to_datetime, get_vitals_for_username

    
class VitalManagement:
    
    def __init__(self, username, vitals_id=None, value=None, timestamp=None, period=None):
        self.username = username
        self.vitals_id = vitals_id
        self.value = value
        self.timestamp = convert_string_to_datetime(timestamp)
        self.period = period
        # self.id += 1
        
    def create(self, vitals_list):
        vitals = {}
        vitals["username"] = self.username
        vitals["vitals_id"] = self.vitals_id
        vitals["value"] = self.value
        # _timestamp = convert_string_to_datetime(self.timestamp)
        vitals["timestamp"] = self.timestamp
        vitals_list.append(vitals)
        return {"status": "success", "sessage": f"Vital inserted for {self.username}."}     
        
    def get(self, vitals_list):
        try:
            start_time = convert_string_to_datetime(self.period[0])
            end_time = convert_string_to_datetime(self.period[1])
            user_vitals = get_vitals_for_username(self.username, start_time, end_time, vitals_list)
            data = []
            for vital in user_vitals:
                vital.pop(self.username)
                data.append(vital)
            return {"status": "success", "data": data}
            
        except Exception as e:
            print(e, "Please provide complete period data.")
        
    def delete(self, vitals_list):
        ''' Writing algo for deleting vital from Vital list in approx o(1) time. '''
        idx = 0
        deleted = False
        for vitals in vitals_list:
            if vitals.get("username") == self.username and vitals.get("vital_id") == self.vitals_id and \
               vitals.get("timestamp") == self.timestamp: # If no error in __init__() while converting then its fine for self.timestamp
                if idx == len(vitals_list)-1:
                    vitals_list.pop()
                else:
                    vitals_list[idx] = vitals.list.pop()
                deleted = True
                break
            idx += 1
            
        if deleted:
            return {"status": "success", "message": f"Vital deleted for {self.username}"}
        return {"status": "error", "message": "No username with this vital_id on the given timestamp."}
        