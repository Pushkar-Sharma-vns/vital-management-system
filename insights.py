from utility import convert_string_to_datetime, get_vitals_for_username


class AggragationsAndComparison:
    
    def __init__(self, username, vital_id, start_timestamp, end_timestamp):
        self.username = username
        self.vital_id = vital_id
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp
        
    def aggregations(self, vitals_list):
        print(str(vitals_list))
        start_time = convert_string_to_datetime(self.start_timestamp)
        end_time = convert_string_to_datetime(self.end_timestamp)
        user_vitals = get_vitals_for_username(self.username, start_time, end_time, vitals_list)
        aggregates = {}
        for id in self.vital_id:
            sum = 0.0
            cnt = 0
            for vital in user_vitals:
                if vital["vitals_id"] == id:
                    sum += float(vital["value"])
                    cnt += 1
            aggregates[id] = sum/cnt
        
        response = {
            "status": "success",
            "message": "Aggregate fetched successfully.",
            "data": {
                "username": self.username,
                "aggregates": aggregates,
                "start_timestamp": self.start_timestamp,
                "end_timestamp": self.end_timestamp
            }
        }
        return response
    
    # For calulating percentile, The explanation and the test case give is contradicting and I am a bit confused with this logic.
    # So what I have done is,taken average of user vital value from given timestamp and also given it single count in the number of users with below vital.
    def population_insights(self, vitals_list):
        start_time = convert_string_to_datetime(self.start_timestamp)
        end_time = convert_string_to_datetime(self.end_timestamp)
        user_vitals = get_vitals_for_username(self.username, start_time, end_time, vitals_list)
        sum = 0.0
        cnt = 0
        for vital in user_vitals:
            if vital["vitals_id"] == self.vital_id:
                sum += vital.get("value")
                cnt += 1
        average_user_vital = sum/cnt
        cnt = 1
        population = 1
        for vital in vitals_list:
            if vital["username"] != self.username and vital.get("vitals_id") == self.vital_id:
                population += 1
                if vital["value"] < average_user_vital:
                    cnt += 1
        percentile = (cnt*100)/population
        percentile = int(percentile)
        
        response = {
            "status": "success",
            "message": "Population insight fetched successfully.",
            "data": {
                "username": self.username,
                "vital_id": self.vital_id,
                "start_timestamp": self.start_timestamp,
                "end_timestamp": self.end_timestamp,
                "insight": f"Your HeartRate is in the {percentile} percentile."  
            }
        }
        return response
        