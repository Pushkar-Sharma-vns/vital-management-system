import json

from insights import AggragationsAndComparison
from user import CreateUser
from vitals import VitalManagement

        
if __name__ == "__main__":
    json_file = open('test_cases.json')
    input_data = json.load(json_file)
    
    user_list = []
    vitals_list = []

    response = []
    for json_object in input_data:
        try:
            command = json_object.pop('command')
            
            if command == 'create_user':
                user_instance = CreateUser(json_object["username"], json_object["age"], json_object["gender"], json_object.get("medical_condition"))
                res = user_instance.create(user_list)
                response.append(res)
                print(res)
                
            elif command == 'insert_vital':
                vital_instance = VitalManagement(json_object["username"], json_object["vital_id"], json_object["value"], json_object["timestamp"])
                res = vital_instance.create(vitals_list)
                print(res)
                
            elif command == 'get_vitals':
                vital_instance = VitalManagement(json_object["username", json_object["period"]])
                res = vital_instance.get(vitals_list)
                response.append(res)
                print(res)
            
            elif command == 'delete_vitals':
                vital_instance = VitalManagement(json_object["username"], json_object["vital_id"], json_object["timestamp"])
                res = vital_instance.delete(vitals_list)
                response.append(res)
                print(res)
                
            elif command == 'aggregate':
                aggregate_instance = AggragationsAndComparison(json_object["username"], json_object["vital_ids"], json_object["start_timestamp"], \
                                     json_object["end_timestamp"])
                res = aggregate_instance.aggregations(vitals_list)
                response.append(res)
                print(res)
                
            elif command == 'population_insight':
                insight_instance = AggragationsAndComparison(json_object["username"], json_object["vital_id"], json_object["start_timestamp"], \
                                   json_object["end_timestamp"])
                res = insight_instance.population_insights(vitals_list)
                response.append(res)
                print(res)
            
        except Exception as e:
            print(e)